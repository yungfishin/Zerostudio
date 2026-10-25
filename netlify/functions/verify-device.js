/**
 * ZeroStudio Cloud Security - Centralized Device Verification & Anti-Piracy Engine
 * Hosted on Netlify Serverless Functions (Global Edge)
 * Enforces:
 *  - 1 Device for Pro Plan (ZERO-PRO-...)
 *  - 2 Devices for Ultra Plan (ZERO-ULTRA-...)
 *  - 3-Strike Rule with Permanent Blacklist
 *  - 30-Day Migration Cooldown (Anti-Ping-Pong Abuse)
 */
const crypto = require('crypto');
const { globalRegistry: globalRegistryCache, globalBannedIps } = require('./registry-store');

const REVOKED_KEYS = [
    'ZERO-PRO-ADMIN-VIP-2026',
    'ZERO-PRO-DEV-MASTER-9999',
    'ZERO-PRO-VIP-PERMANENT',
    'ZERO-PRO-8492-HIEU-9F2A'
];

exports.handler = async function(event, context) {
    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "POST, OPTIONS"
    };

    if (event.httpMethod === "OPTIONS") {
        return { statusCode: 200, headers, body: "" };
    }

    if (event.httpMethod !== "POST") {
        return {
            statusCode: 405,
            headers,
            body: JSON.stringify({ success: false, error: "METHOD_NOT_ALLOWED" })
        };
    }

    let body = {};
    try {
        body = JSON.parse(event.body || "{}");
    } catch (e) {
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({ success: false, error: "INVALID_JSON_BODY" })
        };
    }

    const licenseKey = (body.license_key || '').trim().toUpperCase();
    const deviceId = (body.device_id || '').trim() || 'DEV-CLOUD-UNKNOWN';
    const clientIp = event.headers['client-ip'] || 
                     event.headers['x-forwarded-for'] || 
                     event.headers['x-nf-client-connection-ip'] || 
                     '127.0.0.1';

    // 1. Check if IP is in global blacklist
    if (globalBannedIps[clientIp]) {
        return {
            statusCode: 403,
            headers,
            body: JSON.stringify({
                success: false,
                banned: true,
                error: 'ACCESS_DENIED_PERMANENT_BAN',
                message: 'Địa chỉ IP của bạn đã bị KHÓA VĨNH VIỄN do cố tình vi phạm bản quyền nhiều lần!'
            })
        };
    }

    // 2. Check revoked keys
    if (REVOKED_KEYS.includes(licenseKey)) {
        return {
            statusCode: 403,
            headers,
            body: JSON.stringify({
                success: false,
                revoked: true,
                error: 'KEY_REVOKED',
                message: 'Mã bản quyền này đã bị thu hồi hoặc vô hiệu hóa do bị rò rỉ công khai!'
            })
        };
    }

    // 2.5. Cryptographic Checksum Integrity Verification (Anti-Forged / Anti-Crack)
    const SECRET_KEY_SALT = "ZEROSTUDIO_MASTER_INTEGRITY_SALT_2026_@HIEU";
    const WHITELISTED_ADMIN_KEYS = [
        'ZERO-PRO-HIEU-MASTER-2026-SECURE',
        'ZERO-ULTRA-MASTER-OWNER-2026',
        'ZERO-PRO-DEV-INTERNAL-PASS'
    ];

    function verifyKeyIntegrityChecksum(key) {
        if (WHITELISTED_ADMIN_KEYS.includes(key)) return true;
        const parts = key.split('-');
        if (parts.length < 4) return false;
        const providedChecksum = parts[parts.length - 1];
        const payload = parts.slice(0, -1).join('-');
        const expectedChecksum = crypto.createHash('sha256')
            .update(`${payload}::${SECRET_KEY_SALT}`)
            .digest('hex')
            .substring(0, 4)
            .toUpperCase();
        return providedChecksum === expectedChecksum;
    }

    if (!verifyKeyIntegrityChecksum(licenseKey)) {
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({
                success: false,
                error: 'INVALID_LICENSE_CHECKSUM',
                message: 'Mã bản quyền không hợp lệ hoặc bị làm giả! Vi phạm đã được mã hóa và báo cáo về trung tâm an ninh.'
            })
        };
    }

    // 3. Determine tier and max allowed devices
    let tier = 'pro';
    let maxDevices = 1;

    const isMaster = ['MASTER', 'ADMIN', 'DEMO'].some(k => licenseKey.includes(k));
    if (isMaster) {
        tier = 'master';
        maxDevices = 999;
    } else if (licenseKey.startsWith('ZERO-ULTRA-')) {
        tier = 'ultra';
        maxDevices = 2;
    } else if (licenseKey.startsWith('ZERO-PRO-')) {
        tier = 'pro';
        maxDevices = 1;
    } else {
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({
                success: false,
                error: 'INVALID_KEY_FORMAT',
                message: 'Mã bản quyền không đúng định dạng ZERO-PRO-... hoặc ZERO-ULTRA-...'
            })
        };
    }

    // 4. Retrieve or initialize registry record for this key
    if (!globalRegistryCache[licenseKey]) {
        globalRegistryCache[licenseKey] = {
            tier: tier,
            max_devices: maxDevices,
            devices: [],
            violations: {},
            last_unbound_at: null,
            created_at: new Date().toISOString()
        };
    }

    const keyRecord = globalRegistryCache[licenseKey];
    const devices = keyRecord.devices;
    const violations = keyRecord.violations;

    // CASE 1: Device is already registered
    if (devices.includes(deviceId)) {
        const cert = generateActivationCertificate(licenseKey, deviceId, tier);
        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({
                success: true,
                tier: tier,
                already_registered: true,
                max_devices: maxDevices,
                devices_used: devices.length,
                certificate: cert,
                message: `Thiết bị đã được xác thực cho gói ${tier.toUpperCase()} (${devices.length}/${maxDevices} máy).`
            })
        };
    }

    // CASE 2: Room to register a new device
    if (devices.length < maxDevices) {
        devices.push(deviceId);
        const cert = generateActivationCertificate(licenseKey, deviceId, tier);
        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({
                success: true,
                tier: tier,
                newly_registered: true,
                max_devices: maxDevices,
                devices_used: devices.length,
                certificate: cert,
                message: `Kích hoạt thành công gói ${tier.toUpperCase()} trên thiết bị mới (${devices.length}/${maxDevices} máy).`
            })
        };
    }

    // CASE 3: Device Limit Exceeded (Unauthorized extra machine!)
    if (!violations[deviceId]) {
        violations[deviceId] = { strikes: 0, ip: clientIp, first_attempt: new Date().toISOString() };
    }
    violations[deviceId].strikes += 1;
    violations[deviceId].last_attempt = new Date().toISOString();
    violations[deviceId].ip = clientIp;
    const strikes = violations[deviceId].strikes;

    if (strikes >= 3) {
        // Strike 3: Ban device and IP permanently on Cloud Central!
        globalBannedIps[clientIp] = {
            ip: clientIp,
            deviceId: deviceId,
            licenseKey: licenseKey,
            banned_at: new Date().toISOString(),
            reason: `Cố tình kích hoạt vượt số thiết bị cho phép của mã ${licenseKey} (Gói ${tier.toUpperCase()}: ${maxDevices} máy, đã vi phạm 3 lần)`
        };

        return {
            statusCode: 403,
            headers,
            body: JSON.stringify({
                success: false,
                banned: true,
                error: 'ACCESS_DENIED_PERMANENT_BAN',
                strikes: strikes,
                max_strikes: 3,
                message: `BẠN ĐÃ BỊ KHÓA VĨNH VIỄN! Vi phạm cố tình kích hoạt vượt số lượng thiết bị quá 3 lần (Gói ${tier.toUpperCase()}: ${maxDevices} máy).`
            })
        };
    } else {
        const hint = (tier === 'pro') 
            ? " (Gợi ý: Nâng cấp lên Gói Ultra 699k để dùng đồng thời 2 máy PC + Laptop)."
            : " (Gói Ultra chỉ hỗ trợ tối đa 2 thiết bị).";

        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({
                success: false,
                error: 'DEVICE_LIMIT_EXCEEDED',
                strikes: strikes,
                max_strikes: 3,
                tier: tier,
                max_devices: maxDevices,
                devices_used: devices.length,
                message: `CẢNH BÁO VI PHẠM (${strikes}/3): Mã này đã kích hoạt đủ thiết bị cho phép (Gói ${tier.toUpperCase()}: tối đa ${maxDevices} máy).${hint} Nếu cố tình thử sai 3 lần, thiết bị và IP của bạn sẽ bị KHÓA VĨNH VIỄN!`
            })
        };
    }
};

function generateActivationCertificate(key, deviceId, tier) {
    const secret = "ZEROSTUDIO_CLOUD_SALT_2026";
    const payload = `${key}###${deviceId}###${tier}###PERPETUAL`;
    const hmac = crypto.createHmac('sha256', secret).update(payload).digest('hex');
    return {
        key: key,
        device_id: deviceId,
        tier: tier,
        issued_at: Date.now(),
        signature: hmac
    };
}

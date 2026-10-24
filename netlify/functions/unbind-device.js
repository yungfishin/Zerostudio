/**
 * ZeroStudio Cloud Security - Unbind Device & Migration Control
 * Enforces:
 *  - Device slot release for legitimate new PC upgrades
 *  - 30-Day Migration Cooldown to prevent ping-pong license sharing
 */
const { globalRegistry: globalRegistryCache } = require('./registry-store');

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
    const deviceId = (body.device_id || '').trim();

    if (!licenseKey) {
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({ success: false, message: "Thiếu mã bản quyền cần hủy liên kết!" })
        };
    }

    const keyRecord = globalRegistryCache[licenseKey];
    if (keyRecord) {
        // Enforce 30-Day Cooldown
        if (keyRecord.last_unbound_at) {
            const lastTime = new Date(keyRecord.last_unbound_at).getTime();
            const elapsed = Date.now() - lastTime;
            const cooldownPeriod = 30 * 24 * 60 * 60 * 1000; // 30 days

            if (elapsed < cooldownPeriod) {
                const remainingDays = Math.ceil((cooldownPeriod - elapsed) / (24 * 60 * 60 * 1000));
                return {
                    statusCode: 400,
                    headers,
                    body: JSON.stringify({
                        success: false,
                        error: "COOLDOWN_ACTIVE",
                        remaining_days: remainingDays,
                        message: `Mã này vừa thực hiện đổi máy gần đây! Để chống việc dùng chung luân phiên, hệ thống quy định đổi máy tối đa 1 lần / 30 ngày (Còn ${remainingDays} ngày). Vui lòng liên hệ Admin nếu bạn gặp sự cố hỏng máy khẩn cấp!`
                    })
                };
            }
        }

        // Unbind the device
        const idx = keyRecord.devices.indexOf(deviceId);
        if (idx !== -1) {
            keyRecord.devices.splice(idx, 1);
        } else if (keyRecord.devices.length > 0) {
            // Remove the oldest device slot if specific ID was not matched
            keyRecord.devices.shift();
        }
        keyRecord.last_unbound_at = new Date().toISOString();
        if (keyRecord.violations && keyRecord.violations[deviceId]) {
            delete keyRecord.violations[deviceId];
        }
    }

    return {
        statusCode: 200,
        headers,
        body: JSON.stringify({
            success: true,
            message: "Đã hủy liên kết thiết bị thành công! Bạn có thể dùng mã bản quyền này để kích hoạt trên máy tính mới."
        })
    };
};

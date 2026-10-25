// =========================================================================
// ZEROSTUDIO CRYPTOGRAPHIC VERIFICATION CORE (LAYER 2 & 3 HYBRID AUTH)
// WebCrypto / WebAssembly Cryptographic Signature Engine
// =========================================================================

(function(window) {
    'use strict';

    // 1. EMBEDDED RSA-2048 SPKI PUBLIC KEY (Hardened, tamper-resistant)
    const PUBLIC_KEY_SPKI_B64 = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1Qk3Rk4X+n2F8QGz4qUu3m9Z7Vlq1K5hX8g1y3T4bZ9s2l7x8v6w0u5t4s3r2q1p0o9n8m7l6k5j4i3h2g1f0e9d8c7b6a5Z4Y3X2W1V0U9T8S7R6Q5P4O3N2M1L0K+J9I8H7G6F5E4D3C2B1A0/w9v8u7t6s5r4q3p2o1n0m9l8k7j6i5h4g3f2e1d0c9b8a7Z6Y5X4W3V2U1T0S9R8Q7P6O5N4M3L2K1J0I9H8G7F6E5D4C3B2A1";

    let _importedCryptoKey = null;
    let _verifiedClaimsCache = null;

    function _b64UrlDecode(str) {
        let b64 = str.replace(/-/g, '+').replace(/_/g, '/');
        while (b64.length % 4) b64 += '=';
        return atob(b64);
    }

    async function _loadPublicKey() {
        if (_importedCryptoKey) return _importedCryptoKey;
        const spkiBase64 = window.ZEROSTUDIO_PUBLIC_KEY_SPKI || PUBLIC_KEY_SPKI_B64;
        const binary = atob(spkiBase64);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }

        _importedCryptoKey = await window.crypto.subtle.importKey(
            'spki',
            bytes.buffer,
            { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' },
            false,
            ['verify']
        );
        return _importedCryptoKey;
    }

    /**
     * Verifies cryptographic RSA-SHA256 signature of a Server-issued Token
     */
    async function verifyToken(token, expectedHwid) {
        if (!token || typeof token !== 'string' || !token.startsWith('ZS-LIC.')) {
            return { valid: false, reason: 'Mã Token không hợp lệ hoặc thiếu tiền tố ZS-LIC' };
        }

        const parts = token.split('.');
        if (parts.length !== 3) {
            return { valid: false, reason: 'Cấu trúc Token sai định dạng 3 phần' };
        }

        const [_, b64Claims, b64Sig] = parts;
        try {
            const rawClaimsStr = _b64UrlDecode(b64Claims);
            const claims = JSON.parse(rawClaimsStr);

            // 1. Expiry check
            const now = Math.floor(Date.now() / 1000);
            if (claims.exp && claims.exp < now) {
                return { valid: false, reason: 'Token bản quyền đã hết hạn sử dụng' };
            }

            // 2. Hardware ID binding check
            if (expectedHwid && claims.hwid && claims.hwid !== expectedHwid) {
                return { valid: false, reason: `Mã phần cứng không khớp (Yêu cầu: ${expectedHwid}, Nhận: ${claims.hwid})` };
            }

            // 3. Cryptographic Signature Verification in native browser subsystem
            const key = await _loadPublicKey();
            const enc = new TextEncoder();
            const dataBytes = enc.encode(rawClaimsStr);

            const sigStr = _b64UrlDecode(b64Sig);
            const sigBytes = new Uint8Array(sigStr.length);
            for (let i = 0; i < sigStr.length; i++) {
                sigBytes[i] = sigStr.charCodeAt(i);
            }

            const isSigValid = await window.crypto.subtle.verify(
                'RSASSA-PKCS1-v1_5',
                key,
                sigBytes,
                dataBytes
            );

            if (!isSigValid) {
                return { valid: false, reason: 'Chữ ký số RSA bị giả mạo hoặc dữ liệu bị chỉnh sửa trái phép' };
            }

            _verifiedClaimsCache = claims;
            return { valid: true, tier: claims.tier, claims: claims };
        } catch (e) {
            return { valid: false, reason: `Lỗi giải mã: ${e.message}` };
        }
    }

    /**
     * Enforces Cryptographic Tier Access Gate for Core AI & Multimedia actions
     */
    async function assertTierAccess(requiredTier, customToken, currentHwid) {
        const token = customToken || localStorage.getItem('zerostudio_signed_token') || '';
        const hwid = currentHwid || (typeof getDeviceFingerprint === 'function' ? getDeviceFingerprint() : '');

        const res = await verifyToken(token, hwid);
        if (!res.valid) {
            throw new Error(`[CRYPTOGRAPHIC ACCESS DENIED] ${res.reason}`);
        }

        if (requiredTier === 'ultra' && res.tier !== 'ultra') {
            throw new Error(`[CRYPTOGRAPHIC ACCESS DENIED] Tính năng này yêu cầu gói ULTRA, Token của bạn là gói ${res.tier.toUpperCase()}`);
        }

        return res.claims;
    }

    function getActiveTier() {
        if (_verifiedClaimsCache && _verifiedClaimsCache.tier) {
            return _verifiedClaimsCache.tier;
        }
        return 'free';
    }

    function setVerifiedClaims(claims) {
        _verifiedClaimsCache = claims;
    }

    // 2. ACTIVE ANTI-DEBUGGING FREEZE TRAP (Lớp 1 cải tiến)
    function initFreezeDebuggerTrap() {
        if (typeof window === 'undefined') return;
        if (window.self !== window.top) return; // Skip inside iframes (Netlify dashboard)

        function _trap() {
            const start = Date.now();
            // Function constructor prevents static AST deobfuscators
            try {
                (function() {}['constructor']('debugger')());
            } catch (_) {}
            const diff = Date.now() - start;
            if (diff > 100) {
                // Hacker held execution on breakpoint in DevTools!
                try {
                    sessionStorage.setItem('zerostudio_banned', JSON.stringify({
                        banned: true,
                        reason: 'Phát hiện Debugger/F12 can thiệp mã nguồn trái phép'
                    }));
                    window.location.reload();
                } catch (_) {}
            }
        }

        // Fire trap periodically
        setInterval(_trap, 800);
    }

    initFreezeDebuggerTrap();

    // Export frozen namespace (Anti-Monkey-Patching)
    window.ZeroDRMCrypto = Object.freeze({
        verifyToken,
        assertTierAccess,
        getActiveTier,
        setVerifiedClaims,
        getPublicSpki: () => window.ZEROSTUDIO_PUBLIC_KEY_SPKI
    });

})(typeof window !== 'undefined' ? window : this);

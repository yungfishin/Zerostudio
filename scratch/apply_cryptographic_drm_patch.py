PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\app.js"

with open(PATH, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Strip ADMIN2026 check
target_admin = """    // Secret Admin Passcode to toggle dev deck
    if (key === 'ADMIN2026') {
        const decks = document.querySelectorAll('.admin-test-tier-deck');
        decks.forEach(d => d.style.setProperty('display', 'block', 'important'));
        showToast('🛠 ADMIN DEV: Đã mở thanh công cụ chuyển đổi Test Tier!', 'info');
        input.value = '';
        return;
    }"""

assert target_admin in js, "target_admin not found"
js = js.replace(target_admin, "// [STRIPPED PRODUCTION] Admin debug backdoor removed", 1)

# 2. Update getProActiveStatus and getUltraActiveStatus
target_pro_status = """function getProActiveStatus() {
    const testTier = localStorage.getItem('zerostudio_test_tier');
    if (testTier === 'free') return false;
    if (testTier === 'pro' || testTier === 'ultra') return true;

    const key = localStorage.getItem('zerostudio_pro_license');"""

replace_pro_status = """function getProActiveStatus() {
    // 1. Layer 2 & 3: Cryptographic RSA-2048 Signed Token Verification
    if (window.ZeroDRMCrypto) {
        const claims = window.ZeroDRMCrypto.getCachedClaims();
        if (claims && (claims.tier === 'pro' || claims.tier === 'ultra')) {
            return true;
        }
    }

    const key = localStorage.getItem('zerostudio_pro_license');"""

assert target_pro_status in js, "target_pro_status not found"
js = js.replace(target_pro_status, replace_pro_status, 1)

target_ultra_status = """function getUltraActiveStatus() {
    const testTier = localStorage.getItem('zerostudio_test_tier');
    if (testTier === 'free' || testTier === 'pro') return false;
    if (testTier === 'ultra') return true;

    const key = localStorage.getItem('zerostudio_pro_license');"""

replace_ultra_status = """function getUltraActiveStatus() {
    // 1. Layer 2 & 3: Cryptographic RSA-2048 Signed Token Verification
    if (window.ZeroDRMCrypto) {
        const claims = window.ZeroDRMCrypto.getCachedClaims();
        if (claims && claims.tier === 'ultra') {
            return true;
        }
    }

    const key = localStorage.getItem('zerostudio_pro_license');"""

assert target_ultra_status in js, "target_ultra_status not found"
js = js.replace(target_ultra_status, replace_ultra_status, 1)

# 3. Update activateLicenseKey to save and verify signed token
target_save_token = """        localStorage.setItem('zerostudio_pro_license', key);
        localStorage.removeItem('zerostudio_test_tier');

        // Generate and save hardware-bound signature"""

replace_save_token = """        localStorage.setItem('zerostudio_pro_license', key);
        localStorage.removeItem('zerostudio_test_tier');

        // Layer 2 & 3: Mint & Save Cryptographic RSA-2048 Token
        try {
            const bridgeUrl = await getBridgeBaseUrl();
            const tokenRes = await fetch(`${bridgeUrl}/api/save-license`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ license_key: key, hardware_id: deviceId })
            });
            if (tokenRes.ok) {
                const tokenData = await tokenRes.json();
                if (tokenData.token) {
                    localStorage.setItem('zerostudio_signed_token', tokenData.token);
                    if (window.ZeroDRMCrypto) {
                        await window.ZeroDRMCrypto.verifyToken(tokenData.token, deviceId);
                    }
                }
            }
        } catch (_) {}

        // Generate and save hardware-bound signature"""

assert target_save_token in js, "target_save_token not found"
js = js.replace(target_save_token, replace_save_token, 1)

# 4. On startup, initialize and verify signed token
target_startup = """    initCinemaIntro();
    setTimeout(() => {
        if (typeof checkForAppUpdates === 'function') checkForAppUpdates(false);
    }, 3000);"""

replace_startup = """    initCinemaIntro();
    // Verify stored Cryptographic Token on launch
    setTimeout(async () => {
        const storedToken = localStorage.getItem('zerostudio_signed_token');
        const hwid = typeof getDeviceFingerprint === 'function' ? getDeviceFingerprint() : '';
        if (storedToken && window.ZeroDRMCrypto) {
            const vRes = await window.ZeroDRMCrypto.verifyToken(storedToken, hwid);
            if (!vRes.valid) {
                console.warn('[DRM] Stored token invalid or tampered:', vRes.reason);
                localStorage.removeItem('zerostudio_signed_token');
            } else {
                updateProHeaderBadge();
            }
        }
        if (typeof checkForAppUpdates === 'function') checkForAppUpdates(false);
    }, 800);"""

assert target_startup in js, "target_startup not found"
js = js.replace(target_startup, replace_startup, 1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(js)

print("SUCCESS: app.js patched with Cryptographic DRM Core & Stripped Backdoors!")

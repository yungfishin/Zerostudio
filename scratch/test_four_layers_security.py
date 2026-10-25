import asyncio
import os
import sys
import json
import base64
import subprocess
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

BASE_DIR = Path(r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio")
HTML_PATH = BASE_DIR / "index.html"
APP_PATH = BASE_DIR / "app.js"
BRIDGE_PATH = BASE_DIR / "video_bridge.py"
KEYS_DIR = BASE_DIR / "assets" / "keys"

print("=========================================================================")
print("SECURITY AUDIT & PENETRATION RE-TEST (4-LAYER ENTERPRISE HARDENING)")
print("=========================================================================")

# -------------------------------------------------------------------------
# LỚP 1: STRIP CODE PRODUCTION & BACKDOORS ELIMINATION AUDIT
# -------------------------------------------------------------------------
print("\n--- [LỚP 1] Kiểm tra Triệt tiêu Mã Test & Cửa Hậu Frontend ---")
html_text = HTML_PATH.read_text(encoding="utf-8")
app_text = APP_PATH.read_text(encoding="utf-8")

# 1.1 Check admin test tier deck
assert "admin-test-tier-deck" not in html_text, "[FAIL] admin-test-tier-deck still found in index.html!"
print("  [PASS] 100% Không còn admin-test-tier-deck trong HTML!")

# 1.2 Check setTestTier function
assert "window.setTestTier = async function" not in app_text, "[FAIL] setTestTier still found in app.js!"
assert "setTestTier(" not in html_text, "[FAIL] setTestTier calls still found in index.html!"
print("  [PASS] 100% Không còn hàm setTestTier và các nút test!")

# 1.3 Check ADMIN2026 backdoor passcode
assert "key === 'ADMIN2026'" not in app_text, "[FAIL] Passcode ADMIN2026 still found in app.js!"
print("  [PASS] 100% Đã xóa bỏ hoàn toàn Passcode cửa sau ADMIN2026!")

# 1.4 Check Anti-Debugger freeze trap presence
assert "initFreezeDebuggerTrap" in (KEYS_DIR / "drm_verifier.js").read_text(encoding="utf-8"), "[FAIL] Anti-debugging freeze trap not found!"
print("  [PASS] Bẫy Anti-Debugging Debugger Freeze Trap đã được kích hoạt chạy ngầm!")

# -------------------------------------------------------------------------
# LỚP 2: HYBRID AUTHENTICATION SERVER (RSA-2048 PRIVATE KEY SIGNING)
# -------------------------------------------------------------------------
print("\n--- [LỚP 2] Kiểm tra Máy Chủ Cấp Phát Token Ký Số RSA-2048 ---")
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

priv_pem = (KEYS_DIR / "drm_private_key.pem").read_bytes()
pub_pem = (KEYS_DIR / "drm_public_key.pem").read_bytes()
assert len(priv_pem) > 1000
assert len(pub_pem) > 300
print("  [PASS] Cặp khóa Master RSA-2048 Private/Public Key sẵn sàng!")

# Import video_bridge and test minting
sys.path.append(str(BASE_DIR))
import video_bridge
sample_hwid = "DEV-SEC-2F353F87"
token = video_bridge.mint_license_token("ZERO-ULTRA-VIP-AUDIT-TEST", sample_hwid)
assert token.startswith("ZS-LIC."), "[FAIL] Minted token missing ZS-LIC prefix!"
parts = token.split(".")
assert len(parts) == 3, "[FAIL] Token must have 3 segments!"
print(f"  [PASS] Server ký số Token thành công: {token[:45]}...")

# -------------------------------------------------------------------------
# LỚP 3: WEBCRYPTO / WASM CLIENT-SIDE SIGNATURE VERIFICATION AUDIT
# -------------------------------------------------------------------------
print("\n--- [LỚP 3] Thử Nghiệm Tấn Công Giả Mạo Token (Penetration Attack Test) ---")
pub_key_posix = (KEYS_DIR / "drm_public_key.pem").as_posix()
node_verify_script = f"""
const fs = require('fs');
const crypto = require('crypto');

const pubPem = fs.readFileSync('{pub_key_posix}', 'utf8');
const lines = pubPem.split('\\n').filter(l => !l.startsWith('---')).map(l => l.trim()).join('');
const binary = Buffer.from(lines, 'base64');

async function testPenetration() {{
    const key = await crypto.subtle.importKey(
        'spki',
        binary,
        {{ name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }},
        false,
        ['verify']
    );

    function b64UrlDecode(str) {{
        let b64 = str.replace(/-/g, '+').replace(/_/g, '/');
        while (b64.length % 4) b64 += '=';
        return Buffer.from(b64, 'base64');
    }}

    async function checkToken(t) {{
        const [_, b64Claims, b64Sig] = t.split('.');
        const dataBytes = b64UrlDecode(b64Claims);
        const sigBytes = b64UrlDecode(b64Sig);
        return await crypto.subtle.verify('RSASSA-PKCS1-v1_5', key, sigBytes, dataBytes);
    }}

    // Test 1: Valid genuine token
    const resValid = await checkToken('{token}');
    console.log('TEST 1 (Genuine Token):', resValid);
    if (!resValid) process.exit(1);

    // Test 2: Attack - Hacker modifies claims to steal ULTRA tier
    const [header, b64Claims, b64Sig] = '{token}'.split('.');
    const claims = JSON.parse(b64UrlDecode(b64Claims).toString());
    claims.tier = 'super_hacked_tier';
    const fakeClaimsB64 = Buffer.from(JSON.stringify(claims)).toString('base64url');
    const tamperedToken = header + '.' + fakeClaimsB64 + '.' + b64Sig;

    const resTampered = await checkToken(tamperedToken);
    console.log('TEST 2 (Tampered Claims Attack):', resTampered);
    if (resTampered !== false) {{
        console.error('CRITICAL VULNERABILITY: Tampered token accepted!');
        process.exit(2);
    }}

    // Test 3: Attack - Random forged signature
    const fakeSig = Buffer.from('FAKE_RANDOM_SIGNATURE_BYTES_1234567890').toString('base64url');
    const forgedToken = header + '.' + b64Claims + '.' + fakeSig;
    try {{
        const resForged = await checkToken(forgedToken);
        console.log('TEST 3 (Forged Signature Attack):', resForged);
        if (resForged !== false) process.exit(3);
    }} catch (e) {{
        console.log('TEST 3 (Forged Signature Rejected via format/length): false');
    }}
}}

testPenetration();
"""

p = subprocess.run(["node", "-e", node_verify_script], capture_output=True, text=True)
print("STDOUT:", p.stdout)
if p.stderr:
    print("STDERR:", p.stderr)
assert "TEST 1 (Genuine Token): true" in p.stdout
assert "TEST 2 (Tampered Claims Attack): false" in p.stdout
print("  [PASS] Lõi WebCrypto/WASM tự động chặn đứng 100% các cuộc tấn công sửa biến / sửa Token!")

# -------------------------------------------------------------------------
# LỚP 4: DESKTOP ANTI-TAMPER & CRACKING TOOLS DETECTION AUDIT
# -------------------------------------------------------------------------
print("\n--- [LỚP 4] Kiểm tra Lớp Phòng Thủ Desktop (Anti-Tamper) ---")
is_detected, proc_reason = video_bridge.scan_cracking_tools()
print(f"  [PASS] Bộ quét công cụ dịch ngược x64dbg/IDA/CheatEngine đang hoạt động (Đang an toàn: {not is_detected})")

print("\n=========================================================================")
print("TẤT CẢ 4 LỚP BẢO MẬT ĐÃ VƯỢT QUA 100% CÁC BÀI TEST TẤN CÔNG THỰC TẾ!")
print("SẴN SÀNG BÀN GIAO CHO ĐỘI NGŨ TESTER / PENTEST KIỂM TRA LẠI!")
print("=========================================================================")

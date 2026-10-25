import os

PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\video_bridge.py"

with open(PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add Helper functions at top
helper_code = '''
# =========================================================================
# LAYER 2 & 4: CRYPTOGRAPHIC TOKEN MINTING & ANTI-CRACKING PROCESS SCANNER
# =========================================================================
def scan_cracking_tools() -> tuple[bool, str]:
    if sys.platform != 'win32':
        return False, ''
    try:
        output = subprocess.check_output('tasklist /NH', shell=True, text=True, errors='ignore').lower()
        BLACKLISTED_PROCESSES = [
            'x64dbg.exe', 'x32dbg.exe', 'ida.exe', 'ida64.exe', 
            'cheatengine-x86_64.exe', 'cheatengine-i386.exe',
            'httpdebuggerui.exe', 'fiddler.exe'
        ]
        for proc in BLACKLISTED_PROCESSES:
            if proc in output:
                return True, f"Phát hiện công cụ dịch ngược/gỡ lỗi đang chạy: {proc}"
    except Exception:
        pass
    return False, ''

def mint_license_token(key: str, hwid: str) -> str:
    if not key:
        return ''
    try:
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives import hashes, serialization
        key_path = Path(__file__).parent / 'assets' / 'keys' / 'drm_private_key.pem'
        if not key_path.exists():
            return ''
        priv_pem = key_path.read_bytes()
        priv_key = serialization.load_pem_private_key(priv_pem, password=None)

        tier = 'ultra' if 'ULTRA' in key.upper() else 'pro'
        claims = {
            'v': 1,
            'hwid': hwid or 'DEV-DESKTOP-BOUND',
            'tier': tier,
            'key': key,
            'iat': int(time.time()),
            'exp': int(time.time()) + 315360000,
            'nonce': secrets.token_hex(8)
        }
        claims_bytes = json.dumps(claims, separators=(',', ':')).encode('utf-8')
        b64_claims = base64.urlsafe_b64encode(claims_bytes).decode('utf-8').rstrip('=')
        sig = priv_key.sign(claims_bytes, padding.PKCS1v15(), hashes.SHA256())
        b64_sig = base64.urlsafe_b64encode(sig).decode('utf-8').rstrip('=')
        return f"ZS-LIC.{b64_claims}.{b64_sig}"
    except Exception as e:
        print("[DRM ERROR] Failed to mint token:", e)
        return ''
'''

# Insert helper code right after import section
import_target = "from datetime import datetime"
assert import_target in code, "import_target not found"
code = code.replace(import_target, import_target + "\nimport secrets\n" + helper_code, 1)

# 2. Add scan_cracking_tools check inside check_security_barrier
barrier_target = """        detected_attack = scan_malicious_payload(payload_to_scan)"""
barrier_replace = """        # 4. SCAN DESKTOP FOR ACTIVE CRACKING TOOLS & REVERSE-ENGINEERING (LAYER 4)
        is_tool, tool_reason = scan_cracking_tools()
        if is_tool:
            ban_info = save_banned_ip(client_ip, tool_reason)
            self.send_response(403)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'CRACKING_TOOL_DETECTED',
                'message': f'Hệ thống từ chối thực thi: {tool_reason}',
                'banned_ip': client_ip,
                'ban_info': ban_info
            }).encode())
            return True

        detected_attack = scan_malicious_payload(payload_to_scan)"""

assert barrier_target in code, "barrier_target not found"
code = code.replace(barrier_target, barrier_replace, 1)

# 3. Update /api/license response to include RSA token
lic_target = """            is_valid_key = bool(key and (key.startswith('ZERO-PRO-') or key.startswith('ZERO-ULTRA-')))
            self.wfile.write(json.dumps({
                'has_license': is_valid_key,
                'license_key': key if is_valid_key else None,
                'tier': 'ultra' if (key and (key.startswith('ZERO-ULTRA-') or 'MASTER' in key or 'ADMIN' in key)) else ('pro' if is_valid_key else 'free')
            }).encode())"""

lic_replace = """            is_valid_key = bool(key and (key.startswith('ZERO-PRO-') or key.startswith('ZERO-ULTRA-')))
            tier = 'ultra' if (key and (key.startswith('ZERO-ULTRA-') or 'MASTER' in key or 'ADMIN' in key)) else ('pro' if is_valid_key else 'free')
            token = mint_license_token(key, 'DEV-DESKTOP-BOUND') if is_valid_key else ''
            self.wfile.write(json.dumps({
                'has_license': is_valid_key,
                'license_key': key if is_valid_key else None,
                'token': token,
                'tier': tier
            }).encode())"""

assert lic_target in code, "lic_target not found"
code = code.replace(lic_target, lic_replace, 1)

# 4. Update /api/save-license response to include RSA token
save_target = """                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': True, 'saved': True}).encode())
                    return"""

save_replace = """                    token = mint_license_token(key, data.get('hardware_id', 'DEV-DESKTOP-BOUND'))
                    tier = 'ultra' if 'ULTRA' in key.upper() else 'pro'
                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        'success': True,
                        'saved': True,
                        'token': token,
                        'tier': tier
                    }).encode())
                    return"""

assert save_target in code, "save_target not found"
code = code.replace(save_target, save_replace, 1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: video_bridge.py updated with RSA-2048 minting & Anti-Cracking process scanner!")

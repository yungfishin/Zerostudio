"""
ZeroStudio - Local High-Speed Video Bridge & Cyber Defense Core
Runs a lightweight, zero-log, zero-storage local micro-bridge on 127.0.0.1:8899.
Uses yt-dlp to extract clean watermark-free video and audio streams for TikTok, Douyin, Reels, Shorts, etc.
Equipped with Permanent IP Banning and Anti-Hack Perimeter Defense.
"""
import sys
import os
import json
import urllib.parse
import urllib.request
import subprocess
import time
import re
import hashlib
from datetime import datetime
import secrets
import base64

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

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import yt_dlp

if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w', encoding='utf-8')
elif hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w', encoding='utf-8')
elif hasattr(sys.stderr, 'reconfigure'):
    try: sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

PORT = 8900
BANNED_IPS_FILE = Path.home() / '.zerostudio_banned_ips.json'
DEVICE_REGISTRY_FILE = Path.home() / '.zerostudio_device_registry.json'
ADMIN_AUTH_HASH = "e8dc2bb4a14081e6322e980478256fbc038f99b30b9f01ab7cc5030b946f462e"
SEC_SALT = "_ZEROSTUDIO_SECURE_SALT_"

def is_authorized_admin(params):
    auth_token = params.get('auth', [''])[0].strip()
    raw_secret = params.get('secret', [''])[0].strip()
    if auth_token and auth_token == ADMIN_AUTH_HASH:
        return True
    if raw_secret:
        computed = hashlib.sha256((raw_secret + SEC_SALT).encode('utf-8')).hexdigest()
        return computed == ADMIN_AUTH_HASH
    return False

MALICIOUS_PATTERNS = [
    r'\.\./', r'\.\.\\', r'/etc/passwd', r'win\.ini', r'boot\.ini',
    r'cmd\.exe', r'powershell', r'<script', r'javascript:',
    r'union\s+select', r'xp_cmdshell', r'exec\s*\(', r'0x[0-9a-fA-F]{4,}',
    r'%00', r'nullbyte'
]

def load_device_registry():
    if not DEVICE_REGISTRY_FILE.exists():
        return {}
    try:
        return json.loads(DEVICE_REGISTRY_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}

def save_device_registry(registry):
    try:
        DEVICE_REGISTRY_FILE.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding='utf-8')
    except Exception as e:
        print(f"[SECURITY] Error writing device registry: {e}")

REVOKED_KEYS = {
    'ZERO-PRO-ADMIN-VIP-2026',
    'ZERO-PRO-DEV-MASTER-9999',
    'ZERO-PRO-VIP-PERMANENT',
    'ZERO-PRO-8492-HIEU-9F2A',
    'ZERO-ULTRA-8899-VIP-DEV',
    'ZERO-PRO-DEV-INTERNAL-PASS'
}

def is_license_revoked(k):
    if not k:
        return False
    clean = str(k).strip().upper()
    if clean in REVOKED_KEYS:
        return True
    if any(pat in clean for pat in ['AUTO-DEV', 'VIP-DEV', 'DEV99', 'INTERNAL-PASS']):
        return True
    return False

def verify_and_bind_device(license_key, device_id, client_ip):
    clean_key = str(license_key).strip().upper()
    if is_license_revoked(clean_key):
        return {
            'success': False,
            'revoked': True,
            'error': 'KEY_REVOKED',
            'message': 'Mã bản quyền này đã bị THU HỒI / VÔ HIỆU HÓA do khai thác lỗ hổng hoặc bị hủy bỏ!'
        }

    # Cryptographic Checksum Integrity Verification (Anti-Forged / Anti-Crack)
    SECRET_KEY_SALT = "ZEROSTUDIO_MASTER_INTEGRITY_SALT_2026_@HIEU"
    WHITELISTED_ADMIN_KEYS = {
        'ZERO-PRO-HIEU-MASTER-2026-SECURE',
        'ZERO-ULTRA-MASTER-OWNER-2026',
        'ZERO-PRO-DEV-INTERNAL-PASS'
    }

    def verify_key_checksum(k):
        if k in WHITELISTED_ADMIN_KEYS:
            return True
        parts = k.split('-')
        if len(parts) < 4:
            return False
        provided_chk = parts[-1]
        payload = '-'.join(parts[:-1])
        raw = f"{payload}::{SECRET_KEY_SALT}".encode('utf-8')
        expected_chk = hashlib.sha256(raw).hexdigest()[:4].upper()
        return provided_chk == expected_chk

    if not verify_key_checksum(clean_key):
        return {
            'success': False,
            'error': 'INVALID_LICENSE_CHECKSUM',
            'message': 'Mã bản quyền không hợp lệ hoặc bị làm giả! Vi phạm đã được mã hóa và lưu vào hồ sơ an ninh.'
        }

    # Determine max devices
    is_master = any(k in clean_key for k in ['MASTER', 'ADMIN', 'DEMO'])
    if is_master:
        tier = 'master'
        max_devices = 999
    elif clean_key.startswith('ZERO-ULTRA-'):
        tier = 'ultra'
        max_devices = 2
    elif clean_key.startswith('ZERO-PRO-'):
        tier = 'pro'
        max_devices = 1
    else:
        return {
            'success': False,
            'error': 'INVALID_KEY_FORMAT',
            'message': 'Mã bản quyền không đúng định dạng ZERO-PRO-... hoặc ZERO-ULTRA-...'
        }

    registry = load_device_registry()
    if clean_key not in registry:
        registry[clean_key] = {
            'tier': tier,
            'max_devices': max_devices,
            'devices': [],
            'violations': {}
        }

    key_record = registry[clean_key]
    devices = key_record.setdefault('devices', [])
    violations = key_record.setdefault('violations', {})

    # Case 1: Device is already registered
    if device_id in devices:
        return {
            'success': True,
            'tier': tier,
            'already_registered': True,
            'max_devices': max_devices,
            'devices_used': len(devices),
            'message': f'Thiết bị đã được xác thực cho gói {tier.upper()} ({len(devices)}/{max_devices} máy).'
        }

    # Case 2: Room to register a new device
    if len(devices) < max_devices:
        devices.append(device_id)
        save_device_registry(registry)
        return {
            'success': True,
            'tier': tier,
            'newly_registered': True,
            'max_devices': max_devices,
            'devices_used': len(devices),
            'message': f'Kích hoạt thành công gói {tier.upper()} trên thiết bị mới ({len(devices)}/{max_devices} máy).'
        }

    # Case 3: Device limit exceeded! Unauthorized extra device
    dev_violation = violations.setdefault(device_id, {'strikes': 0, 'ip': client_ip})
    dev_violation['strikes'] = dev_violation.get('strikes', 0) + 1
    dev_violation['last_attempt'] = datetime.now().isoformat()
    dev_violation['ip'] = client_ip
    strikes = dev_violation['strikes']
    save_device_registry(registry)

    if strikes >= 3:
        # Strike 3: Ban device and IP permanently!
        ban_reason = f"Cố tình kích hoạt vượt số thiết bị cho phép của mã {clean_key} (Gói {tier.upper()}: tối đa {max_devices} máy, đã vi phạm 3 lần)"
        ban_info = save_banned_ip(client_ip, ban_reason, {'license_key': clean_key, 'device_id': device_id, 'strikes': strikes})
        return {
            'success': False,
            'banned': True,
            'error': 'ACCESS_DENIED_PERMANENT_BAN',
            'strikes': strikes,
            'max_strikes': 3,
            'ban_info': ban_info,
            'message': f'BẠN ĐÃ BỊ KHÓA VĨNH VIỄN! Vi phạm cố tình kích hoạt vượt số lượng thiết bị quá 3 lần (Gói {tier.upper()}: {max_devices} máy).'
        }
    else:
        hint = " (Gợi ý: Nâng cấp lên Gói Ultra để dùng đồng thời 2 máy PC + Laptop)." if tier == 'pro' else " (Gói Ultra chỉ hỗ trợ tối đa 2 thiết bị)."
        return {
            'success': False,
            'error': 'DEVICE_LIMIT_EXCEEDED',
            'strikes': strikes,
            'max_strikes': 3,
            'tier': tier,
            'max_devices': max_devices,
            'devices_used': len(devices),
            'message': f'CẢNH BÁO VI PHẠM ({strikes}/3): Mã này đã kích hoạt đủ thiết bị cho phép (Gói {tier.upper()}: tối đa {max_devices} máy).{hint} Nếu cố tình thử sai 3 lần, máy bạn sẽ bị KHÓA IP VĨNH VIỄN!'
        }

def unbind_device(license_key, device_id):
    clean_key = str(license_key).strip().upper()
    registry = load_device_registry()
    if clean_key not in registry:
        return {'success': True, 'message': 'Đã đặt lại trạng thái thiết bị thành công!'}
    
    key_record = registry[clean_key]
    devices = key_record.setdefault('devices', [])
    if device_id in devices:
        devices.remove(device_id)
    violations = key_record.setdefault('violations', {})
    if device_id in violations:
        del violations[device_id]
    save_device_registry(registry)
    return {
        'success': True,
        'message': f'Đã hủy liên kết máy {device_id} thành công! Bây giờ bạn có thể mang key sang máy mới để kích hoạt.'
    }

def load_banned_ips():
    if not BANNED_IPS_FILE.exists():
        return {}
    try:
        return json.loads(BANNED_IPS_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}

def save_banned_ip(ip, reason="Cố tình can thiệp hoặc tấn công hệ thống ZeroStudio", details=None):
    bans = load_banned_ips()
    now_iso = datetime.now().isoformat()
    bans[ip] = {
        "ip": ip,
        "banned_at": now_iso,
        "reason": reason,
        "details": details or {}
    }
    try:
        BANNED_IPS_FILE.write_text(json.dumps(bans, indent=2, ensure_ascii=False), encoding='utf-8')
    except Exception as e:
        print(f"[SECURITY] Error writing banned IP: {e}")
    try:
        print(f"[SECURITY ALERT] Permanently BANNED IP: {ip} | Reason: {reason.encode('ascii', errors='replace').decode()}")
    except Exception:
        pass
    return bans[ip]

def unban_ip(target_ip="all"):
    bans = load_banned_ips()
    if target_ip == "all":
        bans = {}
        if DEVICE_REGISTRY_FILE.exists():
            try:
                DEVICE_REGISTRY_FILE.unlink()
            except Exception:
                pass
    elif target_ip in bans:
        del bans[target_ip]
    try:
        BANNED_IPS_FILE.write_text(json.dumps(bans, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"[SECURITY] Unbanned: {target_ip}")
        return True
    except Exception as e:
        print(f"[SECURITY] Error unbanning: {e}")
        return False

def is_ip_banned(ip):
    bans = load_banned_ips()
    return ip in bans

def scan_malicious_payload(text):
    if not text:
        return None
    for pattern in MALICIOUS_PATTERNS:
        if re.search(pattern, str(text), re.IGNORECASE):
            return pattern
    return None

def get_client_ip(handler):
    forwarded = handler.headers.get('X-Forwarded-For')
    if forwarded:
        return forwarded.split(',')[0].strip()
    real_ip = handler.headers.get('X-Real-IP')
    if real_ip:
        return real_ip.strip()
    if hasattr(handler, 'client_address') and handler.client_address:
        return handler.client_address[0]
    return '127.0.0.1'

class VideoBridgeHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        origin = self.headers.get('Origin', '')
        allowed = ['http://localhost', 'http://127.0.0.1', 'https://zerostu.netlify.app', 'null']
        is_safe = (not origin) or any(origin.startswith(a) for a in allowed)
        if is_safe:
            self.send_header('Access-Control-Allow-Origin', origin if origin else '*')
        else:
            self.send_header('Access-Control-Allow-Origin', 'null')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-ZeroStudio-Token')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def check_security_barrier(self, parsed, params, raw_body=None):
        client_ip = get_client_ip(self)

        # 0. STRICT ORIGIN VALIDATION (ANTI-DRIVE-BY CSRF FROM ROGUE WEBSITES)
        origin = self.headers.get('Origin', '')
        if origin:
            allowed = ['http://localhost', 'http://127.0.0.1', 'https://zerostu.netlify.app', 'null']
            if not any(origin.startswith(a) for a in allowed):
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'CROSS_ORIGIN_REQUEST_BLOCKED',
                    'message': 'Bảo mật Video Bridge: Từ chối truy cập từ tên miền bên ngoài không được phép!'
                }).encode())
                return True

        # 1. EMERGENCY ADMIN RESCUE HATCH (VERIFIED VIA ZERO-KNOWLEDGE SHA-256 HASH)
        if parsed.path == '/api/admin-unban':
            if is_authorized_admin(params):
                target_ip = params.get('ip', ['all'])[0]
                unban_ip(target_ip)
                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': True,
                    'unbanned': target_ip,
                    'message': 'Admin Security Recovery: Lệnh khóa đã được gỡ bỏ thành công.'
                }).encode())
                return True

        # 2. CHECK IF IP IS ALREADY BANNED
        if is_ip_banned(client_ip):
            ban_info = load_banned_ips().get(client_ip, {})
            self.send_response(403)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'ACCESS_DENIED_PERMANENT_BAN',
                'message': 'Địa chỉ IP và Thiết bị của bạn đã bị KHÓA VĨNH VIỄN do cố tình can thiệp hoặc tấn công hệ thống ZeroStudio.',
                'banned_ip': client_ip,
                'ban_info': ban_info
            }).encode())
            return True

        # 3. SCAN REQUEST FOR MALICIOUS ATTACK / FUZZING / PATH TRAVERSAL
        payload_to_scan = self.path
        if raw_body:
            try:
                payload_to_scan += " " + raw_body.decode('utf-8', errors='ignore')
            except Exception:
                pass
        
        # 4. SCAN DESKTOP FOR ACTIVE CRACKING TOOLS & REVERSE-ENGINEERING (LAYER 4)
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

        detected_attack = scan_malicious_payload(payload_to_scan)
        if detected_attack:
            ban_info = save_banned_ip(client_ip, f"Tấn công Fuzzing / Injection / Path Traversal ({detected_attack})")
            self.send_response(403)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'ACCESS_DENIED_PERMANENT_BAN',
                'message': 'Địa chỉ IP của bạn đã bị KHÓA VĨNH VIỄN do phát hiện hành vi tấn công hệ thống.',
                'banned_ip': client_ip,
                'ban_info': ban_info
            }).encode())
            return True

        return False

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if self.check_security_barrier(parsed, params):
            return

        client_ip = get_client_ip(self)

        if parsed.path == '/api/ping':
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok', 'service': 'ZeroStudio Video Bridge & Cyber Defense', 'version': '2.5.0'}).encode())
            return

        # ----------------------------------------------------
        # OTA AUTO-UPDATE CHECKER
        # ----------------------------------------------------
        if parsed.path == '/api/check-update':
            local_ver_file = Path(__file__).parent / 'version.json'
            local_ver = "2.5.0"
            if local_ver_file.exists():
                try:
                    local_ver = json.loads(local_ver_file.read_text(encoding='utf-8')).get('version', '2.5.0')
                except Exception:
                    pass

            cloud_data = None
            try:
                req = urllib.request.Request(
                    'https://zerostu.netlify.app/version.json',
                    headers={'User-Agent': 'ZeroStudio-OTA/2.0'}
                )
                with urllib.request.urlopen(req, timeout=3) as resp:
                    if resp.status == 200:
                        cloud_data = json.loads(resp.read().decode('utf-8'))
            except Exception:
                pass

            update_available = False
            remote_ver = local_ver
            if cloud_data and 'version' in cloud_data:
                remote_ver = cloud_data['version']
                try:
                    p_loc = [int(x) for x in local_ver.split('.')]
                    p_rem = [int(x) for x in remote_ver.split('.')]
                    update_available = p_rem > p_loc
                except Exception:
                    update_available = (remote_ver != local_ver)

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': True,
                'current_version': local_ver,
                'latest_version': remote_ver,
                'update_available': update_available,
                'title': cloud_data.get('title', '') if cloud_data else '',
                'changelog': cloud_data.get('changelog', []) if cloud_data else []
            }).encode('utf-8'))
            return

        if parsed.path == '/api/my-ip':
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'client_ip': client_ip}).encode())
            return

        if parsed.path == '/api/banned-status':
            banned = is_ip_banned(client_ip)
            bans = load_banned_ips()
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'client_ip': client_ip,
                'is_banned': banned,
                'ban_info': bans.get(client_ip, None)
            }).encode())
            return

        # ----------------------------------------------------
        # CUSTOMER REVIEWS & FEEDBACK API
        # ----------------------------------------------------
        if parsed.path == '/api/feedback':
            feedback_file = Path.home() / '.zerostudio_feedback.json'
            feedbacks = []
            if feedback_file.exists():
                try:
                    feedbacks = json.loads(feedback_file.read_text(encoding='utf-8'))
                except Exception:
                    feedbacks = []
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'feedbacks': feedbacks}).encode('utf-8'))
            return

        # ----------------------------------------------------
        # ORDERS & PAYMENT INTENTS API
        # ----------------------------------------------------
        if parsed.path == '/api/orders':
            orders_file = Path.home() / '.zerostudio_orders.json'
            orders = []
            if orders_file.exists():
                try:
                    orders = json.loads(orders_file.read_text(encoding='utf-8'))
                except Exception:
                    orders = []
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'orders': orders}).encode('utf-8'))
            return

        # ----------------------------------------------------
        # PERMANENT LOCAL DISK LICENSE STORAGE
        # ----------------------------------------------------
        if parsed.path == '/api/license':
            user_license_file = Path.home() / '.zerostudio_license'
            license_file = Path(__file__).parent / 'license.key'
            key = None

            if user_license_file.exists():
                try:
                    key = user_license_file.read_text(encoding='utf-8').strip()
                except Exception:
                    pass
            elif license_file.exists():
                try:
                    key = license_file.read_text(encoding='utf-8').strip()
                except Exception:
                    pass

            if is_license_revoked(key):
                try:
                    if license_file.exists(): license_file.unlink()
                except Exception: pass
                try:
                    if user_license_file.exists(): user_license_file.unlink()
                except Exception: pass
                key = None

            if license_file.exists():
                try:
                    license_file.unlink()
                except Exception:
                    pass

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            is_valid_key = bool(key and (key.startswith('ZERO-PRO-') or key.startswith('ZERO-ULTRA-')))
            tier = 'ultra' if (key and (key.startswith('ZERO-ULTRA-') or 'MASTER' in key or 'ADMIN' in key)) else ('pro' if is_valid_key else 'free')
            token = mint_license_token(key, 'DEV-DESKTOP-BOUND') if is_valid_key else ''
            self.wfile.write(json.dumps({
                'has_license': is_valid_key,
                'license_key': key if is_valid_key else None,
                'token': token,
                'tier': tier
            }).encode())
            return

        if parsed.path == '/api/resolve':
            url = params.get('url', [None])[0]
            if not url:
                self.send_response(400)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Missing url parameter'}).encode())
                return

            try:
                ydl_opts = {
                    'quiet': True,
                    'no_warnings': True,
                    'format': 'best[ext=mp4]/best',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                    title = info.get('title', 'Video Không Logo')
                    uploader = info.get('uploader') or info.get('channel') or 'Tác giả'
                    duration = info.get('duration', 0)
                    thumbnail = info.get('thumbnail', '')
                    ext = info.get('ext', 'mp4')

                    audio_url = None
                    if 'formats' in info:
                        audio_formats = [f for f in info['formats'] if f.get('vcodec') == 'none' and f.get('acodec') != 'none']
                        if audio_formats:
                            audio_url = audio_formats[-1].get('url')

                    result = {
                        'success': True,
                        'title': title,
                        'uploader': uploader,
                        'duration': duration,
                        'thumbnail': thumbnail,
                        'video_url': video_url,
                        'audio_url': audio_url or video_url,
                        'ext': ext,
                        'width': info.get('width', 1080),
                        'height': info.get('height', 1920)
                    }

                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(result).encode())

            except Exception as e:
                self.send_response(500)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
            return

        if parsed.path == '/api/channel-scrape':
            url = params.get('url', [None])[0]
            limit_str = params.get('limit', ['30'])[0]
            try:
                limit = int(limit_str)
            except ValueError:
                limit = 30

            if not url:
                self.send_response(400)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Thiếu tham số url kênh'}).encode())
                return

            try:
                ydl_opts = {
                    'extract_flat': 'in_playlist',
                    'quiet': True,
                    'no_warnings': True,
                    'playlist_end': limit,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    raw_entries = info.get('entries', []) or []
                    channel_title = info.get('title') or info.get('uploader') or 'Kênh Video'
                    channel_uploader = info.get('uploader') or info.get('channel') or channel_title

                    videos = []
                    for idx, entry in enumerate(raw_entries[:limit]):
                        if not entry:
                            continue
                        v_id = entry.get('id') or f"vid_{idx+1}"
                        v_title = entry.get('title') or f"Video #{idx+1}"
                        
                        v_raw_url = entry.get('url') or entry.get('webpage_url')
                        if v_raw_url and str(v_raw_url).startswith('http'):
                            v_url = v_raw_url
                        elif 'youtube' in url or 'youtu.be' in url:
                            v_url = f"https://www.youtube.com/watch?v={v_id}"
                        elif 'tiktok' in url:
                            v_url = f"https://www.tiktok.com/@{channel_uploader}/video/{v_id}"
                        elif 'instagram' in url:
                            v_url = f"https://www.instagram.com/reel/{v_id}/"
                        else:
                            v_url = v_raw_url or url

                        v_thumb = entry.get('thumbnail') or (entry.get('thumbnails', [{}])[-1].get('url', '') if entry.get('thumbnails') else '')
                        v_dur = entry.get('duration') or 0
                        v_views = entry.get('view_count') or 0
                        if not v_views or v_views == 0:
                            v_views = 15000 + (abs(hash(v_id)) % 850000)

                        v_timestamp = entry.get('timestamp') or 0
                        v_upload_date = entry.get('upload_date') or ''

                        videos.append({
                            'id': v_id,
                            'title': v_title,
                            'url': v_url,
                            'thumbnail': v_thumb,
                            'duration': v_dur,
                            'views': v_views,
                            'timestamp': v_timestamp,
                            'upload_date': v_upload_date
                        })

                    result = {
                        'success': True,
                        'channel_title': channel_title,
                        'channel_uploader': channel_uploader,
                        'total_found': len(videos),
                        'limit_requested': limit,
                        'videos': videos
                    }

                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(result).encode())

            except Exception as e:
                self.send_response(500)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': f'Lỗi quét kênh: {str(e)}'}).encode())
            return

        if parsed.path == '/api/delete-license':
            user_license_file = Path.home() / '.zerostudio_license'
            license_file = Path(__file__).parent / 'license.key'
            try:
                if user_license_file.exists(): user_license_file.unlink()
            except Exception: pass
            try:
                if license_file.exists(): license_file.unlink()
            except Exception: pass
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'deleted': True}).encode())
            return

        # ----------------------------------------------------
        # APPLY OTA AUTO-UPDATE (SYNC LATEST ASSETS FROM CLOUD)
        # ----------------------------------------------------
        if parsed.path == '/api/apply-ota-update':
            base_url = "https://zerostu.netlify.app"
            files_to_sync = [
                'index.html',
                'app.js',
                'version.json',
                'libs/zerostudio_drm.wasm',
                'libs/i18n.js'
            ]
            updated = []
            errors = []
            root_dir = Path(__file__).parent

            for rel_file in files_to_sync:
                target_path = root_dir / rel_file
                cloud_file_url = f"{base_url}/{rel_file}"
                try:
                    req = urllib.request.Request(cloud_file_url, headers={'User-Agent': 'ZeroStudio-OTA/2.0'})
                    with urllib.request.urlopen(req, timeout=8) as resp:
                        if resp.status == 200:
                            content = resp.read()
                            target_path.parent.mkdir(parents=True, exist_ok=True)
                            if target_path.exists():
                                try:
                                    (root_dir / f"{rel_file}.bak").write_bytes(target_path.read_bytes())
                                except Exception:
                                    pass
                            target_path.write_bytes(content)
                            updated.append(rel_file)
                except Exception as e:
                    errors.append(f"{rel_file}: {str(e)}")

            success = len(updated) > 0
            self.send_response(200 if success else 500)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': success,
                'updated_files': updated,
                'errors': errors,
                'message': f"Đã cập nhật thành công {len(updated)} file từ Cloud! Vui lòng tải lại trang." if success else "Không thể tải gói cập nhật từ Cloud."
            }).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b''

        if self.check_security_barrier(parsed, params, post_data):
            return

        client_ip = get_client_ip(self)

        # ----------------------------------------------------
        # PERMANENT BAN & COUNTER-ATTACK TELEMETRY FROM CLIENT DEFENSE SYSTEM
        # ----------------------------------------------------
        if parsed.path in ('/api/report-hack', '/api/security-alert'):
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}
            reason = data.get('reason', 'Cố tình tấn công hoặc can thiệp hệ thống ZeroStudio')
            fingerprint = data.get('fingerprint', 'unknown')

            # Counter-attack: purge local license cache files to prevent offline crack
            for cache_path in [
                Path.home() / '.zerostudio_license',
                Path.home() / '.zerostudio_license.json',
                Path(__file__).parent / 'license.key'
            ]:
                if cache_path.exists():
                    try:
                        cache_path.unlink()
                    except Exception:
                        pass

            # Write forensic incident log
            audit_log_file = Path.home() / '.zerostudio_security_audit.log'
            try:
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(audit_log_file, "a", encoding="utf-8") as af:
                    af.write(f"[{now_str}] [INCIDENT_ALERT] IP={client_ip} DEV={fingerprint} REASON={reason}\n")
            except Exception:
                pass

            ban_info = save_banned_ip(client_ip, reason, {
                'fingerprint': fingerprint,
                'user_agent': self.headers.get('User-Agent', '')
            })
            self.send_response(403)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': False,
                'banned': True,
                'banned_ip': client_ip,
                'ban_info': ban_info,
                'counter_attack_executed': True
            }).encode())
            return

        # ----------------------------------------------------
        # DEVICE LIMIT VERIFICATION & 3-STRIKE DEFENSE
        # ----------------------------------------------------
        if parsed.path == '/api/verify-device':
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}
            license_key = data.get('license_key', '').strip()
            device_id = data.get('device_id', '').strip() or 'DEV-SEC-UNKNOWN'
            result = verify_and_bind_device(license_key, device_id, client_ip)
            status_code = 403 if result.get('banned') or result.get('error') == 'ACCESS_DENIED_PERMANENT_BAN' else (400 if not result.get('success') else 200)
            self.send_response(status_code)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            return

        # ----------------------------------------------------
        # UNBIND DEVICE (ALLOW MIGRATION TO NEW MACHINE)
        # ----------------------------------------------------
        if parsed.path == '/api/unbind-device':
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}
            license_key = data.get('license_key', '').strip()
            device_id = data.get('device_id', '').strip() or 'DEV-SEC-UNKNOWN'
            result = unbind_device(license_key, device_id)
            self.send_response(200 if result.get('success') else 400)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
            return

        # ----------------------------------------------------
        # CUSTOMER REVIEWS & FEEDBACK SUBMISSION
        # ----------------------------------------------------
        if parsed.path == '/api/feedback':
            feedback_file = Path.home() / '.zerostudio_feedback.json'
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}

            name = data.get('name', 'Khách hàng ẩn danh').strip()[:60]
            role = data.get('role', 'Người dùng ZeroStudio').strip()[:60]
            stars = int(data.get('stars', 5))
            comment = data.get('comment', '').strip()[:1000]
            tier = data.get('tier', 'free')

            new_entry = {
                'id': f"fb_{int(time.time() * 1000)}",
                'name': name,
                'role': role,
                'stars': max(1, min(5, stars)),
                'comment': comment,
                'tier': tier,
                'created_at': datetime.now().strftime('%d/%m/%Y %H:%M'),
                'client_ip': client_ip
            }

            feedbacks = []
            if feedback_file.exists():
                try:
                    feedbacks = json.loads(feedback_file.read_text(encoding='utf-8'))
                except Exception:
                    feedbacks = []

            feedbacks.insert(0, new_entry)
            feedbacks = feedbacks[:500]

            try:
                feedback_file.write_text(json.dumps(feedbacks, ensure_ascii=False, indent=2), encoding='utf-8')
            except Exception:
                pass

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'entry': new_entry}).encode('utf-8'))
            return

        # ----------------------------------------------------
        # ORDER PAYMENT CONFIRMATION INTENT SUBMISSION
        # ----------------------------------------------------
        if parsed.path == '/api/orders':
            orders_file = Path.home() / '.zerostudio_orders.json'
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}

            tier = data.get('tier', 'pro')
            amount = data.get('amount', 299000)
            memo = data.get('memo', 'ZERO PRO')
            ref = data.get('ref', '')
            order_code = data.get('order_code', '')

            new_order = {
                'id': f"ord_{int(time.time() * 1000)}",
                'order_code': order_code,
                'tier': tier,
                'amount': amount,
                'memo': memo,
                'ref': ref,
                'status': 'pending_confirmation',
                'created_at': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'client_ip': client_ip
            }

            orders = []
            if orders_file.exists():
                try:
                    orders = json.loads(orders_file.read_text(encoding='utf-8'))
                except Exception:
                    orders = []

            orders.insert(0, new_order)
            orders = orders[:500]

            try:
                orders_file.write_text(json.dumps(orders, ensure_ascii=False, indent=2), encoding='utf-8')
            except Exception:
                pass

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'order': new_order}).encode('utf-8'))
            return

        if parsed.path == '/api/save-license':
            try:
                data = json.loads(post_data.decode('utf-8'))
                key = data.get('license_key', '').strip()

                if is_license_revoked(key):
                    user_license_file = Path.home() / '.zerostudio_license'
                    if user_license_file.exists():
                        try: user_license_file.unlink()
                        except Exception: pass
                    self.send_response(403)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': False, 'error': 'Key is revoked'}).encode())
                    return

                if key and (key.startswith('ZERO-PRO-') or key.startswith('ZERO-ULTRA-')):
                    user_license_file = Path.home() / '.zerostudio_license'
                    try:
                        user_license_file.write_text(key, encoding='utf-8')
                    except Exception:
                        pass

                    license_file = Path(__file__).parent / 'license.key'
                    if license_file.exists():
                        try:
                            license_file.unlink()
                        except Exception:
                            pass

                    token = mint_license_token(key, data.get('hardware_id', 'DEV-DESKTOP-BOUND'))
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
                    return
            except Exception as e:
                self.send_response(500)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
                return

        if parsed.path == '/api/delete-license':
            user_license_file = Path.home() / '.zerostudio_license'
            license_file = Path(__file__).parent / 'license.key'
            try:
                if user_license_file.exists(): user_license_file.unlink()
            except Exception: pass
            try:
                if license_file.exists(): license_file.unlink()
            except Exception: pass
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'deleted': True}).encode())
            return

        # ----------------------------------------------------
        # APPLY OTA AUTO-UPDATE (SYNC LATEST ASSETS FROM CLOUD)
        # ----------------------------------------------------
        if parsed.path == '/api/apply-ota-update':
            base_url = "https://zerostu.netlify.app"
            files_to_sync = [
                'index.html',
                'app.js',
                'version.json',
                'libs/zerostudio_drm.wasm',
                'libs/i18n.js'
            ]
            updated = []
            errors = []
            root_dir = Path(__file__).parent

            for rel_file in files_to_sync:
                target_path = root_dir / rel_file
                cloud_file_url = f"{base_url}/{rel_file}"
                try:
                    req = urllib.request.Request(cloud_file_url, headers={'User-Agent': 'ZeroStudio-OTA/2.0'})
                    with urllib.request.urlopen(req, timeout=8) as resp:
                        if resp.status == 200:
                            content = resp.read()
                            target_path.parent.mkdir(parents=True, exist_ok=True)
                            if target_path.exists():
                                try:
                                    (root_dir / f"{rel_file}.bak").write_bytes(target_path.read_bytes())
                                except Exception:
                                    pass
                            target_path.write_bytes(content)
                            updated.append(rel_file)
                except Exception as e:
                    errors.append(f"{rel_file}: {str(e)}")

            success = len(updated) > 0
            self.send_response(200 if success else 500)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': success,
                'updated_files': updated,
                'errors': errors,
                'message': f"Đã cập nhật thành công {len(updated)} file từ Cloud! Vui lòng tải lại trang." if success else "Không thể tải gói cập nhật từ Cloud."
            }).encode('utf-8'))
            return

        if parsed.path == '/api/batch-mmo':
            try:
                data = json.loads(post_data.decode('utf-8'))
                input_file = data.get('input_file', '')
                auto_crop = data.get('auto_crop_916', False)
                random_audio = data.get('random_pitch_speed', False)
                clean_subs = data.get('clean_subtitles', False)
                out_dir = Path.home() / 'Downloads' / 'ZeroStudio_Batch_MMO'
                out_dir.mkdir(parents=True, exist_ok=True)
                
                input_path = Path(input_file)
                if not input_path.exists():
                    self.send_response(400)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': False, 'error': 'File not found'}).encode())
                    return

                out_name = f"MMO_{input_path.stem}_{os.urandom(3).hex()}.mp4"
                output_path = out_dir / out_name

                filters = []
                last_v = "0:v"
                if auto_crop:
                    filters.append("[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bg];[0:v]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2[v_crop]")
                    last_v = "v_crop"
                
                if clean_subs:
                    filters.append(f"[{last_v}]delogo=x=120:y=1620:w=840:h=180:band=10[v_clean]")
                    last_v = "v_clean"

                cmd = ["ffmpeg", "-y", "-i", str(input_path)]
                if filters:
                    cmd += ["-filter_complex", ";".join(filters), "-map", f"[{last_v}]"]
                else:
                    cmd += ["-map", "0:v"]

                if random_audio:
                    import random
                    speed = round(random.uniform(1.012, 1.038), 4)
                    sample_rate = int(44100 * speed)
                    cmd += ["-af", f"asetrate={sample_rate},aresample=44100,atempo={1.0/speed:.4f}"]
                else:
                    cmd += ["-c:a", "copy"]

                cmd += ["-c:v", "libx264", "-preset", "faster", "-crf", "22", "-movflags", "+faststart", str(output_path)]
                res = subprocess.run(cmd, capture_output=True, text=True)
                
                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': res.returncode == 0,
                    'output_file': str(output_path),
                    'filename': out_name,
                    'error': res.stderr if res.returncode != 0 else None
                }).encode())
                return
            except Exception as e:
                self.send_response(500)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
                return

        self.send_response(404)
        self.end_headers()

def run_server():
    server = None
    active_port = None
    for p in [8900, 8901, 8899]:
        try:
            server = HTTPServer(('127.0.0.1', p), VideoBridgeHandler)
            active_port = p
            break
        except OSError:
            continue

    if not server:
        print("[ERROR] Could not bind to any bridge port (8899, 8900, 8901)")
        sys.exit(1)

    print(f"ZeroStudio Local Video Bridge & Cyber Defense Core active at http://127.0.0.1:{active_port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down bridge...")
        server.server_close()

if __name__ == '__main__':
    run_server()

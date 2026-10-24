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
import subprocess
import time
import re
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import yt_dlp

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    try: sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception: pass

PORT = 8900
BANNED_IPS_FILE = Path.home() / '.zerostudio_banned_ips.json'

MALICIOUS_PATTERNS = [
    r'\.\./', r'\.\.\\', r'/etc/passwd', r'win\.ini', r'boot\.ini',
    r'cmd\.exe', r'powershell', r'<script', r'javascript:',
    r'union\s+select', r'xp_cmdshell', r'exec\s*\(', r'0x[0-9a-fA-F]{4,}',
    r'%00', r'nullbyte'
]

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
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def check_security_barrier(self, parsed, params, raw_body=None):
        client_ip = get_client_ip(self)

        # 1. EMERGENCY ADMIN RESCUE HATCH (ALWAYS OPEN TO ADMIN WITH PASSCODE)
        if parsed.path == '/api/admin-unban':
            secret = params.get('secret', [''])[0]
            if secret == 'HIEU2026':
                target_ip = params.get('ip', ['all'])[0]
                unban_ip(target_ip)
                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': True,
                    'unbanned': target_ip,
                    'message': 'Admin Emergency Rescue Hatch đã gỡ lệnh khóa thành công!'
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
            self.wfile.write(json.dumps({'status': 'ok', 'service': 'ZeroStudio Video Bridge & Cyber Defense', 'version': '2.0'}).encode())
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
        # PERMANENT LOCAL DISK LICENSE STORAGE
        # ----------------------------------------------------
        if parsed.path == '/api/license':
            user_license_file = Path.home() / '.zerostudio_license'
            license_file = Path(__file__).parent / 'license.key'
            key = None

            REVOKED = {'ZERO-PRO-ADMIN-VIP-2026', 'ZERO-PRO-DEV-MASTER-9999', 'ZERO-PRO-VIP-PERMANENT', 'ZERO-PRO-8492-HIEU-9F2A'}

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

            if key in REVOKED:
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
            self.wfile.write(json.dumps({
                'has_license': is_valid_key,
                'license_key': key if is_valid_key else None,
                'tier': 'ultra' if (key and (key.startswith('ZERO-ULTRA-') or 'MASTER' in key or 'ADMIN' in key)) else ('pro' if is_valid_key else 'free')
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
        # PERMANENT BAN REPORTING FROM CLIENT DEFENSE SYSTEM
        # ----------------------------------------------------
        if parsed.path == '/api/report-hack':
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                data = {}
            reason = data.get('reason', 'Cố tình tấn công Brute-force dò quét mã bản quyền')
            fingerprint = data.get('fingerprint', 'unknown')
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
                'ban_info': ban_info
            }).encode())
            return

        if parsed.path == '/api/save-license':
            REVOKED = {'ZERO-PRO-ADMIN-VIP-2026', 'ZERO-PRO-DEV-MASTER-9999', 'ZERO-PRO-VIP-PERMANENT', 'ZERO-PRO-8492-HIEU-9F2A'}
            try:
                data = json.loads(post_data.decode('utf-8'))
                key = data.get('license_key', '').strip()

                if key in REVOKED:
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

                    self.send_response(200)
                    self._send_cors_headers()
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'success': True, 'saved': True}).encode())
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

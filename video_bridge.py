"""
ZeroStudio - Local High-Speed Video Bridge
Runs a lightweight, zero-log, zero-storage local micro-bridge on 127.0.0.1:8899.
Uses yt-dlp to extract clean watermark-free video and audio streams for TikTok, Douyin, Reels, Shorts, etc.
"""
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import yt_dlp

PORT = 8899

class VideoBridgeHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/api/ping':
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'ok', 'service': 'ZeroStudio Video Bridge', 'version': '1.0'}).encode())
            return

        # ----------------------------------------------------
        # PERMANENT LOCAL DISK LICENSE STORAGE
        # ----------------------------------------------------
        if parsed.path == '/api/license':
            license_file = Path(__file__).parent / 'license.key'
            user_license_file = Path.home() / '.zerostudio_license'
            key = None

            if license_file.exists():
                try:
                    key = license_file.read_text(encoding='utf-8').strip()
                except Exception:
                    pass
            elif user_license_file.exists():
                try:
                    key = user_license_file.read_text(encoding='utf-8').strip()
                except Exception:
                    pass

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'has_license': bool(key and key.startswith('ZERO-PRO-')),
                'license_key': key if (key and key.startswith('ZERO-PRO-')) else None
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

                    # Audio format
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

        # ----------------------------------------------------
        # PRO API 1: TIKTOK / DOUYIN FULL CHANNEL SCRAPER
        # ----------------------------------------------------
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
                        v_url = entry.get('url') or entry.get('webpage_url') or (f"https://www.tiktok.com/@user/video/{v_id}" if "tiktok" in url else url)
                        v_thumb = entry.get('thumbnail') or (entry.get('thumbnails', [{}])[-1].get('url', '') if entry.get('thumbnails') else '')
                        v_dur = entry.get('duration') or 0
                        v_views = entry.get('view_count') or 0

                        videos.append({
                            'id': v_id,
                            'title': v_title,
                            'url': v_url,
                            'thumbnail': v_thumb,
                            'duration': v_dur,
                            'views': v_views
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

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path == '/api/save-license':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                key = data.get('license_key', '').strip()
                if key and key.startswith('ZERO-PRO-'):
                    license_file = Path(__file__).parent / 'license.key'
                    user_license_file = Path.home() / '.zerostudio_license'
                    license_file.write_text(key, encoding='utf-8')
                    try:
                        user_license_file.write_text(key, encoding='utf-8')
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

        self.send_response(404)
        self.end_headers()

def run_server():
    server = HTTPServer(('127.0.0.1', PORT), VideoBridgeHandler)
    print(f"ZeroStudio Local Video Bridge active at http://127.0.0.1:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down bridge...")
        server.server_close()

if __name__ == '__main__':
    run_server()

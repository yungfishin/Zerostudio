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

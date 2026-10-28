import http.server
import socketserver
import webbrowser
import os
import sys

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

PORT = 8950
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
        
    def end_headers(self):
        # Enable CORS and disable caching for instant updates
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            url = f"http://127.0.0.1:{PORT}/deepfake_shield_demo.html"
            print("\n=======================================================")
            print("  [+] ZEROTRUST DEEPFAKE SHIELD DEMO SERVER LAUNCHED")
            print("=======================================================")
            print(f"  [+] Dang phuc vu tai: {url}")
            print("  [+] Dang tu dong mo trinh duyet web...")
            print("  [+] Nhan Ctrl+C de dung server khi hoan tat.")
            print("=======================================================\n")
            
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        if "10048" in str(e): # Port already in use
            print(f"[!] Cong {PORT} dang mo san, mo trinh duyet thang...")
            webbrowser.open(f"http://127.0.0.1:{PORT}/deepfake_shield_demo.html")
        else:
            print(f"[!] Loi server: {e}")

if __name__ == '__main__':
    main()

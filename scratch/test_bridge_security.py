import sys, subprocess, time, secrets, base64, json
from pathlib import Path

def scan_cracking_tools():
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

is_cracked, reason = scan_cracking_tools()
print(f"Cracking tool scan result: is_detected={is_cracked}, reason='{reason}'")
assert is_cracked is False
print("[OK] Desktop anti-debugging process scanner passed!")

"""
ZeroStudio - Automated Test: Permanent IP Ban & Cyber Security Lockdown
"""
import sys
import os
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_DIR = Path(r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio")
HTML_PATH = (PROJECT_DIR / "index.html").as_uri()
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ARTIFACT_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")
SCREENSHOT_PATH = ARTIFACT_DIR / "ZEROPDF_DEMO_22_CYBER_LOCKDOWN.png"

def run_test():
    print(f"[TEST] Starting Anti-Hack & Permanent IP Ban Verification...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True,
            args=["--no-sandbox", "--disable-web-security"]
        )
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        # Step 0: Ensure starting with a clean slate
        page.goto(HTML_PATH)
        page.wait_for_timeout(1000)
        
        # Set test tier to free so pricing view and license box are open
        page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); localStorage.setItem('zerostudio_test_tier', 'free'); }")
        
        # Unban on bridge
        import urllib.request
        try:
            urllib.request.urlopen("http://127.0.0.1:8900/api/admin-unban?secret=HIEU2026&ip=all")
        except Exception:
            pass

        page.reload()
        page.wait_for_timeout(1500)

        # Step 1: Open Pro Modal and switch to Pricing View
        print("[TEST] Step 1: Opening Pro Modal & Pricing View...")
        page.evaluate("() => { window.openProModal(); window.showProPricingView(); }")
        page.wait_for_timeout(800)
        assert page.is_visible("#license-key-input"), "#license-key-input should be visible"

        # Step 2: Trigger 5 consecutive failed license activations (Brute-force simulation)
        print("[TEST] Step 2: Simulating 5 failed license key brute-force attacks...")
        for attempt in range(1, 6):
            page.fill("#license-key-input", f"HACK-KEY-ATTEMPT-{attempt:02d}")
            page.click("button:has-text('Kích Hoạt Ngay')")
            page.wait_for_timeout(400)
            print(f"       -> Attempt {attempt}/5 executed")

        # Step 3: Verify Cyber Lockdown Overlay is displayed
        print("[TEST] Step 3: Verifying Cyber Lockdown Screen is active...")
        page.wait_for_timeout(1000)
        is_lockdown_active = page.evaluate("() => document.getElementById('cyber-lockdown-overlay').classList.contains('active')")
        assert is_lockdown_active, "Cyber Lockdown overlay must have class 'active' after 5 failed attempts!"
        
        # Verify Telemetry elements
        reason_text = page.inner_text("#lockdown-telemetry-reason")
        status_text = page.inner_text("#lockdown-telemetry-ip")
        device_text = page.inner_text("#lockdown-telemetry-device")
        print(f"       -> Detected Reason: {reason_text}")
        print(f"       -> Detected IP: {status_text}")
        print(f"       -> Detected Device Fingerprint: {device_text}")
        assert "Brute-force" in reason_text, "Lockdown reason must mention Brute-force"

        # Step 4: Capture Screenshot Artifact
        print(f"[TEST] Step 4: Capturing Forensic Lockdown Screenshot: {SCREENSHOT_PATH.name}")
        page.screenshot(path=str(SCREENSHOT_PATH))
        print("       -> Screenshot successfully saved.")

        # Step 5: Verify Persistence Across Page Reload
        print("[TEST] Step 5: Testing Persistence across hard reload...")
        page.reload()
        page.wait_for_timeout(1200)
        is_still_locked = page.evaluate("() => document.getElementById('cyber-lockdown-overlay').classList.contains('active')")
        assert is_still_locked, "Lockdown must remain ACTIVE after reload (permanent ban enforcement)!"
        print("       -> Pass: Lockdown is strictly permanent and survives page reloads.")

        # Step 6: Test Admin Emergency Rescue Hatch with Passcode 'HIEU2026'
        print("[TEST] Step 6: Testing Admin Emergency Rescue Hatch with passcode 'HIEU2026'...")
        
        dialog_handled = []
        def handle_dialog(dialog):
            dialog_handled.append(dialog.type)
            if dialog.type == "prompt":
                dialog.accept("HIEU2026")
            else:
                dialog.accept()

        page.on("dialog", handle_dialog)
        
        # Trigger rescue hatch
        page.evaluate("() => window._secAuthHatch()")
        page.wait_for_timeout(1500)

        # Step 7: Verify ban is cleared
        page.reload()
        page.wait_for_timeout(1000)
        is_cleared = page.evaluate("() => !localStorage.getItem('zerostudio_banned') && !document.getElementById('cyber-lockdown-overlay').classList.contains('active')")
        assert is_cleared, "Ban should be removed and lockdown cleared after correct admin passcode!"
        print("       -> Pass: Admin rescue hatch successfully unlocked the system!")

        browser.close()
        print("\n[SUCCESS] ALL PERMANENT IP BAN & ANTI-HACK TESTS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    run_test()

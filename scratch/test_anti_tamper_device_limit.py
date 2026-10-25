"""
ZeroStudio - Automated Test: Anti-DevTools & Device Limit 3-Strike Ban
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
SCREENSHOT_STRIKE_PATH = ARTIFACT_DIR / "ZEROPDF_DEMO_23_DEVICE_LIMIT_WARNING.png"
SCREENSHOT_DEVTOOLS_PATH = ARTIFACT_DIR / "ZEROPDF_DEMO_24_ANTI_DEVTOOLS_BLOCKED.png"

def run_test():
    print("[TEST] Starting Anti-DevTools & Device Limit 3-Strike Verification...")
    
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
        page.evaluate("() => { localStorage.clear(); sessionStorage.clear(); localStorage.setItem('zerostudio_test_tier', 'free'); }")
        
        # Unban on bridge
        import urllib.request
        try:
            urllib.request.urlopen("http://127.0.0.1:8900/api/admin-unban?secret=HIEU2026&ip=all")
        except Exception:
            pass

        page.reload()
        page.wait_for_timeout(1500)

        # -------------------------------------------------------------
        # TEST 1: IMMUTABILITY LOCK (ANTI-CONSOLE CRACK)
        # -------------------------------------------------------------
        print("\n[TEST 1] Testing Immutability Lock on window.isProActive...")
        # Verify in Free mode it is false
        is_pro = page.evaluate("() => window.isProActive()")
        assert is_pro == False, "Initial isProActive must be false in free mode"

        # Attempt to crack by overriding function in Console
        crack_result = page.evaluate("""() => {
            try {
                window.isProActive = () => true;
            } catch (e) {
                return 'THREW_ERROR: ' + e.message;
            }
            return window.isProActive();
        }""")
        print(f"       -> Crack attempt result: {crack_result}")
        # Verify that despite assignment attempt, isProActive() is STILL FALSE!
        is_pro_after_crack = page.evaluate("() => window.isProActive()")
        assert is_pro_after_crack == False, "isProActive must remain false despite console override attempt!"
        print("       -> Pass: window.isProActive is immutable and cannot be cracked in console!")

        # -------------------------------------------------------------
        # TEST 2: ANTI-F12 & ANTI-INSPECT SHORTCUTS
        # -------------------------------------------------------------
        print("\n[TEST 2] Testing Anti-F12 and Context Menu Interception...")
        # Trigger F12 keydown
        page.keyboard.press("F12")
        page.wait_for_timeout(600)
        
        # Verify toast appeared
        toast_text = page.evaluate("() => { const t = document.querySelector('.toast-pill'); return t ? t.textContent : ''; }")
        print(f"       -> F12 Toast: {toast_text}")
        assert "F12" in toast_text, "F12 warning toast should be shown"

        # Trigger Context Menu (Right Click)
        page.mouse.click(200, 200, button="right")
        page.wait_for_timeout(600)
        context_toast = page.evaluate("() => { const t = document.querySelectorAll('.toast-pill'); return t.length ? t[t.length - 1].textContent : ''; }")
        print(f"       -> Right-click Toast: {context_toast}")
        assert "Chuột phải" in context_toast, "Right click warning toast should be shown"

        page.screenshot(path=str(SCREENSHOT_DEVTOOLS_PATH))
        print(f"       -> Screenshot saved: {SCREENSHOT_DEVTOOLS_PATH.name}")

        # -------------------------------------------------------------
        # TEST 3: DEVICE LIMIT & 3-STRIKE WARNING ENFORCEMENT
        # -------------------------------------------------------------
        print("\n[TEST 3] Testing Device Limit & 3-Strike Warning on Activation...")
        test_pro_key = "ZERO-PRO-FAMILY-SHARE-2026"
        
        # Open Pro Modal & Pricing View
        page.evaluate("() => { window.openProModal(); window.showProPricingView(); }")
        page.wait_for_timeout(600)

        # Pre-bind key to another device via Bridge API
        bridge_req = urllib.request.Request(
            "http://127.0.0.1:8900/api/verify-device",
            data=json.dumps({"license_key": test_pro_key, "device_id": "DEV-SEC-ORIGINAL-PC"}).encode(),
            headers={"Content-Type": "application/json"}
        )
        urllib.request.urlopen(bridge_req)
        print("       -> Pre-bound key to DEV-SEC-ORIGINAL-PC (Device limit 1/1 reached)")

        # Attempt to activate on current device (Strike 1)
        page.fill("#license-key-input", test_pro_key)
        page.click("button:has-text('Kích Hoạt Ngay')")
        page.wait_for_timeout(800)
        
        strike1_toast = page.evaluate("() => { const t = document.querySelectorAll('.toast-pill'); return t.length ? t[t.length - 1].textContent : ''; }")
        print(f"       -> Attempt 1 Toast: {strike1_toast}")
        assert "1/3" in strike1_toast, "Strike 1 warning toast should say (1/3)"

        page.screenshot(path=str(SCREENSHOT_STRIKE_PATH))
        print(f"       -> Screenshot saved: {SCREENSHOT_STRIKE_PATH.name}")

        # Attempt to activate again (Strike 2)
        page.click("button:has-text('Kích Hoạt Ngay')")
        page.wait_for_timeout(800)
        strike2_toast = page.evaluate("() => { const t = document.querySelectorAll('.toast-pill'); return t.length ? t[t.length - 1].textContent : ''; }")
        print(f"       -> Attempt 2 Toast: {strike2_toast}")
        assert "2/3" in strike2_toast, "Strike 2 warning toast should say (2/3)"

        # Attempt to activate 3rd time (Strike 3 -> Permanent BAN!)
        print("       -> Triggering Attempt 3 (Strike 3: Permanent Ban)...")
        page.click("button:has-text('Kích Hoạt Ngay')")
        page.wait_for_timeout(1200)

        # Verify Cyber Lockdown Screen is active
        is_locked = page.evaluate("() => document.getElementById('cyber-lockdown-overlay').classList.contains('active')")
        assert is_locked, "Device must be PERMANENTLY BANNED after 3 device limit strikes!"
        
        reason = page.inner_text("#lockdown-telemetry-reason")
        print(f"       -> Ban Reason on Screen: {reason}")
        assert "vượt quá số lượng thiết bị" in reason or "vượt số" in reason or "thiết bị" in reason, "Ban reason should indicate device limit violation"

        # Cleanup via Admin Rescue Hatch
        print("\n[CLEANUP] Unbanning system for admin...")
        urllib.request.urlopen("http://127.0.0.1:8900/api/admin-unban?secret=HIEU2026&ip=all")
        print("       -> System unbanned cleanly.")

        browser.close()
        print("\n[SUCCESS] ALL ANTI-DEVTOOLS & DEVICE LIMIT TESTS PASSED 100%!")

if __name__ == "__main__":
    run_test()

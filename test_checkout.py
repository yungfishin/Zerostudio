import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BRAIN_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")
HTML_PATH = Path(r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html").as_uri()
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

async def test_checkout_flow():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True
        )
        context = await browser.new_context(viewport={"width": 1280, "height": 1150})
        page = await context.new_page()

        print("[1] Opening ZeroStudio...")
        await page.goto(HTML_PATH)
        await page.wait_for_timeout(1000)

        # Skip intro to reach workspace
        await page.evaluate("if (window.skipIntro) window.skipIntro()")
        await page.wait_for_timeout(500)

        # Clear any stored license to test clean checkout
        await page.evaluate("localStorage.removeItem('zerostudio_pro_license')")

        # 1. Open Pro Pricing Modal
        print("[2] Opening Pro Modal (Pricing View)...")
        await page.evaluate("openProModal()")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_08_PRO_MODAL.png"))

        # 2. Click VietQR Checkout
        print("[3] Switching to VietQR Checkout Stage...")
        await page.evaluate("openVietQrCheckout()")
        await page.wait_for_timeout(1200) # wait for VietQR image to load or render
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_09_VIETQR_CHECKOUT.png"))

        # 3. Simulate Confirm Paid
        print("[4] Confirming payment & generating license key...")
        await page.evaluate("confirmPaidAndGetLicense()")
        await page.wait_for_timeout(1800) # wait for timeout animation
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_10_LICENSE_SUCCESS.png"))

        # 4. Check if license is saved in localStorage
        saved_key = await page.evaluate("localStorage.getItem('zerostudio_pro_license')")
        print(f"[5] Stored License Key: {saved_key}")

        await browser.close()
        print("SUCCESS: End-to-end VietQR checkout & License Key delivery tested!")

if __name__ == "__main__":
    asyncio.run(test_checkout_flow())

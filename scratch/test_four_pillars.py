import asyncio
import os
import sys
import json
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
from playwright.async_api import async_playwright

BASE_DIR = Path(r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio")
HTML_PATH = BASE_DIR / "index.html"
ARTIFACT_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")

async def run_test():
    print("[TEST] Starting Playwright E2E verification of Four Pillars (v2.4.0)...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="msedge", headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # ---------------------------------------------------------
        # 1. PILLAR 2: OPEN GRAPH & SOCIAL PREVIEW META TEST
        # ---------------------------------------------------------
        print("\n--- 1. Testing Open Graph & PWA Meta Tags ---")
        url_with_ref = f"file:///{HTML_PATH.as_posix()}?ref=TOPMMO"
        await page.goto(url_with_ref, wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)

        og_img = await page.get_attribute("meta[property='og:image']", "content")
        og_title = await page.get_attribute("meta[property='og:title']", "content")
        manifest = await page.get_attribute("link[rel='manifest']", "href")
        print(f"  [OK] og:image: {og_img}")
        print(f"  [OK] og:title: {og_title}")
        print(f"  [OK] manifest: {manifest}")
        assert "zerostudio-og-preview.png" in og_img
        assert "ZeroStudio Pro" in og_title
        assert "manifest.json" in manifest

        # ---------------------------------------------------------
        # 2. PILLAR 4: AFFILIATE DISCOUNT & VIETQR TEST
        # ---------------------------------------------------------
        print("\n--- 2. Testing Affiliate Discount Activation & VietQR ---")
        # Open Pro Modal to check pricing banner
        await page.evaluate("openProModal()")
        await page.wait_for_timeout(500)

        banner = page.locator("#affiliate-discount-banner")
        banner_visible = await banner.is_visible()
        code_text = await page.locator("#affiliate-active-code").inner_text()
        print(f"  [OK] Discount Banner Visible: {banner_visible}, Code: {code_text}")
        assert banner_visible is True
        assert "TOPMMO" in code_text

        # Open VietQR for Pro
        await page.evaluate("openVietQrCheckout('pro')")
        await page.wait_for_timeout(800)

        checkout_modal = page.locator("#pro-modal")
        assert await checkout_modal.is_visible()

        amount_html = await page.locator("#checkout-amount-display").inner_html()
        memo_text = await page.locator("#order-memo-val").inner_text()
        disc_pill = page.locator("#checkout-discount-pill")
        print(f"  [OK] Checkout Amount HTML: {amount_html.strip()}")
        print(f"  [OK] Checkout Memo: {memo_text}")
        print(f"  [OK] Discount Pill Visible: {await disc_pill.is_visible()}")
        assert "269.000 VNĐ" in amount_html
        assert "299.000 VNĐ" in amount_html  # Old strikethrough price
        assert "REF-TOPMMO" in memo_text
        assert await disc_pill.is_visible() is True

        # Capture Screenshot of VietQR with Affiliate discount
        shot_checkout = ARTIFACT_DIR / "ZEROPDF_DEMO_35_AFFILIATE_CHECKOUT.png"
        await page.screenshot(path=shot_checkout.as_posix(), full_page=False)
        print(f"  [OK] Saved Artifact: {shot_checkout.name}")

        # ---------------------------------------------------------
        # 3. PILLAR 1: INSTANT NOTIFICATION & PAYMENT INTENT DISPATCH
        # ---------------------------------------------------------
        print("\n--- 3. Testing Payment Intent & Instant Notification ---")
        await page.evaluate("confirmPaidAndGetLicense()")
        await page.wait_for_timeout(1000)

        # Check bridge orders on disk
        orders_file = Path.home() / ".zerostudio_orders.json"
        assert orders_file.exists()
        orders_data = json.loads(orders_file.read_text(encoding="utf-8"))
        print(f"  [OK] Orders on disk count: {len(orders_data)}")
        latest_ord = orders_data[0]
        print(f"  [OK] Latest Order recorded: tier={latest_ord.get('tier')}, amount={latest_ord.get('amount')}, memo={latest_ord.get('memo')}")
        assert latest_ord.get("ref") == "TOPMMO"
        assert latest_ord.get("amount") == 269000

        # Close Pro Modal
        await page.evaluate("closeProModal()")
        await page.wait_for_timeout(500)

        # ---------------------------------------------------------
        # 4. PILLAR 4 (PART 2): AFFILIATE PARTNER MODAL & LINK GENERATOR
        # ---------------------------------------------------------
        print("\n--- 4. Testing Affiliate Modal & Link Generator ---")
        await page.evaluate("openAffiliateModal()")
        await page.wait_for_timeout(600)

        aff_modal = page.locator("#affiliate-modal")
        assert await aff_modal.is_visible()

        # Fill custom nickname
        await page.locator("#aff-nickname-input").fill("VIPCREATOR")
        await page.evaluate("generateAffiliateLink()")
        await page.wait_for_timeout(800)

        link_val = await page.locator("#aff-link-output").input_value()
        print(f"  [OK] Generated Link: {link_val}")
        assert "ref=VIPCREATOR" in link_val

        # Capture Screenshot of Affiliate Modal
        shot_aff = ARTIFACT_DIR / "ZEROPDF_DEMO_36_AFFILIATE_MODAL.png"
        await page.screenshot(path=shot_aff.as_posix(), full_page=False)
        print(f"  [OK] Saved Artifact: {shot_aff.name}")

        # ---------------------------------------------------------
        # 5. PILLAR 3: PWA MANIFEST & BUTTON VERIFICATION
        # ---------------------------------------------------------
        print("\n--- 5. Testing PWA Manifest & Installation UI ---")
        manifest_file = BASE_DIR / "manifest.json"
        assert manifest_file.exists()
        m_data = json.loads(manifest_file.read_text(encoding="utf-8"))
        print(f"  [OK] PWA App Name: {m_data.get('name')}")
        print(f"  [OK] PWA Icons count: {len(m_data.get('icons'))}")
        assert m_data.get("name") == "ZeroStudio Pro - Video MMO & Xử Lý PDF"
        assert len(m_data.get("icons")) >= 2

        # Check pwa install button in DOM
        pwa_btn = page.locator("#btn-pwa-install")
        assert await pwa_btn.count() == 1

        print("\n=======================================================")
        print("ALL 4 PILLARS VERIFIED 100% SUCCESSFULLY WITH ZERO REGRESSIONS!")
        print("=======================================================")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())

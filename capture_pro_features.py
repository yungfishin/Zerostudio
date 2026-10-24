import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BRAIN_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")
HTML_PATH = Path(r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html").as_uri()
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

async def capture_pro():
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

        # Switch to tab-video
        print("[2] Switching to Video Studio tab...")
        await page.evaluate("document.querySelector('.bento-nav-btn[data-tab=\"video\"]').click()")
        await page.wait_for_timeout(600)

        # 1. Test Channel Scraper
        print("[3] Testing Channel Scraper Sub-mode...")
        await page.evaluate("switchVideoSubMode('channel')")
        await page.wait_for_timeout(400)

        # Input URL and trigger scrape
        await page.evaluate("""() => {
            document.getElementById('channel-url-input').value = 'https://www.tiktok.com/@vtv24news';
            startScrapeChannel();
        }""")
        await page.wait_for_timeout(1500)

        # Take screenshot of Channel Scraper results
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_11_CHANNEL_SCRAPER.png"))
        print("[4] Captured ZEROPDF_DEMO_11_CHANNEL_SCRAPER.png")

        # 2. Test Anti-Ban & MD5 Modder
        print("[5] Testing Anti-Ban & MD5 Modder Sub-mode...")
        await page.evaluate("switchVideoSubMode('antiban')")
        await page.wait_for_timeout(400)

        # Simulate nạp files and processing
        await page.evaluate("""async () => {
            // Mock 2 files in state
            state.antibanFiles = [
                new File(["FAKE_VIDEO_CONTENT_BYTE_DATA_STREAM_PART_1"], "review_cong_nghe_ep01.mp4", { type: "video/mp4" }),
                new File(["FAKE_VIDEO_CONTENT_BYTE_DATA_STREAM_PART_2"], "unboxing_gadget_trend.mp4", { type: "video/mp4" })
            ];
            document.getElementById('antiban-cockpit-workspace').style.display = 'grid';
            renderAntibanStreamPending();
            await processAntibanBatch();
        }""")
        await page.wait_for_timeout(1500)

        # Take screenshot of Anti-Ban Modder telemetry
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_12_ANTIBAN_MODDER.png"))
        print("[6] Captured ZEROPDF_DEMO_12_ANTIBAN_MODDER.png")

        await browser.close()
        print("SUCCESS: Both killer Pro features captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture_pro())

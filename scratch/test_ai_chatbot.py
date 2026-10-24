import asyncio
import os
import sys
from pathlib import Path

# Force UTF-8 output on Windows console
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from playwright.async_api import async_playwright

ARTIFACTS_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")
HTML_PATH = Path(r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html").resolve()

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

async def main():
    print(f"=== TESTING ZEROAI SPECIALIST CHATBOT ===")
    print(f"HTML File: {HTML_PATH}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME_PATH, headless=True)
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()

        # Listen to console logs
        page.on("console", lambda msg: print(f"  [BROWSER CONSOLE] {msg.type}: {msg.text}"))

        # Navigate to ZeroStudio
        await page.goto(f"file:///{HTML_PATH.as_posix()}", wait_until="domcontentloaded")
        await page.wait_for_timeout(1000)

        # 1. Verify Floating Trigger Button
        trigger = page.locator("#zeroai-widget-trigger")
        assert await trigger.is_visible(), "ZeroAI trigger widget must be visible!"
        print(" [PASS] Step 1: ZeroAI Floating Widget is visible.")

        # 2. Click Trigger to Open Chat Window
        await trigger.click()
        await page.wait_for_timeout(500)
        chat_win = page.locator("#zeroai-chat-window")
        assert await chat_win.is_visible(), "ZeroAI Chat window should be open!"
        print(" [PASS] Step 2: ZeroAI Chat Drawer opened smoothly.")

        # 3. Verify Model Tag and Initial Welcome Message
        mode_tag = page.locator("#zeroai-active-mode-tag")
        mode_text = await mode_tag.inner_text()
        print(f"  -> Active Engine Tag: {mode_text}")
        assert "OFFLINE" in mode_text.upper(), "Default mode should be Offline 0đ"

        welcome_bubble = page.locator(".zeroai-msg-row.bot .zeroai-bubble").first
        welcome_text = await welcome_bubble.inner_text()
        assert "ZeroAI Specialist" in welcome_text, "Welcome message should introduce ZeroAI Specialist"
        print(" [PASS] Step 3: Welcome message and Offline 0đ mode verified.")

        # 4. Click Quick Prompt: Lách bản quyền MMO
        chip_mmo = page.locator(".zeroai-chip", has_text="Lách bản quyền MMO")
        await chip_mmo.click()
        print("  -> Clicked Quick Chip: 'Lách bản quyền MMO'")
        await page.wait_for_timeout(1000)

        # Verify bot reply
        mmo_reply = page.locator(".zeroai-msg-row.bot .zeroai-bubble", has_text="CÔNG THỨC LÁCH BẢN QUYỀN")
        assert await mmo_reply.count() > 0, "Bot should reply with MMO Anti-Ban Formula"
        print(" [PASS] Step 4: Quick prompt answered with 4-step MMO Anti-Ban formula.")

        # 5. Test Interactive Action Button inside Bot Message
        action_btn_video = page.locator(".zeroai-action-btn", has_text="Mở Tab Auto-Crop & Lách MMO").last
        assert await action_btn_video.is_visible(), "Action button for Auto-Crop tab must be rendered"
        await action_btn_video.click()
        await page.wait_for_timeout(600)
        
        # Check active tab in main UI
        active_nav = page.locator(".bento-nav-btn.active")
        active_tab_name = await active_nav.get_attribute("data-tab")
        print(f"  -> Current Active Tab after bot action: {active_tab_name}")
        assert active_tab_name == "video", "Tab should switch to 'video'!"
        print(" [PASS] Step 5: 1-Click Interactive Action Button switched tab to Video MMO.")

        # 6. Type Custom Question: "bảng giá gói ultra và quyền lợi"
        input_field = page.locator("#zeroai-chat-input")
        await input_field.fill("bảng giá gói ultra và quyền lợi")
        send_btn = page.locator("#zeroai-send-btn")
        await send_btn.click()
        print("  -> Sent custom query: 'bảng giá gói ultra và quyền lợi'")
        await page.wait_for_timeout(1000)

        pricing_reply = page.locator(".zeroai-msg-row.bot .zeroai-bubble", has_text="GÓI ULTRA MMO MASTER (699.000đ")
        assert await pricing_reply.count() > 0, "Bot should reply with Ultra package pricing & 2-device privileges"
        print(" [PASS] Step 6: Custom pricing query answered with Ultra vs Pro details.")

        # 7. Test Bridge Connection Ping Action
        await input_field.fill("cách sửa lỗi video bridge")
        await send_btn.click()
        await page.wait_for_timeout(1000)

        bridge_ping_btn = page.locator(".zeroai-action-btn", has_text="Kiểm Tra Kết Nối Video Bridge Ngay").last
        assert await bridge_ping_btn.is_visible(), "Bridge ping action button should exist"
        await bridge_ping_btn.click()
        print("  -> Clicked 'Kiểm Tra Kết Nối Video Bridge Ngay'")
        await page.wait_for_timeout(1500)

        bridge_result = page.locator(".zeroai-msg-row.bot .zeroai-bubble", has_text="Video Bridge HOẠT ĐỘNG HOÀN HẢO")
        assert await bridge_result.count() > 0, "Live bridge ping should report 200 OK status from Python Bridge"
        print(" [PASS] Step 7: Live Video Bridge ping executed and verified successfully!")

        # 8. Test Settings Modal (Gear icon)
        settings_btn = page.locator("button[title*='Cài đặt AI']")
        await settings_btn.click()
        await page.wait_for_timeout(400)
        settings_modal = page.locator("#zeroai-api-modal")
        assert await settings_modal.is_visible(), "Settings modal should open"
        print(" [PASS] Step 8: Gemini API Key configuration modal opened and inspected.")
        
        # Close settings modal
        close_settings = page.locator("#zeroai-api-modal .zeroai-btn-icon", has_text="✕")
        await close_settings.click()
        await page.wait_for_timeout(300)

        # 9. Capture Screenshot Artifact
        screenshot_path = ARTIFACTS_DIR / "ZEROPDF_DEMO_25_AI_CHATBOT.png"
        await page.screenshot(path=str(screenshot_path), full_page=False)
        print(f" [PASS] Step 9: Screenshot captured at: {screenshot_path}")

        await browser.close()
        print("=== ALL ZEROAI SPECIALIST CHATBOT TESTS PASSED! ===")

if __name__ == "__main__":
    asyncio.run(main())

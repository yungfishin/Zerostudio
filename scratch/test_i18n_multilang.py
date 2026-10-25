import sys
import time
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33"
SCREENSHOT_PATH = os.path.join(ARTIFACT_DIR, "ZEROPDF_DEMO_32_MULTILANG_SWITCHER.png")
HTML_PATH = (Path(__file__).parent.parent / "index.html").resolve()

def run():
    print("=== STARTING ZEROSTUDIO MULTI-LANGUAGE (i18n) PLAYWRIGHT AUDIT ===", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 950})
        page = context.new_page()

        # 1. Load ZeroStudio
        file_url = f"file:///{HTML_PATH.as_posix()}"
        print(f"[1] Navigating to {file_url}...", flush=True)
        page.goto(file_url, wait_until="domcontentloaded")
        page.evaluate("localStorage.removeItem('zerostudio_lang');")
        page.reload()
        page.wait_for_load_state("domcontentloaded")
        time.sleep(1)

        # 2. Check default language (vi)
        flag = page.locator("#current-lang-flag").inner_text()
        code = page.locator("#current-lang-code").inner_text()
        hero_title = page.locator("[data-i18n='hero_title']").inner_text()
        print(f"[2] Default Language: Flag={flag}, Code={code}, Hero='{hero_title}'", flush=True)
        assert "VI" in code, f"Expected VI but got {code}"

        # 3. Switch to English (en)
        print("[3] Switching to English (en)...", flush=True)
        page.click(".lang-toggle-btn")
        time.sleep(0.3)
        page.click(".lang-item[data-lang='en']")
        time.sleep(0.5)

        en_code = page.locator("#current-lang-code").inner_text()
        en_hero = page.locator("[data-i18n='hero_title']").inner_text()
        en_tab1 = page.locator("[data-i18n='tab_merge']").inner_text()
        print(f"    EN Code: {en_code}, Hero: '{en_hero}', Tab1: '{en_tab1}'", flush=True)
        assert "EN" in en_code, f"Expected EN but got {en_code}"
        assert "Ultimate" in en_hero, f"Expected 'Ultimate' in hero title but got {en_hero}"
        assert "Merge PDF" in en_tab1, f"Expected 'Merge PDF' but got {en_tab1}"

        # 4. Check ZeroAI English Welcome
        print("[4] Checking ZeroAI Chatbot in English...", flush=True)
        page.click("#zeroai-widget-trigger")
        time.sleep(0.5)
        bot_msg = page.locator("#zeroai-msg-list .zeroai-msg-row.bot .zeroai-bubble").first.inner_text()
        print(f"    ZeroAI English Welcome excerpt: {bot_msg[:80]}...", flush=True)
        assert "ZeroAI Specialist" in bot_msg or "Hello" in bot_msg, "Expected English welcome message"

        # 5. Switch to Chinese (zh)
        print("[5] Switching to Chinese (zh)...", flush=True)
        page.click(".lang-toggle-btn")
        time.sleep(0.3)
        page.click(".lang-item[data-lang='zh']")
        time.sleep(0.5)

        zh_code = page.locator("#current-lang-code").inner_text()
        zh_hero = page.locator("[data-i18n='hero_title']").inner_text()
        zh_tab1 = page.locator("[data-i18n='tab_merge']").inner_text()
        zh_bot = page.locator("#zeroai-msg-list .zeroai-msg-row.bot .zeroai-bubble").first.inner_text()
        print(f"    ZH Code: {zh_code}, Hero: '{zh_hero}', Tab1: '{zh_tab1}'", flush=True)
        print(f"    ZH ZeroAI excerpt: {zh_bot[:60]}...", flush=True)
        assert "ZH" in zh_code, f"Expected ZH but got {zh_code}"
        assert "超能" in zh_hero, f"Expected Chinese hero title but got {zh_hero}"
        assert "合并PDF" in zh_tab1, f"Expected '合并PDF' but got {zh_tab1}"

        # 6. Switch to Japanese (ja)
        print("[6] Switching to Japanese (ja)...", flush=True)
        page.click(".lang-toggle-btn")
        time.sleep(0.3)
        page.click(".lang-item[data-lang='ja']")
        time.sleep(0.5)

        ja_code = page.locator("#current-lang-code").inner_text()
        ja_hero = page.locator("[data-i18n='hero_title']").inner_text()
        ja_tab1 = page.locator("[data-i18n='tab_merge']").inner_text()
        ja_bot = page.locator("#zeroai-msg-list .zeroai-msg-row.bot .zeroai-bubble").first.inner_text()
        print(f"    JA Code: {ja_code}, Hero: '{ja_hero}', Tab1: '{ja_tab1}'", flush=True)
        print(f"    JA ZeroAI excerpt: {ja_bot[:60]}...", flush=True)
        assert "JA" in ja_code, f"Expected JA but got {ja_code}"
        assert "次世代" in ja_hero, f"Expected Japanese hero title but got {ja_hero}"
        assert "PDF結合" in ja_tab1, f"Expected 'PDF結合' but got {ja_tab1}"

        # 7. Check Persistence after reload
        print("[7] Testing localStorage persistence upon page reload...", flush=True)
        stored_lang = page.evaluate("localStorage.getItem('zerostudio_lang')")
        print(f"    localStorage['zerostudio_lang'] = {stored_lang}", flush=True)
        assert stored_lang == "ja", f"Expected 'ja' in localStorage but got {stored_lang}"

        page.reload()
        page.wait_for_load_state("domcontentloaded")
        time.sleep(1)
        reloaded_code = page.locator("#current-lang-code").inner_text()
        print(f"    Reloaded Code: {reloaded_code}", flush=True)
        assert "JA" in reloaded_code, f"Expected JA to persist after reload but got {reloaded_code}"

        # 8. Switch to English for showcase screenshot, open dropdown to display all 4 flags, and open ZeroAI
        print("[8] Switching to English and capturing full showcase screenshot...", flush=True)
        page.click(".lang-toggle-btn")
        time.sleep(0.3)
        page.click(".lang-item[data-lang='en']")
        time.sleep(0.5)

        # Open language popover so user can see all 4 flags (VN, US, CN, JP)
        page.click(".lang-toggle-btn")
        time.sleep(0.3)

        # Ensure ZeroAI is open
        page.evaluate("if (!isZeroAIChatOpen) toggleZeroAIChat(true);")
        time.sleep(0.6)

        os.makedirs(ARTIFACT_DIR, exist_ok=True)
        page.screenshot(path=SCREENSHOT_PATH, full_page=False)
        print(f"[SUCCESS] Multi-language audit passed 100%! Screenshot saved to: {SCREENSHOT_PATH}", flush=True)

        browser.close()

if __name__ == "__main__":
    run()

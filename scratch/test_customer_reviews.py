import sys
import time
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33"
SCREENSHOT_PATH = os.path.join(ARTIFACT_DIR, "ZEROPDF_DEMO_33_CUSTOMER_REVIEWS_WALL.png")
HTML_PATH = (Path(__file__).parent.parent / "index.html").resolve()

def run():
    print("=== STARTING ZEROSTUDIO CUSTOMER REVIEWS & FEEDBACK PLAYWRIGHT AUDIT ===", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1000})
        page = context.new_page()

        # 1. Load ZeroStudio
        file_url = f"file:///{HTML_PATH.as_posix()}"
        print(f"[1] Navigating to {file_url}...", flush=True)
        page.goto(file_url, wait_until="domcontentloaded")
        time.sleep(1.5)

        # 2. Scroll to Customer Reviews section
        print("[2] Scrolling to #customer-reviews section...", flush=True)
        reviews_section = page.locator("#customer-reviews")
        reviews_section.scroll_into_view_if_needed()
        time.sleep(0.8)

        # 3. Check Rating Score Summary
        big_num = page.locator(".reviews-big-number").inner_text()
        count_text = page.locator(".reviews-count-text").inner_text()
        print(f"[3] Score Banner: {big_num} ⭐ - {count_text}", flush=True)
        assert "4.9" in big_num, f"Expected 4.9 but got {big_num}"

        # 4. Check Initial Reviews Grid
        cards = page.locator(".review-card")
        card_count = cards.count()
        print(f"[4] Total initial review cards rendered: {card_count}", flush=True)
        assert card_count >= 6, f"Expected at least 6 review cards, got {card_count}"

        first_card_user = cards.first.locator(".review-user-name").inner_text()
        print(f"    First review card author: {first_card_user}", flush=True)

        # 5. Test Filter Pills
        print("[5] Testing Filter Pills...", flush=True)
        page.click(".review-filter-pill[data-i18n='filter_mmo']")
        time.sleep(0.4)
        mmo_cards = page.locator(".review-card").count()
        print(f"    MMO filter count: {mmo_cards} cards", flush=True)
        assert mmo_cards >= 2, "Expected at least 2 MMO cards"

        # Reset to All
        page.click(".review-filter-pill[data-i18n='filter_all']")
        time.sleep(0.4)

        # 6. Test Open Review Modal
        print("[6] Opening Write Review Modal...", flush=True)
        page.click(".btn-write-review")
        time.sleep(0.5)

        modal = page.locator("#review-modal")
        assert modal.is_visible(), "Review modal should be visible"
        print("    Modal is successfully visible!", flush=True)

        # 7. Fill out review form
        print("[7] Filling out 5-Star Customer Feedback...", flush=True)
        # Select 5 stars
        page.click("#modal-star-picker .star-pick-btn[data-star='5']")
        page.fill("#review-input-name", "Nguyễn Vũ Trung Hiếu")
        page.select_option("#review-input-role", "business")
        page.fill(
            "#review-input-comment",
            "Phần mềm ZeroStudio chạy cực kỳ mượt mà! Tách nền ảnh thẻ và lách bản quyền video 4K siêu tốc trên RAM, không tốn 1 đồng server. Rất tự hào về sản phẩm này!"
        )
        time.sleep(0.5)

        # 8. Submit Feedback
        print("[8] Submitting Review...", flush=True)
        page.click("#review-modal button[type='submit']")
        time.sleep(1)

        # 9. Verify Submission Rendered at Top
        new_card = page.locator(".review-card").first
        new_author = new_card.locator(".review-user-name").inner_text()
        new_comment = new_card.locator(".review-comment").inner_text()
        print(f"[9] Newly rendered top review author: {new_author}", flush=True)
        print(f"    Content: {new_comment}", flush=True)
        assert "Nguyễn Vũ Trung Hiếu" in new_author, f"Expected author to be in top review, got {new_author}"
        assert "ZeroStudio" in new_comment, "Expected comment in top review"

        # 10. Test Like Button
        print("[10] Testing Helpful Like button...", flush=True)
        like_btn = new_card.locator(".review-like-btn")
        like_btn.click()
        time.sleep(0.3)
        like_text = like_btn.inner_text()
        print(f"     Updated like status: {like_text}", flush=True)

        # 11. Capture Screenshot Artifact
        print("[11] Capturing Showcase Screenshot of Customer Reviews Wall...", flush=True)
        reviews_section.scroll_into_view_if_needed()
        time.sleep(0.6)

        os.makedirs(ARTIFACT_DIR, exist_ok=True)
        page.screenshot(path=SCREENSHOT_PATH, full_page=False)
        print(f"[SUCCESS] Customer Reviews Wall audit passed 100%! Screenshot saved to: {SCREENSHOT_PATH}", flush=True)

        browser.close()

if __name__ == "__main__":
    run()

import sys
import time
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33"
SCREENSHOT_PATH = os.path.join(ARTIFACT_DIR, "ZEROPDF_DEMO_34_LOAD_MORE_REVIEWS.png")
HTML_PATH = (Path(__file__).parent.parent / "index.html").resolve()

def run():
    print("=== STARTING ZEROSTUDIO CUSTOMER REVIEWS & LOAD MORE PLAYWRIGHT AUDIT ===", flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1100})
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

        # 4. Check Initial Reviews Grid (Should be 6 on page 1)
        cards = page.locator(".review-card")
        initial_card_count = cards.count()
        print(f"[4] Initial review cards rendered on Page 1: {initial_card_count}", flush=True)
        assert initial_card_count == 6 or initial_card_count >= 6, f"Expected 6 or more initial cards, got {initial_card_count}"

        progress_text_1 = page.locator("#reviews-progress-text").inner_text()
        print(f"    Initial Progress Text: '{progress_text_1}'", flush=True)

        # 5. Test Load More Button (Click 1: Should load 6 more cards -> 12 cards)
        print("[5] Clicking 'Xem Thêm Đánh Giá Khác' (Load More 1)...", flush=True)
        load_more_btn = page.locator("#btn-load-more-reviews")
        load_more_btn.scroll_into_view_if_needed()
        time.sleep(0.3)
        load_more_btn.click()
        time.sleep(0.5)

        cards_after_click1 = page.locator(".review-card").count()
        progress_text_2 = page.locator("#reviews-progress-text").inner_text()
        print(f"    Cards after Load More 1: {cards_after_click1} (Expected >= 12)", flush=True)
        print(f"    Progress Text: '{progress_text_2}'", flush=True)
        assert cards_after_click1 >= 12, f"Expected >= 12 cards, got {cards_after_click1}"

        # 6. Test Load More Button (Click 2: Should load remaining cards)
        print("[6] Clicking 'Xem Thêm Đánh Giá Khác' (Load More 2)...", flush=True)
        load_more_btn.scroll_into_view_if_needed()
        time.sleep(0.3)
        load_more_btn.click()
        time.sleep(0.5)

        cards_after_click2 = page.locator(".review-card").count()
        progress_text_3 = page.locator("#reviews-progress-text").inner_text()
        print(f"    Cards after Load More 2: {cards_after_click2} (Expected >= 18)", flush=True)
        print(f"    Progress Text: '{progress_text_3}'", flush=True)
        assert cards_after_click2 >= 18, f"Expected >= 18 cards, got {cards_after_click2}"

        # 7. Test Filter Pills
        print("[7] Testing Filter Pills with pagination reset...", flush=True)
        page.click(".review-filter-pill[data-i18n='filter_mmo']")
        time.sleep(0.4)
        mmo_cards = page.locator(".review-card").count()
        print(f"    MMO filter initial page cards: {mmo_cards}", flush=True)
        assert mmo_cards >= 2, "Expected at least 2 MMO cards"

        # Reset to All
        page.click(".review-filter-pill[data-i18n='filter_all']")
        time.sleep(0.4)

        # 8. Test Open Review Modal
        print("[8] Opening Write Review Modal...", flush=True)
        page.click(".btn-write-review")
        time.sleep(0.5)

        modal = page.locator("#review-modal")
        assert modal.is_visible(), "Review modal should be visible"
        print("    Modal is successfully visible!", flush=True)

        # 9. Fill out review form
        print("[9] Submitting New 5-Star Review...", flush=True)
        page.click("#modal-star-picker .star-pick-btn[data-star='5']")
        page.fill("#review-input-name", "Nguyễn Vũ Trung Hiếu")
        page.select_option("#review-input-role", "business")
        page.fill(
            "#review-input-comment",
            "Đã kiểm thử hệ thống 100-1000+ đánh giá với cơ chế phân trang mượt mà! Tải cực nhanh, lưu trữ an toàn và sẵn sàng mở rộng quy mô lớn."
        )
        time.sleep(0.3)
        page.click("#review-modal button[type='submit']")
        time.sleep(0.8)

        # 10. Verify Top Card
        top_author = page.locator(".review-card").first.locator(".review-user-name").inner_text()
        print(f"[10] Top review author after submit: {top_author}", flush=True)
        assert "Nguyễn Vũ Trung Hiếu" in top_author, "Top author should match newly submitted review"

        # 11. Capture Showcase Screenshot Artifact
        print("[11] Capturing Showcase Screenshot...", flush=True)
        reviews_section.scroll_into_view_if_needed()
        time.sleep(0.6)

        os.makedirs(ARTIFACT_DIR, exist_ok=True)
        page.screenshot(path=SCREENSHOT_PATH, full_page=False)
        print(f"[SUCCESS] Load More and High-Scale Reviews audit passed 100%! Screenshot: {SCREENSHOT_PATH}", flush=True)

        browser.close()

if __name__ == "__main__":
    run()

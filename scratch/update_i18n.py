PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\libs\i18n.js"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# vi
vi_target = 'btn_load_more_reviews: "Xem Thêm Đánh Giá Khác",'
vi_replace = """btn_load_more_reviews: "Xem Thêm Đánh Giá Khác",
        pwa_install_btn: "Cài App",
        affiliate_nav_btn: "Hoa Hồng 30%",
        aff_modal_title: "CHƯƠNG TRÌNH ĐỐI TÁC ZEROSTUDIO",
        aff_modal_sub: "Lan tỏa siêu công cụ Video & PDF — Nhận 30% hoa hồng trực tiếp qua Ngân Hàng / Zalo","""

# en
en_target = 'btn_load_more_reviews: "Load More Reviews",'
en_replace = """btn_load_more_reviews: "Load More Reviews",
        pwa_install_btn: "Install App",
        affiliate_nav_btn: "Earn 30%",
        aff_modal_title: "ZEROSTUDIO PARTNER PROGRAM",
        aff_modal_sub: "Share premium Video & PDF tool — Earn 30% instant commission via Bank / Zalo","""

# zh
zh_target = 'btn_load_more_reviews: "加载更多评价",'
zh_replace = """btn_load_more_reviews: "加载更多评价",
        pwa_install_btn: "安装应用",
        affiliate_nav_btn: "赚取30%佣金",
        aff_modal_title: "ZEROSTUDIO合伙人推广计划",
        aff_modal_sub: "推广终极视频与PDF处理工具 — 获得30%高额实时佣金","""

# ja
ja_target = 'btn_load_more_reviews: "もっとレビューを見る",'
ja_replace = """btn_load_more_reviews: "もっとレビューを見る",
        pwa_install_btn: "アプリをインストール",
        affiliate_nav_btn: "30%報酬を獲得",
        aff_modal_title: "ZEROSTUDIOアフィリエイトプログラム",
        aff_modal_sub: "究極の動画・PDFツールを共有 — 30%の即時報酬を獲得","""

assert vi_target in content, "vi_target not found"
assert en_target in content, "en_target not found"
assert zh_target in content, "zh_target not found"
assert ja_target in content, "ja_target not found"

content = content.replace(vi_target, vi_replace, 1)
content = content.replace(en_target, en_replace, 1)
content = content.replace(zh_target, zh_replace, 1)
content = content.replace(ja_target, ja_replace, 1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: libs/i18n.js updated across VI, EN, ZH, JA!")

/**
 * ZeroStudio - Multi-Language Internationalization (i18n) Engine v2.5.3
 * Supported Languages:
 *   - vi: Tiếng Việt (Default native primary language)
 *   - en: English (Global creators, MMO specialists, US/EU traffic)
 *   - zh: 中文 - 简体 (Taobao, Douyin, 1688, cross-border creators)
 *   - ja: 日本語 (Japanese creators & video editing studios)
 */

const TRANSLATIONS = {
    vi: {
        // Brand & Header
        brand_tag: "v2.5 OTA WASM",
        download_desktop_btn: "Tải Desktop (.EXE)",
        pro_unlock_btn: "Nâng Cấp Pro (299k)",
        zk_badge_text: "Zero-Knowledge • 100% Offline",
        lang_name: "Tiếng Việt",
        pwa_install_btn: "Cài App",
        affiliate_nav_btn: "Hoa Hồng 30%",

        // Hero
        hero_badge: "TIỆN ÍCH VĂN PHÒNG & AI VIDEO MMO 2026",
        hero_title: "Siêu Ứng Dụng Xử Lý PDF & AI Video MMO",
        hero_sub: "Công nghệ Zero-Knowledge: 100% dữ liệu xử lý trực tiếp trên RAM/GPU thiết bị của bạn. 0 Byte gửi ra ngoài máy chủ. Bảo mật tuyệt đối.",

        // Bento Tabs
        tab_merge: "Gộp PDF",
        tab_split: "Tách & Cắt Trang",
        tab_img2pdf: "Ảnh Sang PDF",
        tab_compress: "Nén PDF Thông Minh",
        tab_upscale: "✨ Phóng To Ảnh 4K",
        tab_video: "🎬 Video Không Logo & 4K",
        tab_batch: "Bàn Làm Việc Hàng Loạt",
        tab_bg_ocr: "AI Tách Nền & OCR",

        // Battle Slider
        battle_badge: "BATTLE TEST • TRƯỚC VÀ SAU LÁCH THUẬT TOÁN AI",
        battle_title: "So Sánh Trực Quan: Video Gốc vs Sau Khi Qua ZeroStudio",
        battle_sub: "Kéo thanh trượt qua lại để xem sự khác biệt thực chiến: Từ video dính chữ Tàu, dính bản quyền 0 view biến thành video 9:16 sắc nét tràn viền, sạch logo và sẵn sàng cắn đề xuất triệu view!",
        btn_split_50: "50 / 50 Cân Đối",
        btn_split_before: "100% Video Gốc",
        btn_split_after: "100% ZeroStudio",
        btn_split_radar: "Quét Tự Động Radar",
        hud_before_title: "TRƯỚC XỬ LÝ (VIDEO GỐC)",
        hud_after_title: "SAU ZEROSTUDIO (1-CLICK)",

        // Customer Reviews
        reviews_badge: "BẢO CHỨNG CHẤT LƯỢNG • 1,480+ ĐÁNH GIÁ 5 SAO",
        reviews_title: "Khách Hàng Nói Gì Về ZeroStudio?",
        reviews_sub: "Đánh giá và đóng góp ý kiến thực tế từ các Creator MMO, Kế toán trưởng, Studio Content và Doanh nghiệp trên toàn quốc.",
        reviews_count_text: "1,482+ Đánh Giá Hài Lòng • 98.6% Khuyên Dùng",
        btn_write_review: "Viết Đánh Giá Của Bạn",
        filter_all: "Tất Cả (1,480+)",
        filter_5star: "5 Sao ⭐",
        filter_mmo: "Dân Video MMO 🔥",
        filter_office: "Văn Phòng & Kế Toán 📑",
        filter_mine: "Đánh Giá Của Bạn 👤",
        review_modal_title: "Đánh Giá & Góp Ý ZeroStudio",
        review_modal_sub: "Ý kiến của bạn sẽ được hiển thị trực tiếp trên trang chủ và gửi tới đội ngũ phát triển!",
        review_input_name_lbl: "Họ Tên / Biệt Danh:",
        review_input_name_ph: "Ví dụ: Hoàng Long (MMO Douyin)",
        review_input_role_lbl: "Lĩnh Vực Hoạt Động:",
        review_input_comment_lbl: "Nội Dung Nhận Xét & Góp Ý:",
        review_input_comment_ph: "Chia sẻ trải nghiệm của bạn về tính năng lách bản quyền, nén PDF hoặc góp ý thêm tính năng mới...",
        btn_cancel: "Hủy",
        btn_submit_review: "Gửi Đánh Giá Ngay",
        btn_load_more_reviews: "Xem Thêm Đánh Giá Khác",

        // Affiliate Modal
        aff_modal_title: "CHƯƠNG TRÌNH ĐỐI TÁC ZEROSTUDIO",
        aff_modal_sub: "Lan tỏa siêu công cụ Video & PDF — Nhận 30% - 35% hoa hồng trực tiếp qua Ngân Hàng / Zalo",
        aff_rule_cpa: "<strong>Cơ chế CPA thanh toán thực:</strong> Hoa hồng được kích hoạt và cộng dồn ngay khi người được giới thiệu thanh toán thành công gói Pro/Ultra qua VietQR MB Bank. Tuyệt đối không tính lượt đăng ký ảo, đảm bảo quỹ hoa hồng tiền tươi 100%.",
        aff_tier_pro_desc: "Hoa hồng 30% (Khách giảm 10% còn 269k)",
        aff_tier_ultra_desc: "Hoa hồng 35% (Khách giảm 10% còn 629k)",
        aff_ladder_title: "🏆 THANG CẤP BẬC ĐỐI TÁC (TÍCH LŨY ĐƠN HÀNG THÀNH CÔNG)",
        aff_ladder_bronze: "🥉 Tân Thủ: 1 – 10 đơn (25-30%)",
        aff_ladder_silver: "🥈 Chuyên Nghiệp: 11 – 50 đơn (30-35%)",
        aff_ladder_gold: "🥇 Master Đại Lý: > 50 đơn (+1TR Thưởng)",
        aff_payout_note: "Khách quét mã thanh toán nổ tiền vào MB Bank, hệ thống tự động ghi nhận mã REF. Rút tiền nhanh trong 24h qua STK Zalo.",
        aff_register_btn: "Đăng Ký STK Qua Zalo",

        // Modals & Pricing Header
        pro_modal_title: "ZeroStudio Desktop Pro",
        pro_modal_sub: "Khai phá 100% sức mạnh phần cứng máy tính • Batch Processing 500+ files • Không giới hạn",

        // Founder 100-Slot Tracker
        tracker_status_founder: "ƯU ĐÃI FOUNDER EDITION • GIỚI HẠN 100 SUẤT ĐẦU",
        tracker_status_soldout: "🔒 ĐÃ ĐỦ 100 SUẤT FOUNDER • ĐANG ÁP DỤNG GIÁ NIÊM YẾT CHÍNH THỨC",
        tracker_slots_prefix: "Chỉ còn",
        tracker_slots_suffix: "suất",
        tracker_slots_full: "Đã hết 100/100 suất",
        tracker_explain_founder: "🔥 Đã đăng ký {slots}/100 suất ưu đãi. Khi đủ 100 suất, hệ thống sẽ tự động chuyển về giá niêm yết chính thức.",
        tracker_explain_soldout: "⚠️ Chương trình ưu đãi 100 suất Founder Edition đã kết thúc. Hiện đang áp dụng mức giá niêm yết chính thức trên toàn hệ thống.",

        // Pricing Cards - Free
        free_tier_badge: "WEB FREE",
        free_tier_price: "0đ",
        free_tier_period: "/ Vĩnh viễn",
        free_tier_desc: "Phù hợp nhu cầu cá nhân xử lý tài liệu và video nhẹ hàng ngày.",
        free_feat_1: "Gộp, tách PDF cơ bản",
        free_feat_2: "Tải từng video lẻ không logo",
        free_feat_3: "Giới hạn 3 video/ngày",
        free_feat_4: "Khóa nén PDF nâng cao",
        free_feat_5: "Không hỗ trợ xử lý hàng loạt",
        free_tier_btn: "Đang Sử Dụng (Web)",

        // Pricing Cards - Pro
        pro_tier_badge: "FOUNDER EDITION • 100 SUẤT",
        pro_tier_badge_std: "BẢN QUYỀN CHÍNH THỨC",
        pro_tier_title: "DESKTOP PRO",
        pro_tier_price: "299.000đ",
        pro_tier_price_std: "599.000đ",
        pro_tier_old_price: "599.000đ",
        pro_tier_period: "/ Năm đầu",
        pro_tier_period_std: "/ Năm",
        pro_tier_desc: "Sử dụng vĩnh viễn v2.5 trên 1 thiết bị + 365 ngày cập nhật OTA (Gia hạn 199k/năm).",
        pro_feat_1: "Tải video đơn lẻ không watermark không giới hạn",
        pro_feat_2: "<strong>Nén PDF 3 Preset:</strong> Giảm 88% dung lượng chuẩn in ấn & thuế",
        pro_feat_3: "<strong>Bóc tách phụ đề & dịch SRT:</strong> Trích xuất text đa ngôn ngữ",
        pro_feat_4: "<strong>Nâng cấp 4K & Xóa Logo góc:</strong> Khử watermark cứng",
        pro_feat_5: "<strong>Sở hữu vĩnh viễn v2.5:</strong> Bao gồm 12 tháng update thuật toán",
        btn_choose_pro: "Đăng Ký Gói Pro (299k)",
        btn_choose_pro_std: "Đăng Ký Gói Pro (599k)",

        // Pricing Cards - Ultra
        ultra_tier_badge: "FOUNDER EDITION • CAO CẤP NHẤT",
        ultra_tier_badge_std: "CHIẾN HẠM MMO CHÍNH THỨC",
        ultra_tier_title: "ULTRA MMO MASTER",
        ultra_tier_price: "699.000đ",
        ultra_tier_price_std: "1.490.000đ",
        ultra_tier_old_price: "1.490.000đ",
        ultra_tier_period: "/ Năm đầu",
        ultra_tier_period_std: "/ Năm",
        ultra_tier_desc: "Dành riêng cho Dân Reup MMO & Studio Content cần kháng quét liên tục (Gia hạn 499k/năm).",
        ultra_feat_1: "<strong>Bàn Làm Việc Hàng Loạt:</strong> Treo máy chạy 500 file, chuông báo xong",
        ultra_feat_2: "<strong>AI Auto-Crop 9:16 Dual-Layer:</strong> Biến 16:9 sang 9:16 nền mờ caustics",
        ultra_feat_3: "<strong>Audio Pitch & Speed Randomizer:</strong> Đổi vi tần số hỗ trợ kháng quét bản quyền",
        ultra_feat_4: "<strong>Super Crawler:</strong> Cào cả kênh YouTube Shorts / Reels / TikTok có bộ lọc view",
        ultra_feat_5: "<strong>Xóa Sub Chữ & Logo Cũ:</strong> Khử phụ đề tiếng Trung 1 click",
        ultra_feat_6: "<strong>Bản quyền 2 Thiết Bị (PC + Laptop):</strong> Vĩnh viễn v2.5 + 365 ngày update thuật toán",
        btn_choose_ultra: "Đăng Ký Gói Ultra (699k)",
        btn_choose_ultra_std: "Đăng Ký Gói Ultra (1.490k)",

        // Transparency Banner
        transparency_title: "CAM KẾT MINH BẠCH FOUNDER EDITION (GIỚI HẠN 100 SUẤT ĐẦU)",
        transparency_bullet_1: "• <strong>Sở hữu vĩnh viễn:</strong> Bạn sở hữu vĩnh viễn bộ tính năng ZeroStudio phiên bản hiện tại trên thiết bị cá nhân mà không lo bị khóa app.",
        transparency_bullet_2: "• <strong>365 Ngày Cập Nhật OTA:</strong> Miễn phí 1 năm update các thuật toán kháng quét mới nhất theo biến động của TikTok, Facebook Reels, YouTube.",
        transparency_bullet_3: "• <strong>Chính sách Gia hạn Ưu đãi:</strong> Sau 365 ngày, bạn có thể tiếp tục sử dụng bình thường bản v2.5 hoặc gia hạn gói cập nhật công nghệ mới chỉ <strong>199k/năm (Pro)</strong> hoặc <strong>499k/năm (Ultra)</strong>. Không cam kết né quét 100% vĩnh viễn mà bảo đảm đồng hành nghiên cứu thuật toán liên tục.",

        // License Key Deck
        license_have_key: "Đã có mã kích hoạt Pro hoặc Ultra?",
        license_input_ph: "Nhập khóa bản quyền: ZERO-PRO-... hoặc ZERO-ULTRA-...",
        license_activate_btn: "Kích Hoạt Ngay",

        // VietQR Checkout
        checkout_back_btn: "Quay lại bảng giá",
        checkout_secure_tag: "BẢO MẬT VIETQR • TỰ ĐỘNG CẤP KEY",
        checkout_qr_instruction: "Mở App Ngân Hàng hoặc Ví Điện Tử quét mã VietQR để thanh toán tự động:",
        checkout_bank_name: "Ngân Hàng MB Bank",
        checkout_acc_name_lbl: "Chủ tài khoản:",
        checkout_acc_num_lbl: "Số tài khoản:",
        checkout_amount_lbl: "Số tiền thanh toán:",
        checkout_memo_lbl: "Nội dung chuyển khoản (bắt buộc):",
        checkout_memo_note: "⚠️ Vui lòng giữ nguyên nội dung chuyển khoản để máy chủ đối soát cấp key tự động.",
        checkout_btn_confirm_paid: "Tôi Đã Chuyển Khoản • Nhận Key Ngay",
        checkout_support_contact: "Hỗ trợ kích hoạt nhanh qua Zalo Admin 24/7:",

        // License Success
        success_title: "THANH TOÁN THÀNH CÔNG!",
        success_desc: "Cảm ơn bạn đã nâng cấp ZeroStudio Desktop Pro. Khóa bản quyền vĩnh viễn đã được tạo và tự động kích hoạt trên thiết bị này!",
        success_key_lbl: "MÃ BẢN QUYỀN PRO CỦA BẠN:",
        success_btn_copy: "Sao Chép Mã Key",
        success_btn_start: "Bắt Đầu Sử Dụng Ngay",

        // Common Tool Actions & Dropzones
        stage_drop_pdf: "Kéo & thả các tệp PDF vào đây",
        stage_drop_pdf_sub: "Hoặc chọn nhiều file cùng lúc từ máy tính của bạn",
        btn_choose_pdf: "Chọn Tệp PDF",
        btn_clear_all: "Xóa Hết",
        btn_merge_download: "Gộp & Tải Về Ngay",

        split_title: "Chọn tệp PDF cần Tách hoặc Cắt trang",
        split_sub: "Tự động dựng ma trận hình thu nhỏ từng trang để bạn chọn lọc",
        btn_select_all: "Chọn Tất Cả",
        btn_deselect_all: "Bỏ Chọn",
        btn_rotate_90: "🔄 Xoay 90°",
        btn_export_split: "Xuất Trang Đã Chọn",

        img2pdf_title: "Kéo & thả hình ảnh JPG / PNG vào đây",
        img2pdf_sub: "Đóng gói hàng loạt ảnh thành file PDF sắc nét đúng tỉ lệ",
        btn_choose_img: "Chọn Hình Ảnh",
        btn_export_pdf: "Xuất File PDF",

        upscale_title: "Kéo & thả ảnh cần Phóng to 4K vào đây",
        upscale_sub: "Khử nhiễu, tái tạo chi tiết và phóng to 2X / 4X bằng WebAssembly AI",
        btn_run_upscale: "Chạy AI Upscale Ngay",
        btn_change_img: "Đổi Ảnh",

        video_downloader_title: "Siêu Tải Video Không Watermark",
        video_url_ph: "Dán liên kết TikTok, Facebook Reels, YouTube Shorts...",
        btn_extract_video: "Trích Xuất Video Ngay",
        video_mmo_title: "Bộ Xử Lý Video MMO & Lách Bản Quyền",
        crop_916_lbl: "Auto-Crop 9:16 Dual-Layer (Nền mờ Caustics)",
        audio_pitch_lbl: "Xáo trộn vi tần số âm thanh né quét (Randomizer)",
        remove_sub_lbl: "Khử phụ đề tiếng Trung & Logo cũ 1 click",
        batch_stage_title: "Bàn Làm Việc Hàng Loạt (Batch Processing)",
        btn_start_batch: "Bắt Đầu Chạy Hàng Loạt",

        // ZeroAI Chatbot
        zeroai_trigger_title: "Trợ Lý AI 24/7",
        zeroai_trigger_tag: "Tư Vấn Tức Thì",
        zeroai_title: "ZeroAI Specialist 24/7",
        zeroai_subtitle: "Trợ lý Chuyên gia Bản quyền & AI Studio",
        zeroai_welcome: "Xin chào! Tôi là <strong>ZeroAI Specialist</strong> – Trợ lý chuyên gia 24/7 của bạn tại ZeroStudio.<br><br>Tôi có thể hỗ trợ bạn ngay lập tức:<br>• <strong>Lách bản quyền video MMO</strong> (Auto-crop 9:16, xáo âm thanh, xóa sub/logo).<br>• <strong>AI Background Remover</strong> (Tách nền ảnh thẻ CCCD, Visa sắc nét).<br>• <strong>AI Vietnamese OCR</strong> (Quét chữ tiếng Việt trích xuất sang Word .doc).<br>• <strong>So sánh & Hướng dẫn kích hoạt</strong> gói Pro (299k) và Ultra (699k).<br><br>Hãy chọn gợi ý nhanh bên trên hoặc nhập câu hỏi của bạn nhé!",
        zeroai_input_ph: "Hỏi về lách MMO, tách nền, OCR, giá gói...",

        // Footer
        footer_text_1: "<strong>ZeroPDF Studio</strong> • Kiến trúc WebAssembly 100% Client-Side.",
        footer_text_2: "Bảo mật tuyệt đối • Không máy chủ trung gian • Không thu thập dữ liệu cá nhân"
    },

    en: {
        // Brand & Header
        brand_tag: "v2.5 OTA WASM",
        download_desktop_btn: "Download (.EXE)",
        pro_unlock_btn: "Upgrade Pro ($12)",
        zk_badge_text: "Zero-Knowledge • 100% Offline",
        lang_name: "English",
        pwa_install_btn: "Install App",
        affiliate_nav_btn: "30% Commission",

        // Hero
        hero_badge: "OFFICE SUITE & AI VIDEO MMO 2026",
        hero_title: "Ultimate PDF Suite & AI Video MMO",
        hero_sub: "Zero-Knowledge Architecture: 100% processed directly in your browser RAM/GPU. 0 bytes sent out. Absolute privacy guaranteed.",

        // Bento Tabs
        tab_merge: "Merge PDF",
        tab_split: "Split & Rotate",
        tab_img2pdf: "Image to PDF",
        tab_compress: "Smart Compress",
        tab_upscale: "✨ 4K AI Upscaler",
        tab_video: "🎬 Clean Video Downloader",
        tab_batch: "Batch Workbench",
        tab_bg_ocr: "AI Cutout & OCR",

        // Battle Slider
        battle_badge: "BATTLE TEST • BEFORE & AFTER AI ALGORITHM EVASION",
        battle_title: "Live Comparison: Raw Video vs After ZeroStudio",
        battle_sub: "Drag the slider to inspect real battle results: From watermarked Chinese clips with 0 views to edge-to-edge 9:16 viral videos ready to hit the algorithmic feed!",
        btn_split_50: "50 / 50 Balanced",
        btn_split_before: "100% Raw Video",
        btn_split_after: "100% ZeroStudio",
        btn_split_radar: "Radar Auto-Scan",
        hud_before_title: "BEFORE PROCESSING (RAW INPUT)",
        hud_after_title: "AFTER ZEROSTUDIO (1-CLICK)",

        // Customer Reviews
        reviews_badge: "PROVEN QUALITY • 1,480+ 5-STAR RATINGS",
        reviews_title: "What Creators Say About ZeroStudio?",
        reviews_sub: "Real testimonials and feature requests from global MMO creators, accounting leads, content studios, and enterprise teams.",
        reviews_count_text: "1,482+ Satisfied Reviews • 98.6% Recommend",
        btn_write_review: "Write Your Review",
        filter_all: "All Reviews (1,480+)",
        filter_5star: "5 Stars ⭐",
        filter_mmo: "MMO Video Creators 🔥",
        filter_office: "Office & Finance 📑",
        filter_mine: "Your Reviews 👤",
        review_modal_title: "Review & Feedback ZeroStudio",
        review_modal_sub: "Your feedback will be published live and forwarded directly to our engineering core team!",
        review_input_name_lbl: "Your Name / Handle:",
        review_input_name_ph: "e.g., Alex Johnson (MMO Creator)",
        review_input_role_lbl: "Industry / Field:",
        review_input_comment_lbl: "Review & Suggestions:",
        review_input_comment_ph: "Share your experience with video fair-use remasters, PDF smart compression, or suggest new features...",
        btn_cancel: "Cancel",
        btn_submit_review: "Submit Review Now",
        btn_load_more_reviews: "Load More Reviews",

        // Affiliate Modal
        aff_modal_title: "ZEROSTUDIO PARTNER PROGRAM",
        aff_modal_sub: "Share premium Video & PDF tool — Earn 30% - 35% direct commission via Bank / Zalo",
        aff_rule_cpa: "<strong>Real-Payment CPA Model:</strong> Commission is recorded instantly when the referred customer completes VietQR MB Bank payment. Zero fake accounts counted, 100% verified cash payout.",
        aff_tier_pro_desc: "30% Commission (Referred user gets 10% off at 269k)",
        aff_tier_ultra_desc: "35% Commission (Referred user gets 10% off at 629k)",
        aff_ladder_title: "🏆 PARTNER TIER LADDER (ACCUMULATED PAID ORDERS)",
        aff_ladder_bronze: "🥉 Bronze: 1 – 10 orders (25-30%)",
        aff_ladder_silver: "🥈 Silver: 11 – 50 orders (30-35%)",
        aff_ladder_gold: "🥇 Gold Master: > 50 orders (+1M VND Bonus)",
        aff_payout_note: "When client completes bank payment, REF code is automatically linked. Fast payout within 24h via Bank / Zalo.",
        aff_register_btn: "Register Payout via Zalo",

        // Modals & Pricing Header
        pro_modal_title: "ZeroStudio Desktop Pro",
        pro_modal_sub: "Unlock 100% raw hardware power • Batch Processing 500+ files • No limits",

        // Founder 100-Slot Tracker
        tracker_status_founder: "FOUNDER EDITION OFFER • LIMITED 100 SLOTS",
        tracker_status_soldout: "🔒 100 FOUNDER SLOTS FILLED • STANDARD PRICING APPLIED",
        tracker_slots_prefix: "Only",
        tracker_slots_suffix: "slots left",
        tracker_slots_full: "Sold Out 100/100",
        tracker_explain_founder: "🔥 Claimed {slots}/100 slots. Automatically switches to standard price when 100 slots are reached.",
        tracker_explain_soldout: "⚠️ The 100 Early Founder slots have sold out. Official standard pricing now applies.",

        // Pricing Cards - Free
        free_tier_badge: "WEB FREE",
        free_tier_price: "$0",
        free_tier_period: "/ Forever",
        free_tier_desc: "Perfect for personal everyday light documents & video tasks.",
        free_feat_1: "Basic PDF merge & split",
        free_feat_2: "Single video download without watermark",
        free_feat_3: "Limit 3 videos / day",
        free_feat_4: "Advanced PDF compression locked",
        free_feat_5: "No batch processing",
        free_tier_btn: "Current Plan (Web)",

        // Pricing Cards - Pro
        pro_tier_badge: "FOUNDER EDITION • 100 SLOTS",
        pro_tier_badge_std: "OFFICIAL STANDARD",
        pro_tier_title: "DESKTOP PRO",
        pro_tier_price: "299.000đ (~$12)",
        pro_tier_price_std: "599.000đ (~$24)",
        pro_tier_old_price: "599.000đ",
        pro_tier_period: "/ 1st Year",
        pro_tier_period_std: "/ Year",
        pro_tier_desc: "Lifetime ownership of v2.5 on 1 device + 365 days of OTA updates (Renewal: 199k/year).",
        pro_feat_1: "Unlimited single video extraction without watermark",
        pro_feat_2: "<strong>Smart PDF 3-Preset:</strong> Reduce up to 88% size for print & tax",
        pro_feat_3: "<strong>Subtitle Extraction & SRT:</strong> Multi-language speech-to-text",
        pro_feat_4: "<strong>4K Remaster & Logo Erase:</strong> Remove static hard watermarks",
        pro_feat_5: "<strong>Lifetime v2.5 License:</strong> Includes 12 months algorithm updates",
        btn_choose_pro: "Get Pro Plan (299k VND / ~$12)",
        btn_choose_pro_std: "Get Pro Plan (599k VND / ~$24)",

        // Pricing Cards - Ultra
        ultra_tier_badge: "FOUNDER EDITION • BEST VALUE",
        ultra_tier_badge_std: "MMO MASTER OFFICIAL",
        ultra_tier_title: "ULTRA MMO MASTER",
        ultra_tier_price: "699.000đ (~$28)",
        ultra_tier_price_std: "1.490.000đ (~$60)",
        ultra_tier_old_price: "1.490.000đ",
        ultra_tier_period: "/ 1st Year",
        ultra_tier_period_std: "/ Year",
        ultra_tier_desc: "Engineered for MMO Reup Creators & Content Studios needing continuous algorithm evasion (Renewal: 499k/year).",
        ultra_feat_1: "<strong>Batch Workbench:</strong> Run 500 files in background with sound chime",
        ultra_feat_2: "<strong>AI Auto-Crop 9:16 Dual-Layer:</strong> Transform 16:9 to 9:16 caustics blur",
        ultra_feat_3: "<strong>Audio Pitch & Speed Randomizer:</strong> Evade acoustic fingerprint matching",
        ultra_feat_4: "<strong>Super Crawler:</strong> Scrape entire Shorts/Reels/TikTok channels by views",
        ultra_feat_5: "<strong>Hard Sub & Watermark Remover:</strong> 1-click text eraser",
        ultra_feat_6: "<strong>2 Device License (PC + Laptop):</strong> Lifetime v2.5 + 365 days updates",
        btn_choose_ultra: "Get Ultra Plan (699k VND / ~$28)",
        btn_choose_ultra_std: "Get Ultra Plan (1.490k VND / ~$60)",

        // Transparency Banner
        transparency_title: "FOUNDER EDITION TRANSPARENCY COMMITMENT (100 SLOTS ONLY)",
        transparency_bullet_1: "• <strong>Permanent Ownership:</strong> You permanently own all current ZeroStudio features on your hardware without subscription lockouts.",
        transparency_bullet_2: "• <strong>365 Days OTA Updates:</strong> 1 year of continuous algorithm adaptation updates as TikTok, Facebook Reels, and YouTube evolve.",
        transparency_bullet_3: "• <strong>Discounted Renewal Policy:</strong> After 365 days, keep using your current build forever, or renew algorithm updates from just <strong>199k/year (Pro)</strong> or <strong>499k/year (Ultra)</strong>. We guarantee honest algorithm research and partnership.",

        // License Key Deck
        license_have_key: "Already have a Pro or Ultra activation key?",
        license_input_ph: "Enter activation key: ZERO-PRO-... or ZERO-ULTRA-...",
        license_activate_btn: "Activate Now",

        // VietQR Checkout
        checkout_back_btn: "Back to Pricing",
        checkout_secure_tag: "SECURE VIETQR • AUTO LICENSE DISPATCH",
        checkout_qr_instruction: "Scan the VietQR code using your Banking App or Mobile Wallet:",
        checkout_bank_name: "MB Bank Vietnam",
        checkout_acc_name_lbl: "Account Name:",
        checkout_acc_num_lbl: "Account Number:",
        checkout_amount_lbl: "Payment Amount:",
        checkout_memo_lbl: "Payment Memo (Required):",
        checkout_memo_note: "⚠️ Please enter the exact memo above so our automated bank webhook instantly issues your license.",
        checkout_btn_confirm_paid: "I Have Transferred • Receive Key Now",
        checkout_support_contact: "24/7 Dedicated Support via Zalo Admin:",

        // License Success
        success_title: "PAYMENT VERIFIED SUCCESSFULLY!",
        success_desc: "Thank you for upgrading to ZeroStudio Desktop Pro. Your license key has been cryptographically signed and activated!",
        success_key_lbl: "YOUR PRO LICENSE KEY:",
        success_btn_copy: "Copy License Key",
        success_btn_start: "Start Using Pro Now",

        // Common Tool Actions & Dropzones
        stage_drop_pdf: "Drag & drop PDF files here",
        stage_drop_pdf_sub: "Or select multiple files from your computer",
        btn_choose_pdf: "Select PDF Files",
        btn_clear_all: "Clear All",
        btn_merge_download: "Merge & Download Now",

        split_title: "Select PDF to Split or Extract Pages",
        split_sub: "Generates visual matrix thumbnails of each page for easy selection",
        btn_select_all: "Select All",
        btn_deselect_all: "Deselect All",
        btn_rotate_90: "🔄 Rotate 90°",
        btn_export_split: "Export Selected Pages",

        img2pdf_title: "Drag & drop JPG / PNG images here",
        img2pdf_sub: "Package multiple images into high-resolution PDF",
        btn_choose_img: "Select Images",
        btn_export_pdf: "Export PDF File",

        upscale_title: "Drag & drop image for 4K AI Upscaling",
        upscale_sub: "Denoise, restore details and upscale 2X / 4X with WebAssembly AI",
        btn_run_upscale: "Run AI Upscale Now",
        btn_change_img: "Change Image",

        video_downloader_title: "No-Watermark Video Downloader",
        video_url_ph: "Paste link from TikTok, Facebook Reels, YouTube Shorts...",
        btn_extract_video: "Extract Video Now",
        video_mmo_title: "MMO Video Fair-Use & Evade Engine",
        crop_916_lbl: "Auto-Crop 9:16 Dual-Layer (Caustics Blur)",
        audio_pitch_lbl: "Randomize audio micro-frequencies (Pitch/Speed Randomizer)",
        remove_sub_lbl: "1-Click Chinese hard subtitle & logo eraser",
        batch_stage_title: "Batch Processing Studio",
        btn_start_batch: "Start Batch Processing",

        // ZeroAI Chatbot
        zeroai_trigger_title: "AI Specialist 24/7",
        zeroai_trigger_tag: "Instant Support",
        zeroai_title: "ZeroAI Specialist 24/7",
        zeroai_subtitle: "Specialist in DRM, Video MMO & AI Studio",
        zeroai_welcome: "Hello! I am <strong>ZeroAI Specialist</strong> – Your 24/7 dedicated AI assistant at ZeroStudio.<br><br>I can assist you with:<br>• <strong>MMO Video Fair-Use Remaster</strong> (Auto-crop 9:16, audio pitch, logo/sub removal).<br>• <strong>AI Background Remover</strong> (Passport, ID, Visa photo cutout).<br>• <strong>AI Document OCR</strong> (Extract text to Word .doc).<br>• <strong>License Comparison & Activation</strong> for Pro and Ultra.<br><br>Choose a quick action or type your question below!",
        zeroai_input_ph: "Ask about MMO evasion, OCR, pricing plans...",

        // Footer
        footer_text_1: "<strong>ZeroPDF Studio</strong> • 100% Client-Side WebAssembly Architecture.",
        footer_text_2: "Absolute Privacy • Zero Intermediate Servers • Zero Telemetry Collection"
    },

    zh: {
        // Brand & Header
        brand_tag: "v2.5 OTA WASM",
        download_desktop_btn: "下载客户端 (.EXE)",
        pro_unlock_btn: "升级专业版 (299k VND)",
        zk_badge_text: "零知识架构 • 100%离线",
        lang_name: "中文 (简体)",
        pwa_install_btn: "安装应用",
        affiliate_nav_btn: "推广佣金 30%",

        // Hero
        hero_badge: "2026全能办公套件 & 短视频MMO引擎",
        hero_title: "超强PDF处理套件 & 短视频脱敏二创引擎",
        hero_sub: "零知识安全架构：100%数据直接在您的设备内存/GPU处理，0字节发送到外部服务器，绝对隐私保障。",

        // Bento Tabs
        tab_merge: "合并PDF",
        tab_split: "拆分旋转",
        tab_img2pdf: "图片转PDF",
        tab_compress: "智能压缩",
        tab_upscale: "✨ 4K超分辨率",
        tab_video: "🎬 去水印超清下载",
        tab_batch: "批量工作台",
        tab_bg_ocr: "AI抠图与文字识别",

        // Battle Slider
        battle_badge: "实测对比 • 短视频算法脱敏前后效果",
        battle_title: "直观对比：原视频 vs ZeroStudio处理后",
        battle_sub: "左右拖动滑块查看实战差异：从含有中文字幕与角标、面临限流的视频，瞬间转变为高清9:16微虚化、去水印并随时能够爆量的优质视频！",
        btn_split_50: "50 / 50 平衡",
        btn_split_before: "100% 原视频",
        btn_split_after: "100% ZeroStudio",
        btn_split_radar: "雷达自动扫描",
        hud_before_title: "处理前 (原始视频)",
        hud_after_title: "ZeroStudio处理后 (一键生成)",

        // Customer Reviews
        reviews_badge: "品质保障 • 1,480+ 五星好评",
        reviews_title: "创作者与用户如何评价ZeroStudio？",
        reviews_sub: "来自全球短视频出海创作者、财务主管、设计工作室与企业团队的真实评价与建议。",
        reviews_count_text: "1,482+ 满意评价 • 98.6% 推荐率",
        btn_write_review: "撰写您的评价",
        filter_all: "全部评价 (1,480+)",
        filter_5star: "5星好评 ⭐",
        filter_mmo: "短视频MMO创作者 🔥",
        filter_office: "办公与财务 📑",
        filter_mine: "您的评价 👤",
        review_modal_title: "评价与反馈 ZeroStudio",
        review_modal_sub: "您的宝贵建议将直接在主页公开展示，并同步呈报给核心技术开发团队！",
        review_input_name_lbl: "姓名 / 昵称：",
        review_input_name_ph: "例如：李伟 (出海TikTok运营)",
        review_input_role_lbl: "从事行业：",
        review_input_comment_lbl: "评价与改进建议：",
        review_input_comment_ph: "分享您在短视频重制、PDF智能压缩等方面的使用心得，或提出新功能建议...",
        btn_cancel: "取消",
        btn_submit_review: "立即提交评价",
        btn_load_more_reviews: "加载更多评价",

        // Affiliate Modal
        aff_modal_title: "ZEROSTUDIO分销合伙人计划",
        aff_modal_sub: "推广短视频与PDF神器 — 享受30% - 35%直接佣金分成",
        aff_rule_cpa: "<strong>真实付款CPA机制：</strong>被邀请人通过VietQR银行完成付费后，佣金即刻自动入账。杜绝虚假账号与刷单，保证100%实收真金白银。",
        aff_tier_pro_desc: "30% 佣金（客户立减10%仅需26.9万盾）",
        aff_tier_ultra_desc: "35% 佣金（客户立减10%仅需62.9万盾）",
        aff_ladder_title: "🏆 合伙人等级阶梯（累计成功付款单数）",
        aff_ladder_bronze: "🥉 新晋合伙人: 1 – 10 单 (25-30%)",
        aff_ladder_silver: "🥈 进阶精英: 11 – 50 单 (30-35%)",
        aff_ladder_gold: "🥇 顶级大师: > 50 单 (立奖100万盾)",
        aff_payout_note: "客户完成银行转账后系统自动绑定REF推广码。24小时内通过银行或Zalo快速结算。",
        aff_register_btn: "通过Zalo登记银行卡号",

        // Modals & Pricing Header
        pro_modal_title: "ZeroStudio Desktop Pro 专业版",
        pro_modal_sub: "释放电脑100%硬件算力 • 支持500+文件批量连发 • 无任何限制",

        // Founder 100-Slot Tracker
        tracker_status_founder: "创世者版特惠 • 限量首发100席",
        tracker_status_soldout: "🔒 100席创世者版已满额 • 现已启用官方标准价格",
        tracker_slots_prefix: "仅剩",
        tracker_slots_suffix: "席",
        tracker_slots_full: "已满额 100/100",
        tracker_explain_founder: "🔥 已认领 {slots}/100 席特惠。满100席后，系统将自动切换为官方标准价格。",
        tracker_explain_soldout: "⚠️ 100席创世者版优惠活动已截止，全平台现已恢复官方标准零售价。",

        // Pricing Cards - Free
        free_tier_badge: "网页免费版",
        free_tier_price: "0元",
        free_tier_period: "/ 永久免费",
        free_tier_desc: "适合个人日常处理轻量文档与短视频下载。",
        free_feat_1: "基础PDF合并与拆分",
        free_feat_2: "单视频无水印提取",
        free_feat_3: "每日限制3个视频",
        free_feat_4: "高级PDF压缩锁定",
        free_feat_5: "不支持批量流水线处理",
        free_tier_btn: "正在使用 (网页版)",

        // Pricing Cards - Pro
        pro_tier_badge: "创世者版 • 限量100席",
        pro_tier_badge_std: "官方正式版",
        pro_tier_title: "DESKTOP PRO 专业版",
        pro_tier_price: "299.000đ (~88元)",
        pro_tier_price_std: "599.000đ (~175元)",
        pro_tier_old_price: "599.000đ",
        pro_tier_period: "/ 首年",
        pro_tier_period_std: "/ 年",
        pro_tier_desc: "永久拥有v2.5版单设备授权 + 赠送365天算法OTA云端升级 (续费仅199k/年)。",
        pro_feat_1: "单视频无水印无限次极速提取",
        pro_feat_2: "<strong>智能PDF 3档预设：</strong> 体积骤降88% 满足发票与印刷要求",
        pro_feat_3: "<strong>字幕剥离与SRT转录：</strong> 多语言高精度语音转文本",
        pro_feat_4: "<strong>4K重制与角标去除：</strong> 抹除视频顽固水印",
        pro_feat_5: "<strong>永久买断v2.5：</strong> 包含12个月算法更新",
        btn_choose_pro: "选购专业版 (299k VND / ~88元)",
        btn_choose_pro_std: "选购专业版 (599k VND / ~175元)",

        // Pricing Cards - Ultra
        ultra_tier_badge: "创世者版 • 尊贵旗舰",
        ultra_tier_badge_std: "MMO大师旗舰版",
        ultra_tier_title: "ULTRA MMO MASTER 旗舰版",
        ultra_tier_price: "699.000đ (~200元)",
        ultra_tier_price_std: "1.490.000đ (~430元)",
        ultra_tier_old_price: "1.490.000đ",
        ultra_tier_period: "/ 首年",
        ultra_tier_period_std: "/ 年",
        ultra_tier_desc: "专为出海短视频矩阵、搬运MMO及批量创作工作室打造 (续费仅499k/年)。",
        ultra_feat_1: "<strong>批量流水线工作台：</strong> 后台自动排队运行500个视频 完工铃声提醒",
        ultra_feat_2: "<strong>AI 9:16双层智能裁切：</strong> 横屏秒变竖屏 边缘焦散微虚化",
        ultra_feat_3: "<strong>音频变频防重混淆：</strong> 随机微调音频基频避开指纹查重",
        ultra_feat_4: "<strong>频道爆款超级爬虫：</strong> 按播放量抓取整个YouTube/Reels/TikTok频道",
        ultra_feat_5: "<strong>硬字幕与旧Logo去除：</strong> 1键清除中文硬字幕与Logo",
        ultra_feat_6: "<strong>双设备永久授权 (台式机+笔记本)：</strong> 永久v2.5 + 365天算法维护",
        btn_choose_ultra: "选购旗舰版 (699k VND / ~200元)",
        btn_choose_ultra_std: "选购旗舰版 (1.490k VND / ~430元)",

        // Transparency Banner
        transparency_title: "创世者版限量透明承诺 (仅限首批100席)",
        transparency_bullet_1: "• <strong>永久买断当前版本：</strong> 您将永久拥有安装在个人设备上的当前ZeroStudio全部功能，绝无到期锁定软件风险。",
        transparency_bullet_2: "• <strong>365天持续算法更新：</strong> 免费获得1年应对TikTok、Facebook Reels与YouTube最新版权查重规则的算法补丁。",
        transparency_bullet_3: "• <strong>低门槛优惠续约：</strong> 365天后，您可以继续永久免费使用v2.5已激活版本，或按超低老客户价续约新算法 <strong>199k/年 (专业版)</strong> 或 <strong>499k/年 (旗舰版)</strong>。绝不虚标100%永久过审，真诚携手持续钻研算法。",

        // License Key Deck
        license_have_key: "已有专业版或旗舰版激活码？",
        license_input_ph: "输入授权码：ZERO-PRO-... 或 ZERO-ULTRA-...",
        license_activate_btn: "立即激活",

        // VietQR Checkout
        checkout_back_btn: "返回价格表",
        checkout_secure_tag: "VIETQR金融安全 • 自动秒发授权码",
        checkout_qr_instruction: "打开手机银行App或电子钱包扫描VietQR二维码自动转账：",
        checkout_bank_name: "越南MB Bank银行",
        checkout_acc_name_lbl: "收款人：",
        checkout_acc_num_lbl: "银行账号：",
        checkout_amount_lbl: "应付金额：",
        checkout_memo_lbl: "转账附言 (必须严格一致)：",
        checkout_memo_note: "⚠️ 请务必填写正确的转账附言，以便银行网关毫秒级自动给您签发授权码。",
        checkout_btn_confirm_paid: "我已转账 • 立即获取激活码",
        checkout_support_contact: "24小时专属人工客服支持 (Zalo Admin)：",

        // License Success
        success_title: "转账核验成功！",
        success_desc: "感谢您升级ZeroStudio专业版！授权激活码已成功签名并自动在此设备激活！",
        success_key_lbl: "您的专属激活码：",
        success_btn_copy: "复制激活码",
        success_btn_start: "立即开启专业版",

        // Common Tool Actions & Dropzones
        stage_drop_pdf: "拖拽PDF文件到此处",
        stage_drop_pdf_sub: "或点击按钮从电脑中选择多个文件",
        btn_choose_pdf: "选择PDF文件",
        btn_clear_all: "清空全部",
        btn_merge_download: "立即合并并下载",

        split_title: "选择需要拆分或旋转的PDF文件",
        split_sub: "自动生成每一页的缩略图矩阵供您直观挑选",
        btn_select_all: "全选",
        btn_deselect_all: "取消全选",
        btn_rotate_90: "🔄 旋转 90°",
        btn_export_split: "导出所选页面",

        img2pdf_title: "拖拽JPG / PNG图片到此处",
        img2pdf_sub: "批量打包多张图片生成高清晰度PDF文档",
        btn_choose_img: "选择图片文件",
        btn_export_pdf: "导出PDF文件",

        upscale_title: "拖拽需要4K超分辨率修复的图片到此处",
        upscale_sub: "利用WebAssembly AI进行噪点消除、纹理重建与2X/4X无损放大",
        btn_run_upscale: "立即运行AI放大",
        btn_change_img: "更换图片",

        video_downloader_title: "超强无水印短视频提取器",
        video_url_ph: "粘贴TikTok、Facebook Reels、YouTube Shorts链接...",
        btn_extract_video: "立即解析视频",
        video_mmo_title: "短视频二创去重与合规重制引擎",
        crop_916_lbl: "AI双层9:16画幅转换 (背景焦散虚化)",
        audio_pitch_lbl: "音频微频抖动随机混淆 (Randomizer)",
        remove_sub_lbl: "1键擦除中文硬字幕与角标Logo",
        batch_stage_title: "批量自动化处理中心",
        btn_start_batch: "开始批量流水线处理",

        // ZeroAI Chatbot
        zeroai_trigger_title: "AI 智能助理 24/7",
        zeroai_trigger_tag: "即时咨询",
        zeroai_title: "ZeroAI 专属智能助理",
        zeroai_subtitle: "短视频脱敏二创与AI工作室专家",
        zeroai_welcome: "您好！我是 <strong>ZeroAI Specialist</strong> – ZeroStudio您的全天候专属技术顾问。<br><br>我可以为您提供即时协助：<br>• <strong>短视频二创过审方案</strong>（双层9:16、音频微频扰动、一键抹字擦标）。<br>• <strong>AI智能人像抠图</strong>（证件照、白底签证照超清边缘羽化）。<br>• <strong>AI中越双语OCR扫描</strong>（高精度拍照识别并导出Word）。<br>• <strong>版本选购与授权激活指引</strong>（专业版299k与旗舰版699k对比）。<br><br>请点击上方快捷选项或在下方输入您的疑问！",
        zeroai_input_ph: "咨询短视频去重、抠图、OCR或价格...",

        // Footer
        footer_text_1: "<strong>ZeroPDF Studio</strong> • 100%客户端WebAssembly原生架构。",
        footer_text_2: "绝对隐私 • 零中转服务器 • 不收集任何用户数据"
    },

    ja: {
        // Brand & Header
        brand_tag: "v2.5 OTA WASM",
        download_desktop_btn: "デスクトップ版 (.EXE)",
        pro_unlock_btn: "Proにアップグレード",
        zk_badge_text: "完全オフライン • ゼロナレッジ",
        lang_name: "日本語",
        pwa_install_btn: "アプリをインストール",
        affiliate_nav_btn: "アフィリエイト30%",

        // Hero
        hero_badge: "2026 最新PDFツール & AI動画編集スタジオ",
        hero_title: "次世代 PDF & AI動画自動リマスター",
        hero_sub: "完全ゼロナレッジ技術：全データはお使いの端末のRAM/GPUで100%処理され、外部サーバーへは0バイトも送信されません。",

        // Bento Tabs
        tab_merge: "PDF結合",
        tab_split: "分割・抽出",
        tab_img2pdf: "画像PDF化",
        tab_compress: "スマート圧縮",
        tab_upscale: "✨ 4K超解像",
        tab_video: "🎬 ロゴなし動画抽出",
        tab_batch: "一括バッチ処理",
        tab_bg_ocr: "AI背景切り抜き&OCR",

        // Battle Slider
        battle_badge: "実証テスト • AIアルゴリズム判定の前後比較",
        battle_title: "ビジュアル比較：元動画 vs ZeroStudio処理後",
        battle_sub: "スライダーを左右に動かして実際の効果をご確認ください。透かしや字幕のある動画が、一瞬で超高画質な9:16縦型動画へ生まれ変わります！",
        btn_split_50: "50 / 50 分割",
        btn_split_before: "100% 元動画",
        btn_split_after: "100% ZeroStudio",
        btn_split_radar: "レーダー自動スキャン",
        hud_before_title: "処理前 (オリジナル動画)",
        hud_after_title: "ZEROSTUDIO処理後 (1クリック)",

        // Customer Reviews
        reviews_badge: "実績と信頼 • 1,480件以上の高評価",
        reviews_title: "ZeroStudioをご利用中のお客様の声",
        reviews_sub: "世界中の動画クリエイター、経理責任者、制作スタジオからの実際のレビューをご紹介します。",
        reviews_count_text: "1,482件以上の満足レビュー • 推奨度 98.6%",
        btn_write_review: "レビューを投稿する",
        filter_all: "すべてのレビュー (1,480+)",
        filter_5star: "★5つ評価 ⭐",
        filter_mmo: "動画クリエイター 🔥",
        filter_office: "オフィス・経理業務 📑",
        filter_mine: "あなたの投稿 👤",
        review_modal_title: "ZeroStudio レビュー＆ご要望",
        review_modal_sub: "いただいたご意見はトップページに掲載され、開発チームへ直接届けられます！",
        review_input_name_lbl: "お名前 / ニックネーム：",
        review_input_name_ph: "例：佐藤 健（動画マーケター）",
        review_input_role_lbl: "ご職業・分野：",
        review_input_comment_lbl: "ご感想・ご要望：",
        review_input_comment_ph: "動画処理やPDF圧縮のご感想、追加してほしい機能などをご記入ください...",
        btn_cancel: "キャンセル",
        btn_submit_review: "レビューを送信",
        btn_load_more_reviews: "さらにレビューを読み込む",

        // Affiliate Modal
        aff_modal_title: "ZEROSTUDIO パートナープログラム",
        aff_modal_sub: "高機能動画・PDFツールを紹介して30%〜35%の報酬を獲得",
        aff_rule_cpa: "<strong>実売上CPA方式：</strong>紹介された顧客がVietQR銀行振込で決済を完了した時点で即座に報酬が確定します。不正・ダミーアカウントは100%除外。",
        aff_tier_pro_desc: "30% 報酬（紹介された顧客は10%割引）",
        aff_tier_ultra_desc: "35% 報酬（紹介された顧客は10%割引）",
        aff_ladder_title: "🏆 パートナーランク制度（成約件数に応じた昇格）",
        aff_ladder_bronze: "🥉 ブロンズ: 1〜10件 (25-30%)",
        aff_ladder_silver: "🥈 シルバー: 11〜50件 (30-35%)",
        aff_ladder_gold: "🥇 ゴールドマスター: 50件超 (ボーナス100万VND)",
        aff_payout_note: "銀行振込が確認され次第REFコードが自動確定。24時間以内に銀行口座・Zaloへ迅速送金。",
        aff_register_btn: "Zaloで振込先口座を登録",

        // Modals & Pricing Header
        pro_modal_title: "ZeroStudio Desktop Pro",
        pro_modal_sub: "ハードウェア性能を100%解放 • 500ファイル以上の高速バッチ処理 • 制限なし",

        // Founder 100-Slot Tracker
        tracker_status_founder: "創設者版特典 • 先着100枠限定",
        tracker_status_soldout: "🔒 創設者版100枠完売 • 通常価格適用中",
        tracker_slots_prefix: "残り",
        tracker_slots_suffix: "枠",
        tracker_slots_full: "完売 100/100",
        tracker_explain_founder: "🔥 登録済み {slots}/100 枠。100枠満了後、自動的に通常価格へ切り替わります。",
        tracker_explain_soldout: "⚠️ 先着100枠の創設者優待枠は終了しました。現在は正規通常価格が適用されています。",

        // Pricing Cards - Free
        free_tier_badge: "WEB FREE",
        free_tier_price: "0円",
        free_tier_period: "/ 永久無料",
        free_tier_desc: "日常的な軽量PDF処理や動画ダウンロードに最適。",
        free_feat_1: "基本的なPDF結合・分割",
        free_feat_2: "単一動画のロゴなし抽出",
        free_feat_3: "1日3動画まで",
        free_feat_4: "高度なPDF圧縮は制限",
        free_feat_5: "バッチ一括処理は非対応",
        free_tier_btn: "利用中 (Web版)",

        // Pricing Cards - Pro
        pro_tier_badge: "創設者版 • 先着100枠",
        pro_tier_badge_std: "正規スタンダード版",
        pro_tier_title: "DESKTOP PRO",
        pro_tier_price: "299.000đ (~1,800円)",
        pro_tier_price_std: "599.000đ (~3,600円)",
        pro_tier_old_price: "599.000đ",
        pro_tier_period: "/ 初年度",
        pro_tier_period_std: "/ 年",
        pro_tier_desc: "1台の端末でv2.5を永久保有 + 365日間のアルゴリズムOTAアップデート付属 (更新は年199k)。",
        pro_feat_1: "透かしなし単一動画抽出（無制限）",
        pro_feat_2: "<strong>スマートPDF 3プリセット：</strong> 容量最大88%削減 印刷・電子申告対応",
        pro_feat_3: "<strong>字幕抽出＆SRT変換：</strong> 高精度多言語音声認識",
        pro_feat_4: "<strong>4Kリマスター＆透かし消去：</strong> 頑固なロゴを自動除去",
        pro_feat_5: "<strong>v2.5永久ライセンス：</strong> 12ヶ月のアルゴリズム更新付属",
        btn_choose_pro: "Proプランを購入 (299k VND / ~1,800円)",
        btn_choose_pro_std: "Proプランを購入 (599k VND / ~3,600円)",

        // Pricing Cards - Ultra
        ultra_tier_badge: "創設者版 • 最上位プラン",
        ultra_tier_badge_std: "MMOマスター正規版",
        ultra_tier_title: "ULTRA MMO MASTER",
        ultra_tier_price: "699.000đ (~4,200円)",
        ultra_tier_price_std: "1.490.000đ (~9,000円)",
        ultra_tier_old_price: "1.490.000đ",
        ultra_tier_period: "/ 初年度",
        ultra_tier_period_std: "/ 年",
        ultra_tier_desc: "大量動画投稿クリエイター＆スタジオ向け（更新は年499k）。",
        ultra_feat_1: "<strong>一括バッチワークベンチ：</strong> 500本自動処理・完了通知音",
        ultra_feat_2: "<strong>AI 9:16デュアルレイヤー：</strong> 横動画を縦動画へ変換（背景ぼかし）",
        ultra_feat_3: "<strong>オーディオ周波数ランダマイザー：</strong> 音声指紋の検知を低減",
        ultra_feat_4: "<strong>スーパークローラー：</strong> 再生数フィルターでチャンネル丸ごと収集",
        ultra_feat_5: "<strong>中国語字幕＆ロゴ除去：</strong> ワンクリックで文字を自動消去",
        ultra_feat_6: "<strong>2台永久ライセンス（PC+ノート）：</strong> 永久v2.5 + 365日更新",
        btn_choose_ultra: "Ultraプランを購入 (699k VND / ~4,200円)",
        btn_choose_ultra_std: "Ultraプランを購入 (1.490k VND / ~9,000円)",

        // Transparency Banner
        transparency_title: "創設者版の透明性に関するお約束（先着100枠限定）" ,
        transparency_bullet_1: "• <strong>現在のバージョンの永久保有：</strong> ご自身の端末にインストールした現行機能は期限切れでロックされることなく永久にご利用いただけます。",
        transparency_bullet_2: "• <strong>365日間のアルゴリズム更新：</strong> TikTok、Meta Reels、YouTubeの仕様変更に対応する最新アルゴリズムを1年間無料提供。",
        transparency_bullet_3: "• <strong>優遇更新ポリシー：</strong> 1年経過後もv2.5はそのまま無料でお使いいただけます。新アルゴリズムが必要な場合のみ、特別優遇価格 <strong>年199k (Pro)</strong> / <strong>年499k (Ultra)</strong> で更新可能です。",

        // License Key Deck
        license_have_key: "すでにライセンスキーをお持ちですか？",
        license_input_ph: "ライセンスキーを入力：ZERO-PRO-... または ZERO-ULTRA-...",
        license_activate_btn: "今すぐ有効化",

        // VietQR Checkout
        checkout_back_btn: "価格表に戻る",
        checkout_secure_tag: "VIETQRセキュリティ • ライセンス即時発行",
        checkout_qr_instruction: "銀行アプリまたは電子ウォレットでVietQRコードをスキャンしてお支払いください：",
        checkout_bank_name: "ベトナム MB Bank",
        checkout_acc_name_lbl: "口座名義：",
        checkout_acc_num_lbl: "口座番号：",
        checkout_amount_lbl: "お支払い金額：",
        checkout_memo_lbl: "送金メモ（必須・変更不可）：",
        checkout_memo_note: "⚠️ 上記の送金メモを正確に入力してください。銀行APIにより自動でライセンスが発行されます。",
        checkout_btn_confirm_paid: "送金完了 • ライセンスキーを受け取る",
        checkout_support_contact: "24時間対応 Zalo Admin サポート：",

        // License Success
        success_title: "お支払いが確認されました！",
        success_desc: "ZeroStudio Proへのアップグレードありがとうございます！ライセンスキーが発行され、自動で有効化されました。",
        success_key_lbl: "発行されたライセンスキー：",
        success_btn_copy: "キーをコピー",
        success_btn_start: "今すぐProを利用する",

        // Common Tool Actions & Dropzones
        stage_drop_pdf: "ここにPDFファイルをドラッグ＆ドロップ",
        stage_drop_pdf_sub: "またはお使いのパソコンから複数のファイルを選択",
        btn_choose_pdf: "PDFファイルを選択",
        btn_clear_all: "すべてクリア",
        btn_merge_download: "結合して今すぐダウンロード",

        split_title: "分割・ページ抽出するPDFファイルを選択",
        split_sub: "全ページのサムネイルを一覧表示し、直感的に選択できます",
        btn_select_all: "すべて選択",
        btn_deselect_all: "選択解除",
        btn_rotate_90: "🔄 90°回転",
        btn_export_split: "選択したページを出力",

        img2pdf_title: "ここにJPG / PNG画像をドラッグ＆ドロップ",
        img2pdf_sub: "複数画像をまとめて高画質なPDFにパッケージ化",
        btn_choose_img: "画像ファイルを選択",
        btn_export_pdf: "PDFを出力",

        upscale_title: "4K超解像処理する画像をドラッグ＆ドロップ",
        upscale_sub: "WebAssembly AIでノイズを除去し、2倍/4倍に高画質拡大",
        btn_run_upscale: "AI超解像を実行",
        btn_change_img: "画像を変更",

        video_downloader_title: "透かしなし動画高速ダウンローダー",
        video_url_ph: "TikTok、Facebook Reels、YouTube Shortsのリンクを貼り付け...",
        btn_extract_video: "動画を抽出する",
        video_mmo_title: "短動画リマスター＆重複防止エンジン",
        crop_916_lbl: "AI 9:16 デュアルレイヤー（背景ぼかし）",
        audio_pitch_lbl: "音声微周波ランダマイザー（検知回避）",
        remove_sub_lbl: "ワンクリック中国語字幕＆ロゴ除去",
        batch_stage_title: "一括バッチ処理スタジオ",
        btn_start_batch: "バッチ処理を開始",

        // ZeroAI Chatbot
        zeroai_trigger_title: "AI アシスタント 24/7",
        zeroai_trigger_tag: "即時サポート",
        zeroai_title: "ZeroAI Specialist 24/7",
        zeroai_subtitle: "動画アルゴリズム & AIスタジオ専門アドバイザー",
        zeroai_welcome: "こんにちは！<strong>ZeroAI Specialist</strong> です。<br><br>以下のご相談にリアルタイムでお応えします：<br>• <strong>動画アルゴリズム対策</strong>（9:16画角変換、音声微調整、透かし除去）。<br>• <strong>AI背景切り抜き</strong>（証明写真やパスポート写真の高精度処理）。<br>• <strong>AI高精度OCR</strong>（画像・書類からテキスト抽出）。<br>• <strong>プラン比較＆ライセンス有効化</strong>（Pro 299k / Ultra 699k）。<br><br>ご質問やお困りの点はお気軽にお尋ねください！",
        zeroai_input_ph: "動画処理、OCR、料金プランについて質問...",

        // Footer
        footer_text_1: "<strong>ZeroPDF Studio</strong> • 100%クライアントサイドWebAssemblyアーキテクチャ。",
        footer_text_2: "完全なプライバシー • 中継サーバーなし • 個人情報収集ゼロ"
    }
};

const LANG_CONFIG = {
    vi: { code: 'VI', flag: '🇻🇳', name: 'Tiếng Việt' },
    en: { code: 'EN', flag: '🇺🇸', name: 'English' },
    zh: { code: 'ZH', flag: '🇨🇳', name: '中文' },
    ja: { code: 'JA', flag: '🇯🇵', name: '日本語' }
};

let currentAppLanguage = 'vi';

function getAppLanguage() {
    let saved = null;
    try { saved = localStorage.getItem('zerostudio_lang'); } catch (_) {}
    if (saved && TRANSLATIONS[saved]) return saved;
    return 'vi';
}

function setAppLanguage(lang, silent = false) {
    if (!TRANSLATIONS[lang]) lang = 'vi';
    currentAppLanguage = lang;
    window.currentAppLanguage = lang;
    try { localStorage.setItem('zerostudio_lang', lang); } catch (_) {}

    const dict = TRANSLATIONS[lang];

    // 1. Update elements with [data-i18n]
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key] !== undefined) {
            el.innerHTML = dict[key];
        }
    });

    // 2. Update placeholders with [data-i18n-ph]
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        if (dict[key] !== undefined) {
            el.placeholder = dict[key];
        }
    });

    // 3. Update titles with [data-i18n-title]
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
        const key = el.getAttribute('data-i18n-title');
        if (dict[key] !== undefined) {
            el.title = dict[key];
        }
    });

    // 4. Update Header Dropdown Button
    const flagEl = document.getElementById('current-lang-flag');
    const codeEl = document.getElementById('current-lang-code');
    const cfg = LANG_CONFIG[lang] || LANG_CONFIG['vi'];
    if (flagEl) flagEl.textContent = cfg.flag;
    if (codeEl) codeEl.textContent = cfg.code;

    // 5. Update Active Class in Dropdown Menu
    document.querySelectorAll('.lang-item').forEach(item => {
        const itemLang = item.getAttribute('data-lang');
        if (itemLang === lang) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    // 6. Close Dropdown
    const popover = document.getElementById('lang-menu-popover');
    if (popover) popover.classList.remove('open');

    // 7. Re-render dynamic components in the new language
    if (typeof window.renderFounderSlotState === 'function') {
        window.renderFounderSlotState();
    }

    // 8. Dispatch Event for external listeners
    window.dispatchEvent(new CustomEvent('zerostudio:lang_changed', { detail: { lang, dict } }));

    if (!silent && typeof showToast === 'function') {
        const toastMsg = {
            vi: 'Đã chuyển đổi sang Tiếng Việt!',
            en: 'Switched language to English!',
            zh: '已切换为简体中文！',
            ja: '日本語に切り替えました！'
        };
        showToast(toastMsg[lang] || 'Language updated!', 'info');
    }
}

window.TRANSLATIONS = TRANSLATIONS;
window.setAppLanguage = setAppLanguage;
window.getAppLanguage = getAppLanguage;

function toggleLangDropdown(event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    const popover = document.getElementById('lang-menu-popover');
    if (popover) {
        popover.classList.toggle('open');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', (e) => {
    const wrap = document.getElementById('lang-dropdown-wrap');
    const popover = document.getElementById('lang-menu-popover');
    if (wrap && popover && !wrap.contains(e.target)) {
        popover.classList.remove('open');
    }
});

// Initialize on script load
document.addEventListener('DOMContentLoaded', () => {
    const initialLang = getAppLanguage();
    setAppLanguage(initialLang, true);
});

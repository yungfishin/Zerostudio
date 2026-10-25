import os

PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html"
with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Head Tags
old_head = """    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZeroPDF • Cybernetic Zero-Knowledge PDF & AI Studio</title>
    <meta name="description" content="Nền tảng xử lý PDF & AI Phóng to 4K bảo mật tuyệt đối kiến trúc Bento Grid & WebAssembly 100% Client-Side.">"""

new_head = """    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>ZeroStudio Pro • Siêu Bộ Công Cụ Video MMO & Xử Lý PDF 100% Offline</title>
    <meta name="description" content="Nền tảng xử lý Video MMO lách bản quyền, nén & chuyển đổi PDF 100% Zero-Knowledge bảo mật tuyệt đối trực tiếp trên RAM máy tính. Không gửi 1 Byte ra Internet.">
    
    <!-- PWA & Mobile Web App Meta -->
    <meta name="theme-color" content="#0a0e1a">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="ZeroStudio">
    <link rel="manifest" href="./manifest.json">
    <link rel="icon" type="image/png" href="./assets/icons/favicon.png">
    <link rel="apple-touch-icon" href="./assets/icons/icon-192.png">

    <!-- Open Graph / Facebook / Zalo Preview -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://zerostu.netlify.app/">
    <meta property="og:title" content="ZeroStudio Pro • Siêu Bộ Công Cụ Video MMO & Xử Lý PDF 100% Offline">
    <meta property="og:description" content="Xử lý 100% tại RAM máy tính, 0 Byte gửi ra ngoài. Tải video Douyin/TikTok 1080p không logo, đổi pitch âm thanh lách bản quyền, nén PDF giảm 88% chuẩn in ấn.">
    <meta property="og:image" content="https://zerostu.netlify.app/assets/images/zerostudio-og-preview.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="ZeroStudio Pro">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="https://zerostu.netlify.app/">
    <meta name="twitter:title" content="ZeroStudio Pro • Video MMO & Xử Lý PDF 100% Offline">
    <meta name="twitter:description" content="Xử lý 100% tại RAM máy tính, 0 Byte gửi ra ngoài. An toàn bảo mật tuyệt đối.">
    <meta name="twitter:image" content="https://zerostu.netlify.app/assets/images/zerostudio-og-preview.png">"""

assert old_head in content, "old_head not found"
content = content.replace(old_head, new_head, 1)

# 2. Navbar buttons
old_nav = """        <div class="header-right-deck">
            <!-- Multi-Language Dropdown Selector -->"""

new_nav = """        <div class="header-right-deck">
            <!-- PWA Install 1-Click Button -->
            <button id="btn-pwa-install" class="btn-outline pwa-install-btn" onclick="triggerPwaInstall()" style="border-color: rgba(16, 185, 129, 0.4); color: #34d399; background: rgba(16, 185, 129, 0.08); padding: 6px 12px; font-size: 12px; border-radius: 999px; cursor: pointer; display: none; align-items: center; gap: 5px;" title="Cài đặt ZeroStudio vào máy tính hoặc điện thoại dùng như App">
                <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" width="14" height="14"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                <span data-i18n="pwa_install_btn">Cài App</span>
            </button>

            <!-- Affiliate 30% Partner Button -->
            <button id="btn-affiliate-nav" class="btn-outline" onclick="openAffiliateModal()" style="border-color: rgba(236, 72, 153, 0.4); color: #f472b6; background: rgba(236, 72, 153, 0.08); padding: 6px 12px; font-size: 12px; border-radius: 999px; cursor: pointer; display: inline-flex; align-items: center; gap: 5px;" title="Đăng ký nhận mã giới thiệu và hưởng 30% hoa hồng">
                <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" width="14" height="14"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span data-i18n="affiliate_nav_btn">Hoa Hồng 30%</span>
            </button>

            <!-- Multi-Language Dropdown Selector -->"""

assert old_nav in content, "old_nav not found"
content = content.replace(old_nav, new_nav, 1)

# 3. Affiliate discount banner in pricing
old_pricing = """                <!-- Bento Pricing Comparison (3 Tiers: Free - Pro - Ultra) -->
                <div class="pro-pricing-grid">"""

new_pricing = """                <!-- Affiliate Referral Discount Banner (Dynamic) -->
                <div class="affiliate-discount-banner" id="affiliate-discount-banner" style="display: none; background: linear-gradient(135deg, rgba(236, 72, 153, 0.15), rgba(168, 85, 247, 0.15)); border: 1px solid rgba(236, 72, 153, 0.45); border-radius: 14px; padding: 0.85rem 1.25rem; margin-bottom: 1.25rem; text-align: left; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.15);">
                    <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap;">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 1.5rem;">🎉</span>
                            <div>
                                <div style="font-weight: 800; color: #f472b6; font-size: 0.95rem;">ƯU ĐÃI ĐỐI TÁC: GIẢM 10% TOÀN BỘ CÁC GÓI!</div>
                                <div style="font-size: 0.82rem; color: #cbd5e1; margin-top: 2px;">
                                    Đang kích hoạt mã giới thiệu từ đối tác: <strong id="affiliate-active-code" style="color: #fbbf24; font-family: 'JetBrains Mono', monospace;">...</strong>
                                </div>
                            </div>
                        </div>
                        <span style="padding: 4px 10px; background: rgba(236, 72, 153, 0.2); border: 1px solid #ec4899; color: #f472b6; border-radius: 999px; font-size: 0.75rem; font-weight: 800;">-10% TỰ ĐỘNG</span>
                    </div>
                </div>

                <!-- Bento Pricing Comparison (3 Tiers: Free - Pro - Ultra) -->
                <div class="pro-pricing-grid">"""

assert old_pricing in content, "old_pricing not found"
content = content.replace(old_pricing, new_pricing, 1)

# 4. Checkout discount pill in VietQR
old_checkout = """                    <!-- Right: Info Details & Copy Pills -->
                    <div class="vietqr-info-box">
                        <div class="checkout-price-callout">"""

new_checkout = """                    <!-- Right: Info Details & Copy Pills -->
                    <div class="vietqr-info-box">
                        <div class="checkout-discount-pill" id="checkout-discount-pill" style="display: none; background: rgba(236, 72, 153, 0.15); border: 1px dashed rgba(236, 72, 153, 0.55); padding: 8px 12px; border-radius: 10px; margin-bottom: 12px; font-size: 0.82rem; color: #f472b6; font-weight: 600; text-align: left;">
                            🎁 Đã áp dụng mã đối tác <span id="checkout-ref-tag" style="font-weight: 800; color: #fbbf24; font-family: 'JetBrains Mono', monospace;">...</span>: Giảm ngay 10%!
                        </div>

                        <div class="checkout-price-callout">"""

assert old_checkout in content, "old_checkout not found"
content = content.replace(old_checkout, new_checkout, 1)

# 5. Affiliate Modal
old_toast = """    <!-- Toast Container -->
    <div class="toast-deck" id="toast-container"></div>"""

new_toast = """    <!-- MODAL: ZEROSTUDIO AFFILIATE PARTNER PROGRAM (30% COMMISSION) -->
    <div class="laser-modal" id="affiliate-modal" style="display: none;">
        <div class="pro-hud-card" style="max-width: 650px;">
            <button class="modal-close-btn" onclick="closeAffiliateModal()">
                <svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>

            <div style="text-align: center; margin-bottom: 1.5rem;">
                <div style="width: 54px; height: 54px; margin: 0 auto 12px; border-radius: 16px; background: linear-gradient(135deg, rgba(236, 72, 153, 0.2), rgba(168, 85, 247, 0.2)); border: 1px solid rgba(236, 72, 153, 0.5); display: flex; align-items: center; justify-content: center; font-size: 26px; box-shadow: 0 0 25px rgba(236, 72, 153, 0.3);">
                    🎁
                </div>
                <h2 style="font-size: 1.55rem; font-weight: 800; color: #fff; letter-spacing: -0.02em;" data-i18n="aff_modal_title">CHƯƠNG TRÌNH ĐỐI TÁC ZEROSTUDIO</h2>
                <p style="color: #94a3b8; font-size: 0.88rem; margin-top: 6px;" data-i18n="aff_modal_sub">Lan tỏa siêu công cụ Video & PDF — Nhận 30% hoa hồng trực tiếp qua Ngân Hàng / Zalo</p>
            </div>

            <!-- Commission Rate Bento Cards -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 1.5rem;">
                <div style="background: rgba(168, 85, 247, 0.08); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 14px; padding: 14px; text-align: center;">
                    <div style="font-size: 0.75rem; color: #c084fc; font-weight: 700; text-transform: uppercase;">Gói Desktop Pro</div>
                    <div style="font-size: 1.5rem; font-weight: 800; color: #e879f9; margin: 4px 0;">90.000đ</div>
                    <div style="font-size: 0.78rem; color: #94a3b8;">Hoa hồng 30% / đơn (Giá 299k)</div>
                </div>
                <div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 14px; padding: 14px; text-align: center;">
                    <div style="font-size: 0.75rem; color: #fbbf24; font-weight: 700; text-transform: uppercase;">Gói Ultra MMO Master</div>
                    <div style="font-size: 1.5rem; font-weight: 800; color: #f59e0b; margin: 4px 0;">210.000đ</div>
                    <div style="font-size: 0.78rem; color: #94a3b8;">Hoa hồng 30% / đơn (Giá 699k)</div>
                </div>
            </div>

            <!-- Custom Link Generator Box -->
            <div style="background: rgba(15, 23, 42, 0.75); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 18px; margin-bottom: 1.25rem;">
                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 8px;">
                    1. Nhập biệt danh / tên của bạn để tạo mã riêng:
                </label>
                <div style="display: flex; gap: 8px; margin-bottom: 14px;">
                    <input type="text" id="aff-nickname-input" placeholder="VD: TOPMMO, HIEU99, KETOAN..." style="flex: 1; background: rgba(0, 0, 0, 0.4); border: 1px solid rgba(236, 72, 153, 0.4); border-radius: 10px; padding: 10px 14px; color: #fff; font-size: 0.9rem; font-family: 'JetBrains Mono', monospace; text-transform: uppercase;" />
                    <button class="btn-glow-action" onclick="generateAffiliateLink()" style="border-radius: 10px; padding: 10px 18px; font-size: 0.85rem; background: linear-gradient(135deg, #ec4899, #a855f7); flex-shrink: 0;">
                        Tạo Link
                    </button>
                </div>

                <label style="display: block; font-size: 0.82rem; font-weight: 700; color: #cbd5e1; margin-bottom: 8px;">
                    2. Link giới thiệu độc quyền (Người mua được giảm 10%):
                </label>
                <div style="display: flex; gap: 8px; align-items: center; background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 10px; padding: 6px 10px;">
                    <input type="text" id="aff-link-output" readonly value="https://zerostu.netlify.app/?ref=PARTNER" style="flex: 1; background: transparent; border: none; color: #38bdf8; font-size: 0.85rem; font-family: 'JetBrains Mono', monospace; outline: none;" />
                    <button class="btn-outline" onclick="copyAffiliateLink()" style="border-radius: 8px; padding: 6px 14px; font-size: 0.8rem; border-color: rgba(56, 189, 248, 0.4); color: #38bdf8; flex-shrink: 0;">
                        Sao Chép Link
                    </button>
                </div>
            </div>

            <!-- How payout works & Hotline register -->
            <div style="padding: 12px 16px; border-radius: 12px; background: rgba(0, 104, 255, 0.08); border: 1px solid rgba(0, 104, 255, 0.25); display: flex; align-items: center; justify-content: space-between; gap: 12px;">
                <div style="font-size: 0.8rem; color: #94a3b8; line-height: 1.4; text-align: left;">
                    💳 <strong>Đối soát & Nhận hoa hồng:</strong><br>
                    Khách mua ghi kèm mã REF của bạn, tiền hoa hồng sẽ được Admin chuyển khoản ngay trong ngày qua STK của bạn.
                </div>
                <a href="https://zalo.me/0962876139" target="_blank" rel="noopener noreferrer" style="padding: 0.45rem 0.85rem; font-size: 0.8rem; background: #0068ff; color: #fff; font-weight: 700; border-radius: 8px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; flex-shrink: 0; box-shadow: 0 4px 12px rgba(0, 104, 255, 0.35);">
                    Đăng Ký STK Qua Zalo
                </a>
            </div>
        </div>
    </div>

    <!-- Toast Container -->
    <div class="toast-deck" id="toast-container"></div>"""

assert old_toast in content, "old_toast not found"
content = content.replace(old_toast, new_toast, 1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: index.html updated flawlessly with all 5 sections!")

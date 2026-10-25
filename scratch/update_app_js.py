import os

PATH = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\app.js"
with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update openVietQrCheckout
old_checkout = """window.openVietQrCheckout = function(tier = 'pro') {
    window.selectedTier = tier;
    currentOrderCode = Math.floor(1000 + Math.random() * 9000).toString();
    const isUltra = (tier === 'ultra');
    const amount = isUltra ? 699000 : 299000;
    const memo = isUltra ? `ZERO ULTRA ${currentOrderCode}` : `ZERO PRO ${currentOrderCode}`;

    const memoValEl = document.getElementById('order-memo-val');
    if (memoValEl) memoValEl.textContent = memo;

    const amountDisplay = document.getElementById('checkout-amount-display');
    if (amountDisplay) {
        amountDisplay.textContent = isUltra ? "699.000 VNĐ" : "299.000 VNĐ";
        amountDisplay.style.color = isUltra ? "#f59e0b" : "#6ee7b7";
    }"""

new_checkout = """window.openVietQrCheckout = function(tier = 'pro') {
    window.selectedTier = tier;
    currentOrderCode = Math.floor(1000 + Math.random() * 9000).toString();
    const isUltra = (tier === 'ultra');
    const baseAmount = isUltra ? 699000 : 299000;

    // Check active affiliate referral
    const activeRef = localStorage.getItem('zerostudio_ref');
    let amount = baseAmount;
    let memo = isUltra ? `ZERO ULTRA ${currentOrderCode}` : `ZERO PRO ${currentOrderCode}`;

    const discountPill = document.getElementById('checkout-discount-pill');
    const refTag = document.getElementById('checkout-ref-tag');

    if (activeRef) {
        // 10% Discount applied
        amount = Math.round(baseAmount * 0.9);
        memo = `${memo} REF-${activeRef.toUpperCase()}`;
        if (discountPill) discountPill.style.display = 'block';
        if (refTag) refTag.textContent = activeRef.toUpperCase();
    } else {
        if (discountPill) discountPill.style.display = 'none';
    }

    const memoValEl = document.getElementById('order-memo-val');
    if (memoValEl) memoValEl.textContent = memo;

    const amountDisplay = document.getElementById('checkout-amount-display');
    if (amountDisplay) {
        if (activeRef) {
            const formattedDisc = amount.toLocaleString('vi-VN') + " VNĐ";
            const formattedOld = baseAmount.toLocaleString('vi-VN') + " VNĐ";
            amountDisplay.innerHTML = `${formattedDisc} <span style="font-size: 0.85rem; text-decoration: line-through; color: #94a3b8; margin-left: 6px;">${formattedOld}</span>`;
        } else {
            amountDisplay.textContent = amount.toLocaleString('vi-VN') + " VNĐ";
        }
        amountDisplay.style.color = isUltra ? "#f59e0b" : "#6ee7b7";
    }"""

assert old_checkout in content, "old_checkout not found"
content = content.replace(old_checkout, new_checkout, 1)

# 2. Update confirmPaidAndGetLicense
old_confirm = """window.confirmPaidAndGetLicense = function() {
    showToast("Đang kết nối MB Bank kiểm tra biến động số dư...", "info");
    checkBankPaymentStatus(true);
};"""

new_confirm = """window.confirmPaidAndGetLicense = function() {
    showToast("Đang kết nối MB Bank kiểm tra biến động số dư...", "info");
    
    // Dispatch Instant Webhook & Order Record
    const memoValEl = document.getElementById('order-memo-val');
    const memo = memoValEl ? memoValEl.textContent.trim() : `ZERO PRO ${currentOrderCode}`;
    const activeRef = localStorage.getItem('zerostudio_ref') || '';
    const isUltra = (window.selectedTier === 'ultra');
    const amount = activeRef ? (isUltra ? 629000 : 269000) : (isUltra ? 699000 : 299000);

    if (typeof sendInstantNotification === 'function') {
        sendInstantNotification({
            eventType: 'PAYMENT_CONFIRM_INTENT',
            data: {
                order_code: currentOrderCode,
                tier: window.selectedTier || 'pro',
                amount: amount,
                memo: memo,
                ref: activeRef
            }
        });
    }

    checkBankPaymentStatus(true);
};"""

assert old_confirm in content, "old_confirm not found"
content = content.replace(old_confirm, new_confirm, 1)

# 3. Update submitCustomerReview notification
old_sub_hook = """    // 2. Post to Video Bridge for permanent disk storage
    try {
        fetch('http://127.0.0.1:8900/api/feedback', {"""

new_sub_hook = """    // Trigger instant real-time webhook notification
    if (typeof sendInstantNotification === 'function') {
        sendInstantNotification({
            eventType: 'REVIEW_SUBMITTED',
            data: {
                name: name,
                role: roleTitle,
                stars: modalSelectedStars,
                comment: comment,
                tier: activeTier
            }
        });
    }

    // 2. Post to Video Bridge for permanent disk storage
    try {
        fetch('http://127.0.0.1:8900/api/feedback', {"""

assert old_sub_hook in content, "old_sub_hook not found"
content = content.replace(old_sub_hook, new_sub_hook, 1)

# 4. Append PWA, Affiliate, and Notification Webhook engine at end of app.js
new_engines = """

// =========================================================================
// PILLAR 1: INSTANT PUSH NOTIFICATION WEBHOOK (TELEGRAM & GOOGLE SHEETS)
// =========================================================================
window.sendInstantNotification = async function({ eventType, data }) {
    console.log(`[INSTANT NOTIFICATION] Event: ${eventType}`, data);

    let messageText = '';
    if (eventType === 'PAYMENT_CONFIRM_INTENT') {
        const refInfo = data.ref ? ` (Qua mã REF: <b>${data.ref}</b>)` : '';
        messageText = `🔔 <b>ZeroStudio - ĐƠN HÀNG MỚI!</b>\\n` +
                      `📦 Gói: <b>${data.tier ? data.tier.toUpperCase() : 'PRO'}</b>\\n` +
                      `💵 Số tiền: <b>${Number(data.amount).toLocaleString('vi-VN')} VNĐ</b>\\n` +
                      `📝 Nội dung CK: <code>${data.memo}</code>${refInfo}\\n` +
                      `⏱ Thời gian: ${new Date().toLocaleTimeString('vi-VN')} ${new Date().toLocaleDateString('vi-VN')}`;
        
        // Also save to local Python bridge orders
        try {
            fetch('http://127.0.0.1:8900/api/orders', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            }).catch(() => {});
        } catch (_) {}

    } else if (eventType === 'REVIEW_SUBMITTED') {
        messageText = `⭐ <b>ZeroStudio - ĐÁNH GIÁ MỚI (${data.stars}★)</b>\\n` +
                      `👤 Khách hàng: <b>${data.name}</b> (${data.role})\\n` +
                      `💬 Nhận xét: <i>"${data.comment}"</i>\\n` +
                      `⏱ Thời gian: ${new Date().toLocaleTimeString('vi-VN')} ${new Date().toLocaleDateString('vi-VN')}`;

    } else if (eventType === 'AFFILIATE_SIGNUP') {
        messageText = `🎁 <b>ZeroStudio - ĐỐI TÁC MỚI ĐĂNG KÝ!</b>\\n` +
                      `🔗 Mã giới thiệu: <b>${data.refCode}</b>\\n` +
                      `🌐 Link: <code>https://zerostu.netlify.app/?ref=${data.refCode}</code>`;
    }

    // 1. Dispatch to Telegram Bot if configured
    const tgToken = localStorage.getItem('zerostudio_tg_token') || window.ZEROSTUDIO_TG_TOKEN;
    const tgChatId = localStorage.getItem('zerostudio_tg_chat_id') || window.ZEROSTUDIO_TG_CHAT_ID;
    if (tgToken && tgChatId) {
        try {
            fetch(`https://api.telegram.org/bot${tgToken}/sendMessage`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: tgChatId,
                    text: messageText,
                    parse_mode: 'HTML'
                })
            }).catch(e => console.warn('[TELEGRAM] Webhook failed:', e));
        } catch (e) {
            console.warn('[TELEGRAM] Error sending notification:', e);
        }
    }

    // 2. Dispatch to Custom Google Sheets / Webhook if configured
    const customWebhook = localStorage.getItem('zerostudio_custom_webhook') || window.ZEROSTUDIO_WEBHOOK_URL;
    if (customWebhook) {
        try {
            fetch(customWebhook, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ eventType, data, messageText, timestamp: Date.now() })
            }).catch(() => {});
        } catch (_) {}
    }
};

// =========================================================================
// PILLAR 3: PWA (PROGRESSIVE WEB APP) SERVICE WORKER & 1-CLICK INSTALL
// =========================================================================
let deferredPwaPrompt = null;

if ('serviceWorker' in navigator && (window.location.protocol.startsWith('http') || window.location.protocol.startsWith('https'))) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js')
            .then(reg => console.log('[PWA] Service Worker registered with scope:', reg.scope))
            .catch(err => console.log('[PWA] Service Worker registration failed:', err));
    });
}

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPwaPrompt = e;
    const pwaBtn = document.getElementById('btn-pwa-install');
    if (pwaBtn) pwaBtn.style.display = 'inline-flex';
});

window.triggerPwaInstall = async function() {
    if (!deferredPwaPrompt) {
        showToast("Để cài đặt trên Chrome/Edge: Bấm biểu tượng ⬇️ hoặc ➕ trên thanh địa chỉ duyệt web!", "info");
        return;
    }
    deferredPwaPrompt.prompt();
    const { outcome } = await deferredPwaPrompt.userChoice;
    if (outcome === 'accepted') {
        showToast("Đang cài đặt ZeroStudio vào máy của bạn...", "success");
    }
    deferredPwaPrompt = null;
    const pwaBtn = document.getElementById('btn-pwa-install');
    if (pwaBtn) pwaBtn.style.display = 'none';
};

window.addEventListener('appinstalled', () => {
    showToast("🎉 Cài đặt ứng dụng ZeroStudio thành công!", "success");
    const pwaBtn = document.getElementById('btn-pwa-install');
    if (pwaBtn) pwaBtn.style.display = 'none';
});

// =========================================================================
// PILLAR 4: AFFILIATE & REFERRAL ENGINE (30% COMMISSION / 10% DISCOUNT)
// =========================================================================
window.initAffiliateSystem = function() {
    try {
        const urlParams = new URLSearchParams(window.location.search);
        const refParam = urlParams.get('ref') || urlParams.get('aff') || urlParams.get('coupon');

        if (refParam) {
            const sanitized = refParam.trim().toUpperCase().replace(/[^A-Z0-9_-]/g, '').slice(0, 20);
            if (sanitized) {
                localStorage.setItem('zerostudio_ref', sanitized);
                console.log(`[AFFILIATE] Activated ref code: ${sanitized}`);
            }
        }

        const activeRef = localStorage.getItem('zerostudio_ref');
        const banner = document.getElementById('affiliate-discount-banner');
        const codeEl = document.getElementById('affiliate-active-code');

        if (activeRef) {
            if (banner) banner.style.display = 'block';
            if (codeEl) codeEl.textContent = activeRef;
            if (refParam) {
                setTimeout(() => {
                    showToast(`🎉 Đã kích hoạt mã ưu đãi ${activeRef}: Giảm 10% toàn bộ gói!`, 'success');
                }, 1200);
            }
        } else {
            if (banner) banner.style.display = 'none';
        }
    } catch (e) {
        console.warn('[AFFILIATE] Init error:', e);
    }
};

window.openAffiliateModal = function() {
    const modal = document.getElementById('affiliate-modal');
    if (modal) modal.style.display = 'flex';
    const myRef = localStorage.getItem('zerostudio_my_ref') || '';
    const input = document.getElementById('aff-nickname-input');
    const output = document.getElementById('aff-link-output');
    if (myRef) {
        if (input) input.value = myRef;
        if (output) output.value = `https://zerostu.netlify.app/?ref=${myRef}`;
    }
};

window.closeAffiliateModal = function() {
    const modal = document.getElementById('affiliate-modal');
    if (modal) modal.style.display = 'none';
};

window.generateAffiliateLink = function() {
    const input = document.getElementById('aff-nickname-input');
    let code = input ? input.value.trim().toUpperCase() : '';
    code = code.replace(/[^A-Z0-9_-]/g, '').slice(0, 20);
    if (!code) {
        showToast('Vui lòng nhập biệt danh (chữ cái hoặc số)!', 'error');
        return;
    }
    localStorage.setItem('zerostudio_my_ref', code);
    const link = `https://zerostu.netlify.app/?ref=${code}`;
    const output = document.getElementById('aff-link-output');
    if (output) output.value = link;

    if (typeof launchGoldConfetti === 'function') launchGoldConfetti();
    showToast(`🎉 Đã tạo link giới thiệu: ${code}! Nhận 30% hoa hồng mỗi đơn.`, 'success');

    if (typeof sendInstantNotification === 'function') {
        sendInstantNotification({
            eventType: 'AFFILIATE_SIGNUP',
            data: { refCode: code }
        });
    }
};

window.copyAffiliateLink = function() {
    const output = document.getElementById('aff-link-output');
    const link = output ? output.value.trim() : 'https://zerostu.netlify.app';
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(link).then(() => {
            showToast('✓ Đã sao chép link giới thiệu vào bộ nhớ tạm!', 'success');
        }).catch(() => {
            copyFallback(link);
        });
    } else {
        copyFallback(link);
    }
};

function copyFallback(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('✓ Đã sao chép link giới thiệu!', 'success');
}

// Auto Initialize Affiliate on Load
document.addEventListener('DOMContentLoaded', () => {
    initAffiliateSystem();
});
setTimeout(() => {
    initAffiliateSystem();
}, 600);
"""

content += new_engines

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: app.js updated flawlessly with all 4 Pillars!")

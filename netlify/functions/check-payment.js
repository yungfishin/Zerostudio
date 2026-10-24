/**
 * ZeroStudio Pro - Real-Time Bank Payment Verification Serverless Function
 * Verified against MB Bank transactions via SePAY API (https://sepay.vn)
 */
const https = require('https');

exports.handler = async function(event, context) {
    // Enable CORS for frontend API calls
    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
    };

    if (event.httpMethod === "OPTIONS") {
        return { statusCode: 200, headers, body: "" };
    }

    const params = event.queryStringParameters || {};
    let orderCode = params.order;

    if (!orderCode && event.body) {
        try {
            const parsedBody = JSON.parse(event.body);
            orderCode = parsedBody.order;
        } catch (e) {}
    }

    if (!orderCode) {
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({
                success: false,
                message: "Thiếu mã đơn hàng cần kiểm tra (order code)!"
            })
        };
    }

    // Sanitize order code (only numbers)
    const cleanDigits = orderCode.toString().replace(/[^0-9]/g, '');
    const sepayToken = process.env.SEPAY_API_TOKEN;

    // Check if SEPAY_API_TOKEN is set in Netlify Environment Variables
    if (!sepayToken) {
        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({
                success: true,
                paid: false,
                config_needed: true,
                orderCode: cleanDigits,
                message: "Chưa cấu hình SEPAY_API_TOKEN trên Netlify. Vui lòng cấu hình biến môi trường để kích hoạt đối soát MB Bank tự động."
            })
        };
    }

    try {
        const responseData = await fetchSepayTransactions(sepayToken);
        const transactions = responseData.transactions || responseData.data || [];

        // Check if any incoming transaction matches:
        // 1. amount_in >= 299,000 VND
        // 2. content includes 'ZERO' and the 4-digit order code
        const matched = transactions.find(tx => {
            const amountIn = parseFloat(tx.amount_in || tx.transferAmount || 0);
            const content = ((tx.transaction_content || tx.content || '') + ' ' + (tx.code || '')).toUpperCase();
            
            const targetPattern1 = `ZERO ${cleanDigits}`.toUpperCase();
            const targetPattern2 = `ZERO${cleanDigits}`.toUpperCase();
            const hasOrderCode = content.includes(targetPattern1) || content.includes(targetPattern2) || content.includes(cleanDigits);

            return amountIn >= 299000 && hasOrderCode;
        });

        if (matched) {
            // Transaction found in MB Bank! Generate authorized Pro License Key
            const randHex = Math.random().toString(36).substring(2, 6).toUpperCase();
            const licenseKey = `ZERO-PRO-${cleanDigits}-HIEU-${randHex}`;

            return {
                statusCode: 200,
                headers,
                body: JSON.stringify({
                    success: true,
                    paid: true,
                    transaction: {
                        id: matched.id,
                        amount: matched.amount_in || matched.transferAmount,
                        date: matched.transaction_date || matched.createdAt || new Date().toISOString()
                    },
                    licenseKey: licenseKey,
                    message: "Xác thực thành công: Đã nhận đủ 299.000đ từ tài khoản MB Bank."
                })
            };
        } else {
            // Not paid yet or bank hasn't updated
            return {
                statusCode: 200,
                headers,
                body: JSON.stringify({
                    success: true,
                    paid: false,
                    orderCode: cleanDigits,
                    message: `Chưa tìm thấy giao dịch chuyển khoản 299.000đ với nội dung 'ZERO ${cleanDigits}' trên MB Bank.`
                })
            };
        }
    } catch (err) {
        console.error("Lỗi khi kết nối SePAY API:", err);
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({
                success: false,
                error: err.message,
                message: "Lỗi kết nối tới cổng đối soát ngân hàng SePAY."
            })
        };
    }
};

/**
 * Helper to call SePAY User API over HTTPS
 */
function fetchSepayTransactions(token) {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'my.sepay.vn',
            path: '/userapi/transactions/list?limit=30',
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        };

        const req = https.request(options, (res) => {
            let rawData = '';
            res.on('data', chunk => rawData += chunk);
            res.on('end', () => {
                try {
                    const parsed = JSON.parse(rawData);
                    resolve(parsed);
                } catch (e) {
                    reject(new Error("Lỗi đọc phản hồi SePAY: " + rawData.substring(0, 150)));
                }
            });
        });

        req.on('error', (e) => reject(e));
        req.setTimeout(7000, () => {
            req.destroy();
            reject(new Error("Quá thời gian kết nối (Timeout 7s) tới SePAY"));
        });
        req.end();
    });
}

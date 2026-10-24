/**
 * ZeroStudio Pro - SePAY Webhook Endpoint
 * Receives instant HTTP POST when a transaction occurs on MB Bank
 */
exports.handler = async function(event, context) {
    const headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    };

    if (event.httpMethod !== "POST") {
        return {
            statusCode: 405,
            headers,
            body: JSON.stringify({ error: "Chỉ hỗ trợ phương thức POST từ SePAY" })
        };
    }

    try {
        const payload = JSON.parse(event.body || "{}");
        const {
            id,
            gateway,
            accountNumber,
            transferType,
            transferAmount,
            content,
            code
        } = payload;

        console.log(`[SePAY Webhook] Giao dịch mới: ID ${id} | ${gateway} | ${transferAmount}đ | Nội dung: ${content}`);

        // Acknowledge SePAY immediately with HTTP 200 { success: true }
        return {
            statusCode: 200,
            headers,
            body: JSON.stringify({
                success: true,
                message: "Đã nhận dữ liệu webhook thành công",
                received_id: id
            })
        };
    } catch (err) {
        console.error("[SePAY Webhook] Lỗi phân tích body:", err);
        return {
            statusCode: 400,
            headers,
            body: JSON.stringify({ success: false, error: err.message })
        };
    }
};

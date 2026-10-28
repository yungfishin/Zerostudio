# 🛡️ ZEROSTUDIO HACKER GAUNTLET 2026: ĐẤU TRƯỜNG PHÁ HỦY BẢO MẬT

Chào mừng toàn thể các Hacker, Pentester, Reverse Engineer, Cryptanalyst và các pháp sư AI/Computer Vision!

Đây là gói thử thách thực chiến được phát hành trực tiếp từ **ZeroStudio Research Lab** (https://zerostu.netlify.app).
Tất cả công nghệ phòng vệ này chạy **100% Client-Side / Zero-Server** ngay trên trình duyệt của người dùng.

Nhiệm vụ của các bạn rất đơn giản: **HÃY TÌM MỌI CÁCH ĐỂ PHÁ HỦY NÓ!**

---

### 🎯 THỬ THÁCH 1: THE INVISIBLE GHOST (Trích xuất thủy vân mù)
* **File mục tiêu:** `TARGET_1_STEGO_CHALLENGE_Q75.jpg`
* **Hiện trạng:** Bức ảnh này đã bị cấy một chuỗi ký tự mật dạng `FLAG{...}` sâu vào miền tần số rời rạc 2D-DCT của kênh độ sáng Luminance (Y), sau đó **bị nén giảm chất lượng lossy JPEG Quality=75**.
* **Nhiệm vụ:**
  1. Phân tích ma trận tần số của ảnh và khôi phục lại chuỗi Flag.
  2. Dùng file `verify_flag.py` (chạy lệnh: `python verify_flag.py`) để kiểm chứng xem bạn đã giải mã đúng hay chưa.
* **Quy tắc:** Không được dùng công cụ web của tác giả, hãy dùng mã nguồn, script hoặc kiến thức toán học của chính bạn!

---

### 🎯 THỬ THÁCH 2: THE STEGO WIPER (Tẩy sạch không tì vết)
* **File mục tiêu:** `TARGET_1_STEGO_CHALLENGE_Q75.jpg`
* **Nhiệm vụ:** Hãy biến đổi, áp dụng bộ lọc hoặc dùng bất kỳ công cụ nào để **tẩy sạch hoàn toàn chuỗi Flag ẩn** sao cho khi đưa vào Kính Soi của ZeroStudio, hệ thống báo lỗi không tìm thấy dữ liệu, **NHƯNG chất lượng thị giác của ảnh vẫn phải nguyên vẹn (PSNR > 36 dB)**.

---

### 🎯 THỬ THÁCH 3: THE SHIELD BREAKER (Phá vỡ lớp giáp Guilloche)
* **File mục tiêu:** `TARGET_2_GUILLOCHE_SHIELD.jpg`
* **Nhiệm vụ:** Bức ảnh này đã bị khóa bởi dải bảo vệ chéo 45 độ và mạng lưới hoa văn sóng Guilloche vi mô. Hãy dùng Stable Diffusion Inpainting, Generative AI, Photoshop hoặc thuật toán Computer Vision để gỡ bỏ hoàn toàn dải chữ đỏ và hoa văn bảo vệ, tạo ra một bức ảnh sạch sẽ như ban đầu để qua mặt hệ thống OCR/eKYC mà không để lại vết mờ nhòe dị thường.

---

### 🏆 PHẦN THƯỞNG & VINH DANH
* **Không tiền thưởng vật chất - Chỉ có sự tôn trọng danh dự học thuật cao nhất.**
* Bất kỳ ai giải được Thử thách 1 hoặc Thử thách 2 hoặc Thử thách 3 và gửi Writeup (bài phân tích kỹ thuật) về email `support@zerostu.netlify.app` hoặc đăng công khai trên J2TEAM / Viblo:
  1. **Vinh danh vĩnh viễn** trên Bảng Vàng **ZeroStudio Hall of Fame** tại https://zerostu.netlify.app.
  2. Ghi danh tên tuổi trong mã nguồn mở và Whitepaper công nghệ.
  3. Trở thành **Cố vấn Bảo mật Danh dự** của dự án.

Chúc anh em giải mã vui vẻ và bẻ gãy được hệ thống của chúng mình!

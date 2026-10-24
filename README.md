# 🛡️ ZeroPDF Studio - 100% Client-Side Private PDF Tools

> **Trạm xử lý PDF chuẩn an ninh Zero-Knowledge:** 100% tác vụ được thực thi trực tiếp trong bộ nhớ RAM trình duyệt của người dùng qua WebAssembly. Không gửi bất kỳ byte dữ liệu nào lên máy chủ. Miễn phí vĩnh viễn, không giới hạn dung lượng file, không quảng cáo bẩn.

---

## 🚀 TÍNH NĂNG ĐÃ HOÀN TẤT TRONG BẢN V1:
1. **🧩 Gộp PDF (Merge PDF):** Kéo thả nhiều file PDF, sắp xếp thứ tự linh hoạt, gộp siêu tốc chỉ trong 1-2 giây.
2. **✂️ Tách & Trích xuất trang (Split & Extract):** Hiển thị hình thu nhỏ (thumbnail) từng trang dạng lưới bằng PDF.js, bấm chọn các trang cần xuất hoặc xoay từng trang 90/180 độ.
3. **🖼️ Chuyển hình ảnh sang PDF (Images to PDF):** Kéo thả hàng loạt ảnh JPG/PNG, tự động xuất file PDF sắc nét đúng tỉ lệ gốc.
4. **🛡️ Kiểm tra An ninh Trực quan (Zero-Knowledge Audit):** Bấm vào huy hiệu trên góc phải để kiểm tra nhật ký mạng (Network Log), chứng minh 0 byte rời khỏi máy tính.
5. **✈️ Hoạt động 100% Offline:** Đã tích hợp sẵn thư viện trong thư mục `libs/`. Rút mạng Wi-Fi, bật chế độ máy bay vẫn sử dụng bình thường.

---

## 🌐 HƯỚNG DẪN ĐƯA LÊN MẠNG (DEPLOY TRONG 2 PHÚT - CHI PHÍ 0 ĐỒNG):

### Cách 1: Đưa lên Vercel (Khuyên dùng - Nhanh nhất)
1. Tải toàn bộ thư mục này lên một kho lưu trữ **GitHub** (chọn chế độ Public hoặc Private).
2. Truy cập [vercel.com](https://vercel.com) -> Đăng nhập bằng tài khoản GitHub.
3. Nhấn **Add New Project** -> Chọn kho GitHub vừa tạo -> Nhấn **Deploy**.
4. Xong! Bạn sẽ có ngay một đường link toàn cầu siêu nhanh: `https://ten-du-an-cua-ban.vercel.app` (kèm chứng chỉ bảo mật SSL HTTPS xanh).

### Cách 2: Đưa lên Cloudflare Pages
1. Truy cập [pages.cloudflare.com](https://pages.cloudflare.com).
2. Kết nối với GitHub repo -> Chọn thư mục -> Nhấn **Save and Deploy**.
3. Bạn có ngay một tên miền miễn phí trọn đời từ mạng lưới CDN nhanh nhất thế giới.

---

## 🔒 CAM KẾT BẢO MẬT & KIẾN TRÚC KỸ THUẬT:
* **Không Backend:** Không có máy chủ Node.js/Python trung gian tiếp nhận file.
* **Không Database:** Không lưu vết người dùng, không IDOR, không rò rỉ dữ liệu.
* **Engine:** `pdf-lib` + `pdf.js` chạy hoàn toàn bằng JavaScript/WebAssembly client-side.

# ZEROSTUDIO SKUNKWORKS R&D LAB (CÔ LẬP TRƯỚC - HÒA MẠNG SAU)

> **MẬT LỆNH PHÒNG THÍ NGHIỆM:** Mọi phát minh công nghệ đỉnh cao (Proof-of-Concept) bắt buộc phải được chế tác và stress-test độc lập 100% trong thư mục này trước khi đưa vào lõi sản xuất (`app.js` / `video_bridge.py`).

## 1. Danh Mục Các File Thử Nghiệm Độc Lập (PoC Roadmap):
1. `01_guilloche_matrix_cccd.html`: Ma trận hoa văn quang học Guilloche chống giả mạo eKYC CCCD/Hộ chiếu trực tiếp trên Canvas 4K không thư viện ngoài.
2. `02_nonlinear_warping_dsp.py`: Thuật toán co giãn thời gian vi phân (Non-Linear Time Warping) biến đổi tốc độ phi tuyến tính theo hàm Cosine, đánh lừa băm Content ID.
3. `03_ultrasound_steganography.py`: Nhúng và trích xuất thủy vân số vào dải tần siêu âm 19.2kHz bằng biến đổi Fourier (FFT), bền vững qua 3 lần nén MP3/AAC.
4. `04_neuro_hook_autosplicer.py`: Thuật toán bóc tách cao trào tâm lý micro-expression tự động tạo 3s hook giữ chân >65% AVD.
5. `05_lmp_p2p_checkout_kernel.html`: Vi nhân WASM nhúng trong sub-pixel video tự phát sinh QR thanh toán P2P VietQR NAPAS 24/7 trực tiếp trên màn hình video.
6. `06_zbox_airgap_patch_packager.py`: Đóng gói bản cập nhật hệ thống ngoại tuyến `.zup` có chữ ký số mật mã Ed25519 cho trạm ZeroBox không có internet.
7. `07_local_ai_webgpu.html`: [KỊCH BẢN 2] Động cơ trí tuệ nhân tạo cục bộ chạy 100% trên phần cứng card đồ họa NVIDIA GeForce RTX 3050 Ti qua chuẩn WebGPU / Transformers.js trực tiếp trong trình duyệt, suy luận hoàn toàn ngoại tuyến không cần internet.
8. `08_password_entropy_bruteforce_simulator.html`: [BẢO MẬT & ENTROPY] Trình mô phỏng bẻ khóa Brute-Force đa tầng phần cứng (Online, RTX 3050 Ti, Dàn 8x RTX 4090, Siêu máy tính 100 Triệu Tỷ phép tính/s) và đo độ hỗn loạn toán học (Entropy Bits) cục bộ thời gian thực.
9. `09_image_steganography_lsb.html`: [THỦY VÂN & GIẤU TIN ĐIỂM ẢNH] Công cụ nhúng và trích xuất mật thư nhị phân vào điểm ảnh LSB (Least Significant Bit) trên HTML5 Canvas, mắt thường không thể phân biệt màu sắc, hỗ trợ lớp bảo vệ mã hóa XOR PIN, 100% offline.

## 2. Kế Hoạch Lớn: Kịch Bản 1 - ZeroBrain Offline SLM Node (Khi hồi 100% Quota):
- **Phần cứng đích:** NVIDIA GeForce RTX 3050 Ti Laptop GPU (4GB Dedicated VRAM).
- **Mô hình tối ưu:** Llama 3.2 3B / Qwen 2.5 Coder 3B (Lượng tử hóa Q4_K_M ~ 2.0GB VRAM).
- **Động cơ thực thi:** Tích hợp `video_bridge.py` qua giao thức ASGI Localhost `127.0.0.1:8900`, cho phép trợ lý AI cục bộ tự động đọc/ghi file, chỉnh sửa video, đối soát ngân hàng ngay cả khi cách ly mạng 100%.

## 3. Tiêu Chuẩn Nghiệm Thu (Audit Gate):
- **Gate 1:** Chạy độc lập 100% (Zero External Dependency).
- **Gate 2:** Stress-test kiểm soát rò rỉ bộ nhớ (RAM Leak < 5MB).
- **Gate 3:** Benchmark hiệu năng mili-giây (Real-time Execution).
- **Gate 4:** Bàn giao vào hệ thống sản xuất dưới cờ tính năng bí mật (Feature Flag).

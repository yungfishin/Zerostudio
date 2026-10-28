import sys
import os
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

work_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(work_dir)
import anti_fraud_shield as afs

target_file = os.path.join(work_dir, "hieu_cccd_invisible_stego_q75.jpg")

print(f"🔍 [KÍNH SOI TẦN SỐ ĐANG QUÉT PHỔ 2D-DCT]:")
print(f"📂 Tệp tin kiểm tra: {target_file}")
print("📊 Định dạng: Ảnh đã bị nén giảm chất lượng JPEG Quality=75")
print("⏳ Đang phân tích ma trận tần số trung bình F(3,2) & F(2,3)...")

res = afs.extract_invisible_watermark(target_file)

if res.get("status") == "success":
    print("\n🎉 [PHÁT HIỆN THỦY VÂN VÔ HÌNH THÀNH CÔNG 100%!]")
    print("----------------------------------------------------------------------")
    print(f"🎯 CHUỖI ĐỊNH DANH GIẤU KÍN:")
    print(f"👉 \"{res['extracted_text']}\"")
    print("----------------------------------------------------------------------")
    print(f"⚡ Thuật toán khôi phục: {res['method']}")
    print("🔒 Trạng thái CRC32: Khớp mã kiểm tra 100% nguyên bản!")
else:
    print(f"\n❌ Thất bại: {res.get('error')}")

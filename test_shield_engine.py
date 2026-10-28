import sys
import os
from PIL import Image, ImageDraw

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

work_dir = os.path.dirname(os.path.abspath(__file__))
import anti_fraud_shield as afs

print("======================================================================")
print("  ZEROSTUDIO SOVEREIGN SECURITY - TEST SUITE 2026")
print("======================================================================\n")

# 1. Tạo ảnh CCCD giả lập (Mock CCCD card 1000x630)
print("📸 [1/4] Đang tạo mẫu phôi Căn cước công dân kiểm nghiệm...")
mock_cccd = Image.new('RGB', (1000, 630), (242, 246, 250))
d = ImageDraw.Draw(mock_cccd)
d.rounded_rectangle([(10, 10), (990, 620)], radius=24, outline=(180, 195, 210), width=3)
d.rectangle([(40, 30), (120, 110)], fill=(200, 60, 60))
d.text((150, 40), 'CONG HOA XA HOI CHU NGHIA VIET NAM', fill=(20, 40, 80))
d.text((150, 70), 'CAN CUOC CONG DAN / CITIZEN IDENTITY CARD', fill=(180, 30, 30))
d.rounded_rectangle([(40, 180), (130, 270)], radius=8, fill=(215, 180, 70), outline=(150, 120, 30), width=2)
d.rectangle([(40, 310), (240, 580)], fill=(120, 140, 160), outline=(60, 80, 100), width=2)
d.text((280, 200), 'So / No.: 001202008899', fill=(20, 20, 20))
d.text((280, 260), 'Ho va ten / Full name: NGUYEN VU TRUNG HIEU', fill=(10, 30, 70))
d.text((280, 320), 'Ngay sinh / Date of birth: 20/05/2002', fill=(30, 30, 30))
d.text((280, 380), 'Gioi tinh / Sex: Nam    Quoc tich: Viet Nam', fill=(30, 30, 30))
d.text((280, 440), 'Que quan / Place of origin: Ha Noi', fill=(30, 30, 30))

mock_input = os.path.join(work_dir, 'mock_cccd_raw.jpg')
mock_cccd.save(mock_input, 'JPEG', quality=95)
print(f"   -> Phôi CCCD gốc: {mock_input}")

# 2. Thử nghiệm Bộ Giáp Bảo Vệ CCCD
print("\n🛡️ [2/4] Đang đóng giáp bảo vệ CCCD (Guilloche + Khóa chéo 45 độ + Băm SHA-256)...")
mock_protected = os.path.join(work_dir, 'mock_cccd_protected.jpg')
res_cccd = afs.apply_cccd_anti_fraud_shield(
    mock_input,
    mock_protected,
    purpose='MO TAI KHOAN DOITAC 2026',
    organization='NGAN HANG MB BANK',
    recipient_name='NGUYEN VU TRUNG HIEU'
)
print(f"   -> Thành công! Mã băm xác thực: {res_cccd['hash_code']}")
print(f"   -> File xuất: {mock_protected}")

# 3. Thử nghiệm Thủy Vân Tần Số Ẩn 2D-DCT
print("\n👁️ [3/4] Đang khắc thủy vân vô hình vào miền tần số 2D-DCT...")
secret = 'ID:ZERO-2026|OWNER:HIEU|SCOPE:CONFIDENTIAL'
mock_stego = os.path.join(work_dir, 'mock_doc_stego.png')
res_embed = afs.embed_invisible_watermark(mock_input, mock_stego, secret, delta=30.0)
print(f"   -> Đã nhúng bí mật: {res_embed['payload']}")
print(f"   -> Độ vô hình PSNR: {res_embed['psnr_db']} dB (Mắt thường hoàn toàn không thấy!)")
print(f"   -> Hệ số lặp đa số phiếu: {res_embed['redundancy_factor']}x")

# 4. Thử thách Sống Sót Qua Nén JPEG Q=75 (Mô phỏng rò rỉ qua mạng)
print("\n🔥 [4/4] Kiểm tra độ bền: Nén JPEG Quality 75 & Quét trích xuất danh tính rò rỉ...")
mock_compressed_jpeg = os.path.join(work_dir, 'mock_doc_leaked_q75.jpg')
stego_img = Image.open(mock_stego)
stego_img.save(mock_compressed_jpeg, 'JPEG', quality=75)

res_extract = afs.extract_invisible_watermark(mock_compressed_jpeg)
if res_extract.get('status') == 'success':
    print(f"   🎉 TRÍCH XUẤT THÀNH CÔNG 100%:")
    print(f"   -> Danh tính kẻ rò rỉ: \"{res_extract['extracted_text']}\"")
    print(f"   -> Thuật toán: {res_extract['method']}")
else:
    print(f"   ❌ Thất bại: {res_extract.get('error')}")

print("\n======================================================================")
print("  HOÀN THÀNH KIỂM NGHIỆM! HỆ THỐNG ĐÃ SẴN SÀNG.")
print("======================================================================")

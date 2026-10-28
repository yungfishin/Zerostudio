# -*- coding: utf-8 -*-
"""
ZeroStudio - Independent Artifact Integrity Verifier
Verifies local files against published SHA-256 Checksums.
Usage: python verify_integrity.py
"""
import hashlib
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

work_dir = os.path.dirname(os.path.abspath(__file__))
checksum_file = os.path.join(work_dir, "CHECKSUMS.txt")

if not os.path.exists(checksum_file):
    print("❌ LỖI: Không tìm thấy file CHECKSUMS.txt!")
    sys.exit(1)

print("=" * 70)
print("  🛡️ ZEROSTUDIO INDEPENDENT ARTIFACT INTEGRITY VERIFIER 🛡️")
print("=" * 70)

all_passed = True
total = 0

with open(checksum_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            expected_hash = parts[0]
            filename = parts[1]
            file_path = os.path.join(work_dir, filename)
            total += 1
            
            if not os.path.exists(file_path):
                print(f"❌ [MISSING] {filename}: Tệp tin không tồn tại!")
                all_passed = False
                continue
                
            with open(file_path, "rb") as target_f:
                actual_hash = hashlib.sha256(target_f.read()).hexdigest()
                
            if actual_hash.lower() == expected_hash.lower():
                print(f"✅ [MATCH]   {filename}")
                print(f"            SHA-256: {actual_hash[:32]}...")
            else:
                print(f"🚨 [TAMPERED] {filename} BỊ SỬA ĐỔI HOẶC HỎNG DỮ LIỆU!")
                print(f"            Kỳ vọng: {expected_hash}")
                print(f"            Thực tế: {actual_hash}")
                all_passed = False

print("-" * 70)
if all_passed and total > 0:
    print(f"🎉 XÁC MINH THÀNH CÔNG: Toàn bộ {total}/{total} tệp tin đạt chuẩn toàn vẹn 100%!")
    print("   Không phát hiện dấu vết sửa đổi hay chèn mã độc vào mã nguồn.")
else:
    print("⚠️ CẢNH BÁO: Phát hiện tệp tin bị sai lệch băm! Đừng sử dụng bản phát hành này.")
print("=" * 70)

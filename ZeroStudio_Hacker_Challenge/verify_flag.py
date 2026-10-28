# -*- coding: utf-8 -*-
import hashlib
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stdin, 'reconfigure'):
    sys.stdin.reconfigure(encoding='utf-8')

TARGET_HASH = "4d84fc5c45bc19e2fc0b8e8c41d74b041eec71de0892ebf88fdf7d4c719f15e0"

print("=" * 65)
print("    🔥 ZEROSTUDIO CTF CHALLENGE - BỘ KIỂM TRA MẬT MÃ (FLAG VERIFIER) 🔥")
print("=" * 65)
print("Nhập Flag bí mật bạn đã trích xuất từ TARGET_1_STEGO_CHALLENGE_Q75.jpg:")
user_input = input("👉 FLAG: ").strip()

if not user_input:
    print("❌ Bạn chưa nhập nội dung!")
    sys.exit(1)

user_hash = hashlib.sha256(user_input.encode()).hexdigest()

if user_hash == TARGET_HASH:
    print("\n" + "*" * 65)
    print("🎉 CHÚC MỪNG BẠN! BẠN ĐÃ PHÁ GIẢI THÀNH CÔNG THỦY VÂN 2D-DCT!")
    print("🏆 Chuỗi Flag chính xác 100%:", user_input)
    print("📌 Hãy gửi writeup hoặc cách bạn bẻ khóa tới: support@zerostu.netlify.app")
    print("   để nhận vinh danh trên Hall of Fame vĩnh viễn!")
    print("*" * 65)
else:
    print("\n❌ SAI RỒI! Flag chưa chính xác hoặc còn thiếu ký tự.")
    print("💡 Gợi ý: Hãy phân tích miền tần số 2D-DCT của kênh Luminance (Y) ở các khối 8x8!")

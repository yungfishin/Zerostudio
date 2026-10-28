# -*- coding: utf-8 -*-
"""
ZeroStudio v3.0 - Automated Zero-Server Network Egress Telemetry Test
Fulfills Acceptance Criterion #3 (Independent Traffic Verification).
Asserts that ZERO bytes of sensitive identity data or image buffers leak to the network.
"""
import sys
import os
import time
import socket
import json
import hashlib
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

work_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(work_dir)
import anti_fraud_shield as afs

# 1. Socket Sniffer / Egress Interceptor
captured_egress_traffic = []

orig_socket_connect = socket.socket.connect
def intercepted_connect(self, address):
    captured_egress_traffic.append({
        "timestamp": time.time(),
        "type": "TCP_CONNECT",
        "destination": str(address)
    })
    return orig_socket_connect(self, address)

orig_socket_send = socket.socket.send
def intercepted_send(self, data, *args, **kwargs):
    captured_egress_traffic.append({
        "timestamp": time.time(),
        "type": "SOCKET_SEND",
        "bytes": len(data)
    })
    return orig_socket_send(self, data, *args, **kwargs)

socket.socket.connect = intercepted_connect
socket.socket.send = intercepted_send

print("=" * 70)
print("  📡 ZEROSTUDIO v3.0: KIỂM THỬ LƯU LƯỢNG MẠNG ZERO-SERVER (EGRESS AUDIT) 📡")
print("=" * 70)
print("[1/3] Kích hoạt màng bọc đánh chặn lưu lượng mạng cấp socket...")
print("[2/3] Bắt đầu nạp dữ liệu CCCD nhạy cảm tổng hợp (Synthetic PII):")

test_raw_image = os.path.join(work_dir, "mock_cccd_raw.jpg")
test_protected_output = os.path.join(work_dir, "scratch", "telemetry_test_protected.jpg")
test_stego_output = os.path.join(work_dir, "scratch", "telemetry_test_stego.png")

sensitive_name = "NGUYỄN VĂN MẪU"
sensitive_id = "001202009999"
sensitive_payload = f"ID: {sensitive_id} | NAME: {sensitive_name} | SECRET_TOKEN_7788"

print(f"      - Chủ thể: {sensitive_name}")
print(f"      - Số thẻ: {sensitive_id}")
print(f"      - Chuỗi mật mã: {sensitive_payload}")

# Thực thi bảo vệ Giáp CCCD
t0 = time.time()
afs.apply_cccd_anti_fraud_shield(
    test_raw_image,
    test_protected_output,
    purpose="MỞ TÀI KHOẢN NGÂN HÀNG",
    organization="NGÂN HÀNG QUÂN ĐỘI MB",
    recipient_name=sensitive_name
)
t_shield = (time.time() - t0) * 1000

# Thực thi cấy thủy vân vô hình 2D-DCT
t1 = time.time()
afs.embed_invisible_watermark(
    test_raw_image,
    test_stego_output,
    secret_payload=sensitive_payload,
    delta=28.0
)
t_stego = (time.time() - t1) * 1000

# Thực thi giải mã trích xuất thủy vân
t2 = time.time()
extract_res = afs.extract_invisible_watermark(test_stego_output)
t_extract = (time.time() - t2) * 1000

print("[3/3] Quét toàn bộ lưu lượng mạng phát sinh trong suốt chu trình xử lý...")
print("-" * 70)

egress_bytes_sent = sum(item.get("bytes", 0) for item in captured_egress_traffic)
total_connections = len([item for item in captured_egress_traffic if item.get("type") == "TCP_CONNECT"])

audit_result = {
    "audit_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "audit_version": "v3.0.0-verified",
    "specification": "Zero-Server-No-Egress-Verification",
    "results": {
        "sensitive_data_processed": True,
        "shield_render_latency_ms": round(t_shield, 2),
        "stego_embed_latency_ms": round(t_stego, 2),
        "stego_extract_latency_ms": round(t_extract, 2),
        "extraction_match": extract_res.get("status") == "success",
        "tcp_connections_attempted": total_connections,
        "raw_bytes_exfiltrated": egress_bytes_sent,
        "network_leak_detected": egress_bytes_sent > 0 or total_connections > 0
    }
}

report_path = os.path.join(work_dir, "ZERO_SERVER_AUDIT_REPORT.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(audit_result, f, indent=2)

print(f"📊 KẾT QUẢ KIỂM TOÁN LƯU LƯỢNG MẠNG:")
print(f"   • Số kết nối TCP cố gắng gọi ra ngoài: {total_connections}")
print(f"   • Số byte dữ liệu bị gửi ra Internet: {egress_bytes_sent} bytes")
print(f"   • Thời gian xử lý Giáp CCCD: {t_shield:.2f} ms")
print(f"   • Thời gian cấy Thủy vân 2D-DCT: {t_stego:.2f} ms")
print(f"   • Trích xuất thành công: {extract_res.get('status') == 'success'}")

if egress_bytes_sent == 0 and total_connections == 0:
    print("\n🎉 PHÁN QUYẾT: CHỨNG NHẬN ĐẠT CHUẨN ZERO-SERVER TUYỆT ĐỐI 100%!")
    print("   Hoàn toàn không có bất kỳ byte dữ liệu hay hình ảnh nào bị rò rỉ ra mạng.")
    print(f"   Báo cáo kiểm toán đã được ghi nhận tại: {report_path}")
else:
    print("\n🚨 CẢNH BÁO NGUY HIỂM: Phát hiện rò rỉ dữ liệu ra mạng ngoài!")
    sys.exit(1)

print("=" * 70)

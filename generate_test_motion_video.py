import subprocess
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKDIR = r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio"
INPUT_RAW = os.path.join(WORKDIR, "sample_raw_motion.mp4")
OUTPUT_MASTER = os.path.join(WORKDIR, "sample_broadcast_master_60fps.mp4")

def create_synthetic_raw_video():
    """Tạo một video chuyển động 9:16 60fps có đầy đủ âm thanh đa dải tần để kiểm nghiệm"""
    print("🎬 [BƯỚC 1/2] Đang tự động tạo video chuyển động mẫu 1080x1920 60fps...")
    
    # Tạo video 6 giây 1080x1920 60fps bằng FFmpeg testsrc2 + âm thanh giàu phổ tần (Sub-bass + mid + high)
    cmd_gen = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "testsrc2=size=1080x1920:rate=60:duration=6",
        "-f", "lavfi",
        "-i", "anoisesrc=d=6:c=pink:r=48000:a=0.06,aeval=val(0)+0.25*sin(2*PI*40*t)+0.25*sin(2*PI*120*t)+0.15*sin(2*PI*4800*t)",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        INPUT_RAW
    ]
    
    res = subprocess.run(cmd_gen, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ Đã tạo xong video chuyển động gốc: {INPUT_RAW}")
        return True
    else:
        print(f"❌ Lỗi tạo video gốc: {res.stderr}")
        return False

def run_pipeline():
    """Nhập module broadcast_creative_pipeline và chạy trên GPU RTX 3050 Ti"""
    from broadcast_creative_pipeline import process_video_broadcast
    print("\n⚡ [BƯỚC 2/2] Kích hoạt Quy trình Xử lý Sáng tạo Chuẩn Phát sóng (Broadcast Creative Pipeline)...")
    success = process_video_broadcast(INPUT_RAW, OUTPUT_MASTER)
    if success:
        print(f"\n🎉 THÀNH CÔNG RỰC RỠ!")
        print(f"🎥 Video Master hoàn chỉnh: {OUTPUT_MASTER}")
        print(f"▶️ Đang tự động bật video lên màn hình của anh Hiếu để thưởng thức...")
        os.startfile(OUTPUT_MASTER)

if __name__ == '__main__':
    if create_synthetic_raw_video():
        run_pipeline()

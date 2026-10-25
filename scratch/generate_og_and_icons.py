import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = r"c:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio"
ASSETS_IMG = os.path.join(BASE_DIR, "assets", "images")
ASSETS_ICONS = os.path.join(BASE_DIR, "assets", "icons")
os.makedirs(ASSETS_IMG, exist_ok=True)
os.makedirs(ASSETS_ICONS, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"

def create_og_image():
    w, h = 1200, 630
    img = Image.new("RGBA", (w, h), (10, 14, 26, 255))
    draw = ImageDraw.Draw(img)

    # Ambient radial gradient glows
    # Cyan glow top-left
    glow1 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gdraw1 = ImageDraw.Draw(glow1)
    gdraw1.ellipse([-100, -100, 600, 600], fill=(6, 182, 212, 45))
    glow1 = glow1.filter(ImageFilter.GaussianBlur(120))
    img.alpha_composite(glow1)

    # Gold glow bottom-right
    glow2 = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    gdraw2 = ImageDraw.Draw(glow2)
    gdraw2.ellipse([700, 250, 1350, 750], fill=(245, 158, 11, 40))
    glow2 = glow2.filter(ImageFilter.GaussianBlur(130))
    img.alpha_composite(glow2)

    # Subtle grid lines pattern
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for x in range(0, w, 40):
        odraw.line([(x, 0), (x, h)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, h, 40):
        odraw.line([(0, y), (w, y)], fill=(255, 255, 255, 6), width=1)
    img.alpha_composite(overlay)

    # Card border with rounded corners
    cdraw = ImageDraw.Draw(img)
    cdraw.rounded_rectangle([25, 25, w - 25, h - 25], radius=24, outline=(245, 158, 11, 100), width=2)

    # Badge Pill: 100% ZERO-KNOWLEDGE OFFLINE
    badge_box = [70, 70, 480, 115]
    cdraw.rounded_rectangle(badge_box, radius=999, fill=(15, 23, 42, 220), outline=(6, 182, 212, 180), width=1)
    font_badge = ImageFont.truetype(FONT_BOLD, 18)
    cdraw.text((95, 82), "⚡ 100% OFFLINE ZERO-KNOWLEDGE RAM", font=font_badge, fill=(6, 182, 212, 255))

    # Version Pill
    cdraw.rounded_rectangle([495, 70, 660, 115], radius=999, fill=(245, 158, 11, 30), outline=(245, 158, 11, 160), width=1)
    cdraw.text((515, 82), "PRO v2.4", font=font_badge, fill=(251, 191, 36, 255))

    # Brand Title
    font_title = ImageFont.truetype(FONT_BOLD, 62)
    cdraw.text((70, 140), "ZeroStudio Pro", font=font_title, fill=(255, 255, 255, 255))

    # Sub-Headline
    font_sub = ImageFont.truetype(FONT_BOLD, 30)
    cdraw.text((70, 225), "Siêu Bộ Công Cụ Video MMO & Xử Lý PDF Đỉnh Cao", font=font_sub, fill=(251, 191, 36, 255))

    # Bullet Points with custom badges
    font_item = ImageFont.truetype(FONT_REG, 23)
    font_item_b = ImageFont.truetype(FONT_BOLD, 23)

    items = [
        ("🎬 Lách Gậy Bản Quyền Video:", "Đổi âm vực Pitch +2.4%, Xóa Logo Douyin/TikTok 1080p"),
        ("📑 Nén & Chuyển Đổi PDF Chuẩn In Ấn:", "Bảo toàn 100% Vector, OCR tiếng Việt sắc nét"),
        ("🛡️ Bảo Mật Tuyệt Đối:", "Không gửi 1 Byte ra Internet, xử lý 100% tại RAM máy tính"),
        ("⚡ Tự Động Hóa 1-Click:", "Hỗ trợ Đa Ngôn Ngữ, Cài đặt PWA dùng mượt cả khi mất mạng")
    ]

    start_y = 295
    for i, (label, desc) in enumerate(items):
        y = start_y + i * 50
        # Bullet dot
        cdraw.ellipse([70, y + 8, 82, y + 20], fill=(6, 182, 212, 255))
        cdraw.text((95, y), label, font=font_item_b, fill=(241, 245, 249, 255))
        lbl_w = cdraw.textlength(label, font=font_item_b)
        cdraw.text((95 + lbl_w + 8, y), desc, font=font_item, fill=(148, 163, 184, 255))

    # Bottom Banner Bar
    cdraw.rounded_rectangle([70, 515, w - 70, 580], radius=16, fill=(15, 23, 42, 200), outline=(255, 255, 255, 30), width=1)
    font_cta = ImageFont.truetype(FONT_BOLD, 20)
    font_url = ImageFont.truetype(FONT_BOLD, 22)
    cdraw.text((100, 535), "⭐ 4.9/5.0 (1,480+ Đánh Giá) • 100% Bảo Mật RAM", font=font_cta, fill=(245, 158, 11, 255))
    cdraw.text((820, 533), "zerostu.netlify.app ↗", font=font_url, fill=(6, 182, 212, 255))

    out_path = os.path.join(ASSETS_IMG, "zerostudio-og-preview.png")
    img.convert("RGB").save(out_path, format="PNG", quality=95)
    print(f"Generated OG Image: {out_path} ({os.path.getsize(out_path)} bytes)")

def create_app_icon(size):
    img = Image.new("RGBA", (size, size), (10, 14, 26, 255))
    draw = ImageDraw.Draw(img)

    # Glow in center
    glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([size * 0.1, size * 0.1, size * 0.9, size * 0.9], fill=(245, 158, 11, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(int(size * 0.18)))
    img.alpha_composite(glow)

    # Inner rounded box
    padding = int(size * 0.08)
    corner = int(size * 0.22)
    idraw = ImageDraw.Draw(img)
    idraw.rounded_rectangle([padding, padding, size - padding, size - padding], radius=corner, fill=(15, 23, 42, 230), outline=(245, 158, 11, 200), width=max(2, int(size * 0.02)))

    # Stylized "ZS" or "Z" Logo in center
    font_size = int(size * 0.44)
    font = ImageFont.truetype(FONT_BOLD, font_size)
    text = "Z"
    bbox = idraw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = (size - th) // 2 - bbox[1] - int(size * 0.03)

    # Shadow
    idraw.text((tx + 2, ty + 4), text, font=font, fill=(0, 0, 0, 160))
    # Gradient/Neon text
    idraw.text((tx, ty), text, font=font, fill=(251, 191, 36, 255))

    # Dot indicator (Neon cyan dot bottom-right)
    dot_r = int(size * 0.08)
    dot_x = int(size * 0.72)
    dot_y = int(size * 0.70)
    idraw.ellipse([dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r], fill=(6, 182, 212, 255), outline=(255, 255, 255, 200), width=max(1, int(size * 0.015)))

    return img

def main():
    create_og_image()
    
    # 512x512
    icon512 = create_app_icon(512)
    p512 = os.path.join(ASSETS_ICONS, "icon-512.png")
    icon512.save(p512, format="PNG")
    print(f"Generated Icon 512: {p512}")

    # 192x192
    icon192 = create_app_icon(192)
    p192 = os.path.join(ASSETS_ICONS, "icon-192.png")
    icon192.save(p192, format="PNG")
    print(f"Generated Icon 192: {p192}")

    # Favicon 64x64
    fav = create_app_icon(64)
    pfav = os.path.join(ASSETS_ICONS, "favicon.png")
    fav.save(pfav, format="PNG")
    print(f"Generated Favicon: {pfav}")

if __name__ == "__main__":
    main()

import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BRAIN_DIR = Path(r"C:\Users\9htru\.gemini\antigravity\brain\8d9b3375-d185-467b-9be1-2f8457c97e33")
HTML_PATH = Path(r"C:\Users\9htru\OneDrive\Desktop\Commercial_Projects_Archive\ZeroPDF_Studio\index.html").as_uri()
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

async def capture_demo():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path=CHROME_PATH,
            headless=True
        )
        context = await browser.new_context(viewport={"width": 1280, "height": 1150})
        page = await context.new_page()

        # 0. Cybernetic Optical Intro Sequence
        print("Capturing 0. Cybernetic Optical Intro...")
        await page.goto(HTML_PATH)
        await page.wait_for_timeout(1050)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_00_CINEMATIC_INTRO.png"))

        # Wait for intro to finish or skip
        await page.evaluate("if (window.skipIntro) window.skipIntro()")
        await page.wait_for_timeout(600)

        # 1. Main View (Overview)
        print("Capturing 1. Overview...")
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_01_OVERVIEW.png"))

        # 2. Simulate Merged List
        print("Capturing 2. Merge List in Action...")
        await page.evaluate("""() => {
            state.mergeFiles = [
                { id: 'f1', file: { name: 'Hop_dong_kinh_te_2026.pdf' }, pageCount: 14, size: '2.45' },
                { id: 'f2', file: { name: 'Bang_ke_hoa_don_thue_Q3.pdf' }, pageCount: 8, size: '1.18' },
                { id: 'f3', file: { name: 'Phu_luc_dieu_khoan_bo_sung.pdf' }, pageCount: 5, size: '0.72' }
            ];
            renderMergeList();
        }""")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_02_MERGE_ACTION.png"))

        # 3. Simulate Split & Extract Thumbnails Grid
        print("Capturing 3. Split Grid...")
        await page.click('button[data-tab="split"]')
        await page.evaluate("""() => {
            state.splitPages = [];
            for (let i = 1; i <= 6; i++) {
                const canvas = document.createElement('canvas');
                canvas.width = 160;
                canvas.height = 220;
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = '#ffffff';
                ctx.fillRect(0, 0, 160, 220);
                ctx.strokeStyle = '#e2e8f0';
                ctx.lineWidth = 2;
                ctx.strokeRect(1, 1, 158, 218);

                ctx.fillStyle = '#1e293b';
                ctx.font = 'bold 12px sans-serif';
                ctx.fillText(`Tài liệu Trang ${i}`, 15, 30);

                ctx.fillStyle = '#94a3b8';
                for (let y = 50; y < 190; y += 12) {
                    const width = (y % 24 === 0) ? 80 : 130;
                    ctx.fillRect(15, y, width, 5);
                }

                state.splitPages.push({
                    pageNum: i,
                    canvasDataUrl: canvas.toDataURL('image/png'),
                    selected: i !== 4,
                    rotation: i === 2 ? 90 : 0
                });
            }
            document.getElementById('split-workspace').style.display = 'block';
            document.getElementById('split-dropzone').style.display = 'none';
            renderSplitGrid();
        }""")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_03_SPLIT_GRID.png"))

        # 4. Security Audit Modal
        print("Capturing 4. Security Modal...")
        await page.evaluate("runLeakAudit()")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_04_SECURITY_AUDIT.png"))

        # Close audit modal
        await page.evaluate("closeLeakAudit()")
        await page.wait_for_timeout(300)

        # 5. AI 4K Upscale Studio
        print("Capturing 5. AI 4K Upscale Studio...")
        await page.click('button[data-tab="upscale"]')
        await page.wait_for_timeout(300)
        await page.evaluate("""() => {
            const canvas = document.createElement('canvas');
            canvas.width = 400;
            canvas.height = 300;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 400, 300);
            grad.addColorStop(0, '#090d16');
            grad.addColorStop(0.5, '#1e293b');
            grad.addColorStop(1, '#0284c7');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 400, 300);

            ctx.fillStyle = '#f8fafc';
            ctx.font = 'bold 20px sans-serif';
            ctx.fillText('Chan_Dung_Do_Net_Cao.jpg', 30, 130);
            ctx.font = '14px sans-serif';
            ctx.fillStyle = '#94a3b8';
            ctx.fillText('Độ phân giải: 960 x 540 • 24-bit sRGB', 30, 165);

            const dataUrl = canvas.toDataURL('image/png');
            state.upscaleImage = { name: 'Chan_Dung_Do_Net_Cao.jpg', size: 142000 };
            state.upscaleOriginalUrl = dataUrl;
            state.upscaleScale = 4;

            setupUpscaleWorkspace(dataUrl, state.upscaleImage);

            const canvas4k = document.createElement('canvas');
            canvas4k.width = 800;
            canvas4k.height = 600;
            const ctx4k = canvas4k.getContext('2d');
            ctx4k.drawImage(canvas, 0, 0, 800, 600);
            ctx4k.strokeStyle = '#06b6d4';
            ctx4k.lineWidth = 4;
            ctx4k.strokeRect(6, 6, 788, 588);

            const upscaledUrl = canvas4k.toDataURL('image/png');
            state.upscaleResultUrl = upscaledUrl;
            document.getElementById('preview-after').src = upscaledUrl;
            document.getElementById('upscale-result-wrap').style.display = 'flex';
            document.getElementById('upscale-result-info').innerText = 'Hoàn tất: 3840 x 2160 (4K UHD) • 100% RAM Cục Bộ';
        }""")
        await page.wait_for_timeout(600)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_05_UPSCALE_4K.png"))

        # 6. Video Studio - Clean Watermark-Free Downloader
        print("Capturing 6. Video Studio (Go Logo)...")
        await page.click('button[data-tab="video"]')
        await page.wait_for_timeout(300)
        await page.evaluate("""() => {
            document.getElementById('video-url-input').value = 'https://www.tiktok.com/@creative_director/video/7342918237189281';
            detectPlatform('tiktok.com');
            renderResolvedVideo({
                title: 'Nghệ Thuật Kể Chuyện Điện Ảnh 2026 - Master Film Look (No Watermark)',
                uploader: '@director_alex • 1.2M Followers',
                duration: 48,
                video_url: 'https://www.w3schools.com/html/mov_bbb.mp4',
                audio_url: 'https://www.w3schools.com/html/horse.mp3',
                platform: 'TikTok'
            });

            // Create poster frame
            const pCanvas = document.createElement('canvas');
            pCanvas.width = 400;
            pCanvas.height = 700;
            const pCtx = pCanvas.getContext('2d');
            const grad = pCtx.createLinearGradient(0, 0, 400, 700);
            grad.addColorStop(0, '#090d16');
            grad.addColorStop(0.5, '#1e1b4b');
            grad.addColorStop(1, '#06b6d4');
            pCtx.fillStyle = grad;
            pCtx.fillRect(0, 0, 400, 700);
            pCtx.fillStyle = '#ffffff';
            pCtx.font = 'bold 24px sans-serif';
            pCtx.fillText('HD 1080P CLEAN', 80, 320);
            pCtx.font = '16px sans-serif';
            pCtx.fillStyle = '#94a3b8';
            pCtx.fillText('Đã khử hoàn toàn logo TikTok', 70, 360);
            document.getElementById('video-preview-el').poster = pCanvas.toDataURL('image/png');
        }""")
        await page.wait_for_timeout(600)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_06_VIDEO_STUDIO.png"))

        # 7. Video Remaster 4K Studio
        print("Capturing 7. Video Remaster 4K Studio...")
        await page.evaluate("""() => {
            switchVideoSubMode('remaster');
            setupVideoRemaster('https://www.w3schools.com/html/mov_bbb.mp4', 'Cinematic_Sequence_Shot_01.mp4');
            updateRemasterParam('sharpness', 85);
            updateRemasterParam('vibrance', 45);

            // Draw comparison frames
            const canvas = document.getElementById('remaster-canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = 800;
            canvas.height = 450;
            const grad = ctx.createLinearGradient(0, 0, 800, 450);
            grad.addColorStop(0, '#020617');
            grad.addColorStop(0.5, '#581c87');
            grad.addColorStop(1, '#db2777');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 800, 450);

            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 24px sans-serif';
            ctx.fillText('4K ULTRA HD REMASTERED • 60FPS', 40, 210);
            ctx.font = '15px sans-serif';
            ctx.fillStyle = '#fbcfe8';
            ctx.fillText('Micro-Sharpness: 85% • HDR Dynamic Vibrance: 45%', 40, 250);

            // Give source video poster too
            const sCanvas = document.createElement('canvas');
            sCanvas.width = 800;
            sCanvas.height = 450;
            const sCtx = sCanvas.getContext('2d');
            sCtx.fillStyle = '#0f172a';
            sCtx.fillRect(0, 0, 800, 450);
            sCtx.fillStyle = '#94a3b8';
            sCtx.font = 'bold 22px sans-serif';
            sCtx.fillText('Video Gốc 1080p (Chưa Nâng Cấp)', 40, 220);
            document.getElementById('remaster-source-video').poster = sCanvas.toDataURL('image/png');
        }""")
        await page.wait_for_timeout(600)
        await page.screenshot(path=str(BRAIN_DIR / "ZEROPDF_DEMO_07_VIDEO_REMASTER.png"))

        await browser.close()
        print("SUCCESS: All 7 demo snapshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture_demo())

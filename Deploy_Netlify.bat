@echo off
chcp 65001 >nul
title ZeroStudio - 1-Click Netlify Production Deploy
echo ========================================================
echo   ⚡ ZEROSTUDIO CLOUD DEPLOY - 1-CLICK PRODUCTION ⚡
echo ========================================================
echo.
echo [1/3] Kiểm tra Netlify CLI...
where netlify >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Netlify CLI chưa được cài đặt. Đang tự động cài đặt...
    call npm install -g netlify-cli
)

echo [2/3] Kiểm tra kết nối tài khoản & Production Site...
echo.
echo Đang triển khai toàn bộ ứng dụng lên Netlify Production...
call netlify deploy --prod --dir=.

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo   ✅ TRIỂN KHAI PRODUCTION THÀNH CÔNG!
    echo   Bản cập nhật v2.5.6 đã hoạt động trên toàn cầu.
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   [LƯU Ý] Nếu đây là lần đầu tiên chạy Netlify CLI:
    echo   Vui lòng đăng nhập bằng lệnh: netlify login
    echo   Sau đó liên kết site bằng lệnh: netlify link
    echo ========================================================
)
echo.
pause

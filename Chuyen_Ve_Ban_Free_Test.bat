@echo off
chcp 65001 >nul
echo =======================================================
echo   CHUYỂN ZEROSTUDIO VỀ CHẾ ĐỘ FREE (TEST KHÁCH HÀNG)
echo =======================================================
echo.

if exist "%USERPROFILE%\.zerostudio_license" (
    del /f /q "%USERPROFILE%\.zerostudio_license"
    echo [OK] Đã xóa file bản quyền trên ổ cứng.
) else (
    echo [INFO] Không tìm thấy file bản quyền trên ổ cứng.
)

if exist "%USERPROFILE%\.zerostudio_license.bak" (
    del /f /q "%USERPROFILE%\.zerostudio_license.bak"
)

if exist "license.key" (
    del /f /q "license.key"
    echo [OK] Đã xóa license.key trong thư mục app.
)

echo.
echo Bây giờ máy bạn đã trở thành KHÁCH HÀNG CHƯA MUA (Free).
echo Hãy mở lại web hoặc app để test cảm giác bị khóa đòi tiền nhé!
echo (Khi nào muốn khôi phục Pro, chỉ cần chạy Khoi_Phuc_Admin_Pro.bat)
echo.
pause

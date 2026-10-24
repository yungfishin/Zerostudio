@echo off
chcp 65001 >nul
echo =======================================================
echo   KHÔI PHỤC BẢN QUYỀN VIP ADMIN PRO (ZEROSTUDIO)
echo =======================================================
echo.

if exist "%USERPROFILE%\.zerostudio_license.bak" (
    ren "%USERPROFILE%\.zerostudio_license.bak" ".zerostudio_license"
    echo [OK] Đã khôi phục file bản quyền trên ổ cứng.
) else (
    echo ZERO-PRO-ADMIN-VIP-2026 > "%USERPROFILE%\.zerostudio_license"
    echo [OK] Đã tạo mới file bản quyền VIP Admin.
)

echo ZERO-PRO-ADMIN-VIP-2026 > "license.key"

echo.
echo CHÚC MỪNG: Bạn đã trở lại làm ADMIN VIP PRO VĨNH VIỄN!
echo Mở app ZeroStudio.exe hoặc web để tận hưởng full tính năng.
echo.
pause

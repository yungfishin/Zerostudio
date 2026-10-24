@echo off
chcp 65001 >nul
title ZeroStudio - Admin Emergency Rescue Tool
color 0A
echo ========================================================
echo   ZEROSTUDIO - CONG CU GIAI CUU VA GO KHOA ADMIN
echo ========================================================
echo [i] Dang ket noi may chu an ninh bao mat noi bo...
echo.

python -c "import urllib.request, hashlib; salt = '_ZEROSTUDIO_SECURE_SALT_'; h = hashlib.sha256(('HIEU2026' + salt).encode()).hexdigest(); r = urllib.request.urlopen('http://127.0.0.1:8900/api/admin-unban?auth=' + h + '&ip=all').read().decode(); print('  -> May chu phan hoi:', r)" 2>nul

if exist "%USERPROFILE%\.zerostudio_banned_ips.json" (
    del /f /q "%USERPROFILE%\.zerostudio_banned_ips.json" >nul 2>&1
    echo   -> [OK] Da xoa danh sach den IP tren o cung.
)

if exist "%USERPROFILE%\.zerostudio_device_registry.json" (
    del /f /q "%USERPROFILE%\.zerostudio_device_registry.json" >nul 2>&1
    echo   -> [OK] Da lam moi so cai dang ky thiet bi.
)

echo ZERO-PRO-HIEU-MASTER-2026-SECURE > "%USERPROFILE%\.zerostudio_license"
echo   -> [OK] Da bao luu ban quyen Ultra MMO Master tren o cung.

echo.
echo ========================================================
echo   CHUC MUNG: HE THONG DA DUOC GO KHOA VA PHUC HOI 100%!
echo   Moi lenh cam da duoc xoa sach. Hay tai lai trang web!
echo ========================================================
echo.
pause

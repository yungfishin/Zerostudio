@echo off
title Day ZeroStudio Len GitHub
color 0B
echo ========================================================
echo       ZEROSTUDIO - 1-CLICK GITHUB PUSH ^& DEPLOY
echo ========================================================
echo.
echo [i] Tai khoan Git hien tai: yungfishin (yungfishin@gmail.com)
echo.
echo Neu ban chua tao Repo tren GitHub, hay mo link sau truoc:
echo https://github.com/new
echo (Dat ten la: zerostudio, chon Public roi bam Create)
echo.
set /p REPO_URL="Dan link Git Repo cua ban vao day (vi du: https://github.com/yungfishin/zerostudio.git): "

if "%REPO_URL%"=="" (
    echo [!] Ban chua nhap duong dan. Huy thao tac...
    pause
    exit /b
)

git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%
git branch -M main
echo.
echo [i] Dang day source code len GitHub...
git push -u origin main

echo.
echo ========================================================
echo [OK] DA DAY SOURCE CODE LEN GITHUB THANH CONG!
echo.
echo De bat link web online mien phi vinh vien:
echo 1. Tren GitHub, vao muc Settings -^> Pages.
echo 2. Tai muc Branch, chon "main" (root) -^> Bam Save.
echo 3. Web se online tai: https://yungfishin.github.io/zerostudio/
echo ========================================================
pause

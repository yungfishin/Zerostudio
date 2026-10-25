@echo off
title ZeroStudio Pro Desktop Launcher
color 0B
echo ========================================================
echo       ZEROSTUDIO DESKTOP PRO - HYBRID CLOUD SUITE
echo ========================================================
echo [i] Khoi dong moi truong Zero-Knowledge cuc bo...
echo [i] Kich hoat Hardware Acceleration ^& Local Video Bridge...
echo.

:: 1. Khoi dong Video Bridge cuc bo chay ngam tren port 8900
start /b "" python "%~dp0video_bridge.py" >nul 2>&1

:: 2. Kiem tra ket noi Internet de tu dong dong bo tinh nang moi nhat tu Cloud
set "TARGET_URL=https://zerostu.netlify.app"
ping -n 1 8.8.8.8 >nul 2>&1
if %errorlevel% neq 0 (
    echo [OFFLINE] Khong co Internet, chuyen sang che do chay file cuc bo...
    set "TARGET_URL=file:///%~dp0index.html"
) else (
    echo [CLOUD] Da ket noi Cloud thanh cong! Dang dong bo phien ban moi nhat...
)

:: 3. Mo ung dung trong che do Native Frameless Desktop Window
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="%TARGET_URL%" --window-size=1360,900
) else if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --app="%TARGET_URL%" --window-size=1360,900
) else (
    start "" "%TARGET_URL%"
)

echo [OK] ZeroStudio Pro da san sang!
exit

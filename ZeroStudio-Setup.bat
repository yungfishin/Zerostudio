@echo off
title ZeroStudio Pro Desktop Launcher
color 0B
echo ========================================================
echo       ZEROSTUDIO DESKTOP PRO - STANDALONE SUITE
echo ========================================================
echo [i] Khoi dong moi truong Zero-Knowledge cuc bo...
echo [i] Kich hoat Hardware Acceleration ^& Local Video Bridge...
echo.

:: 1. Khoi dong Video Bridge cuc bo chay ngam
start /b "" python "%~dp0video_bridge.py" >nul 2>&1

:: 2. Mo ung dung trong che do Native Desktop App Window (khong thanh dia chi)
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="file:///%~dp0index.html" --window-size=1280,850
) else if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --app="file:///%~dp0index.html" --window-size=1280,850
) else (
    start "" "%~dp0index.html"
)

echo [OK] ZeroStudio Pro da san sang!
exit

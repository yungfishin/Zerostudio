@echo off
title ZeroStudio Video Bridge
color 0B
echo ========================================================
echo       ZEROSTUDIO - LOCAL SECURE VIDEO BRIDGE
echo ========================================================
echo [i] Khoi dong cau noi video cuc bo (127.0.0.1:8899)...
echo [i] Khong gui du lieu ra ngoai - Hoan toan rieng tu.
echo.

python "%~dp0video_bridge.py"

pause

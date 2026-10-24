@echo off
title ZeroStudio Video Bridge ^& Cyber Defense Core
color 0B
echo ========================================================
echo   ZEROSTUDIO - LOCAL SECURE VIDEO BRIDGE ^& CYBER DEFENSE
echo ========================================================
echo [i] Khoi dong cau noi video cuc bo (127.0.0.1:8900 / 8899)...
echo [i] Khong gui du lieu ra ngoai - Hoan toan rieng tu.
echo [i] He thong phong thu Anti-Hack va Blacklist IP vinh vien da kich hoat.
echo.

python "%~dp0video_bridge.py"

pause

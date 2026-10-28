@echo off
chcp 65001 > nul
title ZeroStudio - Phòng Thí Nghiệm Vi Kiến Trúc & Vật Lý Bán Dẫn
cd /d "%~dp0"
echo ========================================================
echo   ZEROSTUDIO FRONTIER SILICON & CRYPTO LAB
echo   Chứng minh thực nghiệm tại mắt 3 Tử huyệt:
echo   1. Dòng rò Sneak Path vs Transistor 1T1R
echo   2. Bùng nổ Dung lượng & Nhiễu FHE (Bootstrapping)
echo   3. Mã độc DNA ghi đè thanh ghi RIP (2017 Exploit)
echo ========================================================
echo.
python run_frontier_lab.py
pause

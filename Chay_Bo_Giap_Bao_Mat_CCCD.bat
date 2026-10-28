@echo off
chcp 65001 >nul
title ZeroStudio Sovereign Security Lab - Anti-Fraud & Steganography Shield
echo ======================================================================
echo   ZEROSTUDIO BỘ GIÁP BẢO MẬT CCCD & THỦY VÂN TẦN SỐ ẨN 2026
echo ======================================================================
echo.
echo   [1] Mở Phòng Thí Nghiệm Bảo Mật (Giao diện Web tương tác trực tiếp)
echo   [2] Chạy Kiểm Nghiệm Python: Đóng giáp CCCD + Khắc/Trích Thủy vân 2D-DCT
echo.
set /p choice="Nhập lựa chọn của anh Hiếu (1 hoặc 2): "

if "%choice%"=="1" (
    start "" "%~dp0anti_fraud_lab.html"
)
if "%choice%"=="2" (
    python "%~dp0test_shield_engine.py"
    pause
)

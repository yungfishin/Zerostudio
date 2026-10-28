@echo off
chcp 65001 >nul
title ZeroStudio Broadcast Master Showcase
echo ======================================================================
echo   ZEROSTUDIO BROADCAST CREATIVE SUITE - MASTER 60FPS (EBU R128)
echo ======================================================================
echo.
echo   [1] Xem Video ZeroStudio Thực Tế (10s Master Chuẩn Phát Sóng)
echo   [2] Xem Video Chuyển Động Tổng Hợp (Lissajous 60fps + Sub-bass 40Hz)
echo   [3] Tự Động Render Lại Pipeline Sáng Tạo Bằng FFmpeg
echo.
set /p choice="Nhập lựa chọn của anh Hiếu (1, 2 hoặc 3): "

if "%choice%"=="1" (
    start "" "%~dp0ZeroStudio_Broadcast_Master_10s.mp4"
)
if "%choice%"=="2" (
    start "" "%~dp0sample_broadcast_master_60fps.mp4"
)
if "%choice%"=="3" (
    python "%~dp0generate_test_motion_video.py"
)

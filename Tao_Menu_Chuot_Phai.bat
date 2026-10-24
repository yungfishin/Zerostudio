@echo off
chcp 65001 >nul
title ZeroStudio Pro - Cài Đặt Menu Chuột Phải Windows

echo =======================================================
echo    ZEROSTUDIO PRO - TÍCH HỢP CHUỘT PHẢI WINDOWS
echo =======================================================
echo.
echo Đang đăng ký tính năng vào Windows Explorer (Không cần quyền Admin)...

set "APP_BAT=%~dp0ZeroStudio-Setup.bat"

:: 1. Tích hợp cho file Video (.mp4, .webm, .mov)
reg add "HKCU\Software\Classes\SystemFileAssociations\.mp4\shell\ZeroStudioAntiban" /ve /d "[ZeroStudio Pro] Lách Bản Quyền & Đổi MD5" /f >nul
reg add "HKCU\Software\Classes\SystemFileAssociations\.mp4\shell\ZeroStudioAntiban\command" /ve /d "\"%APP_BAT%\" \"%%1\"" /f >nul

reg add "HKCU\Software\Classes\SystemFileAssociations\.webm\shell\ZeroStudioAntiban" /ve /d "[ZeroStudio Pro] Lách Bản Quyền & Đổi MD5" /f >nul
reg add "HKCU\Software\Classes\SystemFileAssociations\.webm\shell\ZeroStudioAntiban\command" /ve /d "\"%APP_BAT%\" \"%%1\"" /f >nul

:: 2. Tích hợp cho file PDF (.pdf)
reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\ZeroStudioPDF" /ve /d "[ZeroStudio Pro] Gộp & Chỉnh Sửa PDF" /f >nul
reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\ZeroStudioPDF\command" /ve /d "\"%APP_BAT%\" \"%%1\"" /f >nul

echo.
echo [V] THÀNH CÔNG! Đã tích hợp Menu Chuột Phải vào Windows File Explorer.
echo Bây giờ bạn chỉ cần bấm chuột phải vào bất kỳ file Video hoặc PDF nào trên máy tính
echo để gọi ZeroStudio Pro xử lý tức thì!
echo.
pause

@echo off
chcp 65001 >nul
title ZeroStudio Pro - Gỡ Menu Chuột Phải Windows

echo Đang gỡ bỏ menu chuột phải ZeroStudio khỏi Windows Explorer...

reg delete "HKCU\Software\Classes\SystemFileAssociations\.mp4\shell\ZeroStudioAntiban" /f >nul 2>&1
reg delete "HKCU\Software\Classes\SystemFileAssociations\.webm\shell\ZeroStudioAntiban" /f >nul 2>&1
reg delete "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\ZeroStudioPDF" /f >nul 2>&1

echo.
echo [V] Đã gỡ bỏ sạch sẽ menu chuột phải.
pause

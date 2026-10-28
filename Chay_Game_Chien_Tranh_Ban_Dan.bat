@echo off
chcp 65001 > nul
title Project AEGIS: The Silicon War - ZeroStudio
cd /d "%~dp0"
echo ========================================================
echo   PROJECT AEGIS: THE SILICON WAR
echo   Đấu trường mô phỏng thực chiến Dự án 2:
echo   Mã độc AI Đa hình vs Pháo đài Bán dẫn CHERI + seL4
echo ========================================================
echo.
start http://localhost:8952/aegis_silicon_game.html
echo Đã mở trò chơi trên trình duyệt của bạn!
pause

@echo off
REM Push restart-time.json to GitHub
cd /d "%~dp0"
git add restart-time.json
git commit -m "Update timer"
git push origin main
pause

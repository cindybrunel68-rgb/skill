@echo off
cd /d "C:\Users\legue\Downloads\mon aios\template-aios-local-v1-main"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0daily_backup.ps1"
exit /b %ERRORLEVEL%

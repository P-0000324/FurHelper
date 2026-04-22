@echo off
color 97
echo FurHelper Reset tool
echo Version 0.1.0001
echo By P0000324, 25.06.24
echo ================
echo Press any key to reset...
pause
echo Resetting configs...
cd Data
rd /s /q ".\FurHelper"
xcopy /S /E ".\FurHelper_backup\*" ".\FurHelper\*"
pause

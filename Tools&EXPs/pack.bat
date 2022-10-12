@echo off
pyinstaller --version-file internal_file_version_info.txt -w -F "Selector Version 1.2 Internal Release.py"
pyinstaller --version-file public_file_version_info.txt -w -F "Selector Version 1.2 Public Release.py"
move dist\"Selector Version 1.2 Internal Release.exe"
move dist\"Selector Version 1.2 Public Release.exe"
rmdir /S /Q build
rmdir /S /Q dist
del "Selector Version 1.2 Internal Release.spec"
del "Selector Version 1.2 Public Release.spec"
pause

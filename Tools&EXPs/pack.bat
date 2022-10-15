@echo off
pyinstaller --version-file internal_file_version_info.txt -w -F "Selector 1.3 Internal.py"
pyinstaller --version-file public_file_version_info.txt -w -F "Selector 1.3 Public.py"
move dist\"Selector 1.3 Internal.exe"
move dist\"Selector 1.3 Public.exe"
rmdir /S /Q build
rmdir /S /Q dist
del "Selector 1.3 Internal.spec"
del "Selector 1.3 Public.spec"
pause

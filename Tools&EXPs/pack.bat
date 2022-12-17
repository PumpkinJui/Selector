@echo off
pyinstaller --version-file internal_file_version_info.txt -w --hidden-import pygame -F "Selector 1.4 Internal.py"
pyinstaller --version-file public_file_version_info.txt -w --hidden-import pygame -F "Selector 1.4 Public.py"
move dist\"Selector 1.4 Internal.exe" dist
move dist\"Selector 1.4 Public.exe" dist
rmdir /S /Q build
del "Selector 1.4 Internal.spec"
del "Selector 1.4 Public.spec"
pyinstaller --version-file internal_file_version_info.txt -w --hidden-import pygame -D "Selector 1.4 Internal.py"
pyinstaller --version-file public_file_version_info.txt -w --hidden-import pygame -D "Selector 1.4 Public.py"
rmdir /S /Q build
del "Selector 1.4 Internal.spec"
del "Selector 1.4 Public.spec"
pause

@echo off
pyinstaller --version-file internal_file_version_info.txt -w -F "Selector Version 1.1 Internal Release.py" --clean
pyinstaller --version-file public_file_version_info.txt -w -F "Selector Version 1.1 Public Release.py" --clean
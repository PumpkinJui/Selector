@ECHO OFF

:loop
CLS
ECHO ���� 1 ���д����
ECHO ���� 2 ���߰�װ/���� pyinstaller��
ECHO ���� 3 ���߰�װ/������������������
CHOICE /C 0123 /N /M "���� 0 �˳���"
if errorlevel 4 goto requirements
if errorlevel 3 goto pyinstaller
if errorlevel 2 goto pack
if errorlevel 1 goto exit
if errorlevel 0 goto exit
goto loop

:pack
CLS
pyinstaller --hidden-import pygame.mixer --version-file file_version_info.txt -w -D ../Selector.py
rmdir /S /Q build
del "Selector.spec"
pause
goto loop

:pyinstaller
CLS
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pyinstaller
pause
goto loop

:requirements
CLS
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade -r ../requirements.txt
pause
goto loop

:exit
exit
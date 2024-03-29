@ECHO OFF

:loop
CLS
ECHO 输入 1 进行打包；
ECHO 输入 2 在线安装/升级 pyinstaller；
ECHO 输入 3 在线安装/升级第三方库依赖；
CHOICE /C 0123 /N /M "输入 0 退出："
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

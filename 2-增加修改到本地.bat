@echo off 
mode con: cols=80 lines=25 
chcp 65001
color 09
echo %cd% 
git add .
set /p info=请输入main分支改动信息:
git commit -m %info%
pause 

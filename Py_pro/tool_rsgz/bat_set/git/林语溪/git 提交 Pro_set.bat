@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
F: && cd F:\0-git-pro\Pro-set
set /p info=请输入main分支改动信息:
git add .
git commit -m %info%
git push origin main
pause
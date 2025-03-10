@echo off 
mode con: cols=80 lines=25 
chcp 65001
color 09 
git add .
git push origin main
pause 

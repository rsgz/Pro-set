@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
set /p pic_path=图片路径?:
set /p x=尺寸x?:
set /p y=尺寸y?:
ffmpeg -i %pic_path% -vf scale=%x%:%y% 001.png
pause
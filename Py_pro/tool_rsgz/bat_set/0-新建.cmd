set a=@echo off
set aa=chcp 65001
set b=mode con: cols=80 lines=25
set c=color 09
set d=pause
echo %a% > 0-001.bat
echo %aa% > 0-001.bat
echo %b% >> 0-001.bat
echo %c% >> 0-001.bat
echo %d% >> 0-001.bat

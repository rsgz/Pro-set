@echo off
:: 提示用户拖拽文件
echo 把文件拖拽进来

:: 检查是否有文件被拖入
if "%1"=="" (
    echo 没检测到文件
    pause
    exit /b
)

:: 获取文件路径
set input_file=%1

:: 提示用户输入目标文件格式
echo.
set /p output_format=Enter the desired output format (e.g., mp4, avi, mp3, mkv, etc.): 

:: 检查用户是否输入了格式
if "%output_format%"=="" (
    echo 你没有输入转换后的格式
    pause
    exit /b
)

:: 获取文件扩展名
for %%A in ("%input_file%") do set file_ext=%%~xA

:: 生成输出文件名
set output_file="%~dpn1.%output_format%"

:: 输出文件路径
echo Converting %input_file% to %output_file%...
ffmpeg -i "%input_file%" %output_file%
echo 转换完成

pause
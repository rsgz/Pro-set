@echo off
:: ��ʾ�û���ק�ļ�
echo ���ļ���ק����

:: ����Ƿ����ļ�������
if "%1"=="" (
    echo û��⵽�ļ�
    pause
    exit /b
)

:: ��ȡ�ļ�·��
set input_file=%1

:: ��ʾ�û�����Ŀ���ļ���ʽ
echo.
set /p output_format=Enter the desired output format (e.g., mp4, avi, mp3, mkv, etc.): 

:: ����û��Ƿ������˸�ʽ
if "%output_format%"=="" (
    echo ��û������ת����ĸ�ʽ
    pause
    exit /b
)

:: ��ȡ�ļ���չ��
for %%A in ("%input_file%") do set file_ext=%%~xA

:: ��������ļ���
set output_file="%~dpn1.%output_format%"

:: ����ļ�·��
echo Converting %input_file% to %output_file%...
ffmpeg -i "%input_file%" %output_file%
echo ת�����

pause
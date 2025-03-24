import os
import time

# 需要清空的目录列表
directories = [
r"E:\z\0-up1220-1\App_Data\Logs",
r"E:\z\0-up1220-1\StaticFiles",
r"E:\z\0-up1220-2\App_Data\Logs",
r"E:\z\0-up1220-2\StaticFiles",
r"E:\z\up1230b-1\App_Data\Logs",
r"E:\z\up1230b-1\StaticFiles",
r"E:\z\up1230b-2\App_Data\Logs",
r"E:\z\up1230b-2\StaticFiles",
]

def clear_directories(dirs):
    for directory in dirs:
        if os.path.exists(directory):
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)  # 删除文件或符号链接
                    elif os.path.isdir(file_path):
                        os.rmdir(file_path)  # 删除空文件夹
                except Exception as e:
                    print(f"无法删除 {file_path}: {e}")
flag=1
if flag==1:
    while True:
        clear_directories(directories)
        print("已清空指定目录中的文件")
        time.sleep(30 * 60)  # 休眠 30 分钟
        # time.sleep(10)  # 休眠 30 分钟
        print("等待30分钟!")
        # time.sleep(10 * 1)  # 休眠 30 分钟
else:
    clear_directories(directories)
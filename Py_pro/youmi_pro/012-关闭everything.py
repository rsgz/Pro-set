import subprocess

def close_everything_windows():
    """
    使用taskkill命令关闭所有Everything进程。
    """
    # 使用taskkill命令，/IM指定要关闭的程序映像名称，/F表示强制终止
    subprocess.run(["taskkill", "/IM", "Everything.exe", "/F"], check=True)

if __name__ == '__main__':
    try:
        close_everything_windows()
        print("所有Everything窗口已被关闭")
    except subprocess.CalledProcessError as e:
        print(f"发生错误: {e}")
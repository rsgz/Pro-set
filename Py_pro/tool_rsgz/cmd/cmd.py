import os,platform,shutil,random,string
import subprocess
import socket
j=os.path.join
s=os.system

class Cmd:
    def __init__(self):
        pass

    def xinjian_cmd(self):
        pass

    # 查看所有wifi名称
    def chakan_wifi_mingcheng_all(self):
        r"""查看所有wifi名称"""
        os.system("netsh wlan show profile")

    # 新建cmd
    def xinjian_cmd_file(self, fumulu,cmd_name="demo.bat"):
        """
        创建一个包含指定语句的 .bat 文件。

        参数:
        file_path (str): .bat 文件的路径。
        """
        bat_commands = [
            "@echo off",
            "mode con: cols=80 lines=25",
            "color 09",
            "pause"
        ]

        try:
            with open(j(fumulu,cmd_name), 'w', encoding='utf-8') as f:
                for command in bat_commands:
                    f.write(command + '\n')
            print(f"成功创建 .bat 文件: {j(fumulu,cmd_name)}")
        except IOError as e:
            print(f"创建 .bat 文件时出错: {e}")

    # 命名计算机
    def mingming_jisuanji_gui(self):
        r"""命名计算机"""
        s("rundll32.exe shell32.dll,Control_RunDLL sysdm.cpl")

    # 打开任务管理器
    def dakai_renwu_guanliqi_gui(self):
        r"""打开任务管理器"""
        s("start taskmgr.exe")

    # 设置Administrator密码
    def shezhi_mima_Administrator(self,mima):
        r"""设置Administrator密码"""
        print(f"开始设置Administrator账户密码")
        print(f"你的新密码：{mima}")
        s(f"net user Administrator {mima}")

    # 查看电脑版本
    def chakan_win_banben_gui(self):
        r"""查看电脑版本"""
        s("start winver.exe")

    # 查看电脑版本
    def chakan_win_banben_platform(self):
        """使用 platform 模块获取操作系统版本信息"""
        system = platform.system()
        release = platform.release()
        version = platform.version()
        banben_info = f"操作系统：{system}，版本：{release}，构建：{version}"
        print(banben_info)
        return f"操作系统：{system}，版本：{release}，构建：{version}"

    # 打开host文件目录
    def dakai_host_wenjian_mulu(self):
        r"""打开host文件目录"""
        s(r"start C:\Windows\System32\drivers\etc")

    # 打开host文件
    def dakai_host_wenjian_gui(self):
        r"""打开host文件"""
        s(r"notepad C:\Windows\System32\drivers\etc\hosts")

    # 打开网线设置
    def dakai_wangxian_shezhi_gui(self):
        r"""打开网线设置"""
        s("control netconnections")
        # s("rundll32.exe shell32.dll,Control_RunDLL ncpa.cpl")

    # 查看本机ip
    def chakan_ip(self):
        host_name = socket.gethostname()
        try:
            host_ip_list = socket.gethostbyname_ex(host_name)[2]
            print(*host_ip_list)
            return host_ip_list
        except socket.gaierror:
            return []

    # 立刻关机
    def guanji_0s(self):
        r"""立刻关机"""
        s("shutdown /s /t 0")

    # 几秒关机
    def guanji(self,miao):
        r"""几秒关机"""
        s(f"shutdown /s /t {str(miao)}")
        print(f"你的电脑即将{miao}秒关机!")

    # 立刻重启
    def chongqi_0s(self):
        r"""立刻重启"""
        s("shutdown /r /t 0")

    # 取消关机 取消重启
    def guanji_quxiao(self):
        r"""关机取消 重启取消"""
        s("shutdown /a")
        print("已经 取消关机/重启!")

    # 几秒关机
    def guanji_subprocess(self, miao):
        r"""几秒关机"""
        # import subprocess
        subprocess.run(["shutdown", "/s", "/t", str(miao)])
        print(f"你的电脑即将{miao}秒关机!")

    # 删除共享
    def shanchu_moren_gongxiang(self):
        r"""删除共享"""
        share_mulu = [
            "C$",
            "D$",
            "E$",
            "IPC$",
            "ADMIN$"
        ]

        for share_name in share_mulu:
            try:
                os.system(f"net share {share_name} /delete")
                print(f"成功删除共享: {share_name}")
            except Exception as e:
                print(f"删除共享 {share_name} 时出错: {e}")

    # 删除文件
    def shanchu_wenjian(self,file_path):
        r"""删除文件"""
        # shell=True  文件有空格 加上这个 有效果
        subprocess.run(["del", file_path],check=True, shell=True)
        print(f"{file_path} 已经删除!")

    # 清空目录 留目录
    def qingkong_mulu_cmd_liumulu(self,mulu_path):
        r"""清空目录 留目录"""
        # subprocess.run(["del", "/q", "/s", mulu_path+r"\*"], check=True, shell=True)
        # print(f"{mulu_path} 已经清空!")

        m = f"""del /q /s "{mulu_path}\\*" """
        os.system(m)
        print(f"{mulu_path} 已经清空! 但是还有目录骨架")

    # 清空目录 不留目录
    def qingkong_mulu_buliu_mulu(self,mulu_path):
        shutil.rmtree(mulu_path)  # 删除目录
        os.makedirs(mulu_path, exist_ok=True)

    # 模拟数据
    def moni_shuju_xinjian(self):
        r"""模拟数据"""
        r"""
        使用python创建一个父目录 多个子目录 每个子目录下面存放一些模拟文件 比如图片 txt 表格
        """
        # 模拟数据默认放在 桌面 0001_rsgz__data_moni
        fu = r"C:\Users\Administrator\Desktop\0001_rsgz__data_moni"
        os.makedirs(fu, exist_ok=True)
        print(f"你的模拟数据在：{fu}")


        # 创建子目录
        zi_mulu = ["pic","txt","图像","txt 文件"]
        for zi in zi_mulu:
            os.chdir(fu)
            os.makedirs(zi, exist_ok=True)
            os.chdir(j(fu,zi))
            file_type = random.choice(['.txt', '.jpg', '.csv',".png"])  # 随机选择文件类型
            file_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + file_type
            print(f"模拟数据: {file_name}")

            # 创建模拟数据
            with open(file_name, 'w') as f:
                if file_type == '.txt':
                    f.write('This is a mock text file.')
                elif file_type == '.csv':
                    f.write('col1,col2,col3\n1,2,3\n4,5,6')
                elif file_type == '.jpg':
                    f.write("This is a jpg picture file.")
                elif file_type == '.png':
                    f.write("This is a png picture file.")

    # 删除模拟数据
    def moni_shuju_shanchu(self):
        r"""删除模拟数据"""
        fu = r"C:\Users\Administrator\Desktop\0001_rsgz__data_moni"
        subprocess.run(["rd", "/q", "/s", fu], check=True, shell=True)
        print("模拟数据 目录已经删除")

    # 新建 目录
    def xinjian_mulu(self,mulu_path):
        r"""新建 目录"""
        os.makedirs(mulu_path, exist_ok=True)

    # 新建txt
    def xinjian_txt(self,txt_path):
        r"""新建txt"""
        s(f'type null>"{txt_path}"')

    # 锁屏
    def suoping_cmd(self):
        r"""锁屏"""
        s(r"%windir%\System32\rundll32.exe user32.dll,LockWorkStation")

    # 关闭垃圾进程
    def guanbi_laji_jincheng_wmic(self):
        r"""关闭垃圾进程"""
        laji_app=["MultiTip.exe","360huabao.exe","360SpeedldHealth.exe","webapp.exe","ZhuDongFangYu.exe"]
        for app in laji_app:
            # s(f"""wmic process where "name='360huabao.exe'" call terminate""")
            s(f"""wmic process where "name='{app}'" call terminate""")

    # 关闭进程
    def guanbi_jincheng_wmic(self,app):
        r"""关闭进程"""
        s(f"""wmic process where "name='{app}'" call terminate""")

    #



if __name__ == '__main__':
    c=Cmd()
    # c.xinjian_cmd_file(fumulu=r"C:\Users\Administrator\Desktop\0001_rsgz__data_moni")

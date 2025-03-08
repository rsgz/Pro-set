import os,inspect,shutil
import subprocess
import ctypes

class Mulu():
    def __init__(self):
        pass

    # 合并路径
    def hebing_path(self,*args):
        r"""合并路径"""
        return os.path.join(*args)

    # 父目录
    def fumulu(self,path):
        r"""父目录"""
        return os.path.dirname(path)

    # 项目文件路径 指的是调用者的 源码路径
    def yuanma_path(self):
        r"""项目文件路径"""
        # return os.path.abspath(path)  这种写法 调用的时候 必须传参 __file__
        # 获取调用者的栈信息
        caller_frame = inspect.stack()[1]  # 获取调用者的帧信息
        caller_file = caller_frame.filename  # 获取调用者的文件路径
        return os.path.abspath(caller_file)

    # 项目文件名字
    def yuanma_base_path(self):
        r"""项目文件名字"""
        # return os.path.basename(path)  这种写法 调用的时候 必须传参 __file__
        # 获取调用者的栈信息
        caller_frame = inspect.stack()[1]  # 获取调用者的帧信息
        caller_file = caller_frame.filename  # 获取调用者的文件路径
        return os.path.basename(caller_file)

    # 工作路径
    def work_dir(self):
        r"""返回工作路径"""
        return os.getcwd()

    # 切换解释器路径
    def cd(self,path):
        r"""切换工作路径 只对python解释器的工作目录有用 有时候对cmd是无效的"""
        os.chdir(path)

    # 后缀名
    def houzhuiming(self,path):
        r"""获取后缀名 .jpg"""
        return os.path.splitext(path)[-1]

    # 返回文件名
    def get_wenjian_name(self,path):
        r"""返回文件名"""
        return os.path.basename(path)

    # 清空多个目录
    def qingkong_mulu_set(self,mulu_str):
        r"""清空多个目录"""
        import os
        z = os.system

        # mulu_str = r"""
        # E:\up1230b-1\StaticFiles\*
        # E:\up1230b-2\StaticFiles\*
        # E:\up1230b-1\App_Data\Logs\*
        # E:\up1230b-2\App_Data\Logs\*
        # """
        if type(mulu_str)==str:
            path_set = [line.strip('"') for line in mulu_str.splitlines() if line.strip()]
            print(*path_set, sep="\n")

            for p in path_set:
                m = f"""del /q /s "{p}\\*" """
                z(m)
                print(f"{p} 清除成功!")
        if type(mulu_str)==list or type(mulu_str)==tuple:
            for p in mulu_str:
                m = f"""del /q /s "{p}\\*" """
                z(m)
                print(f"{p} 清除成功!")

    # 清空一个目录
    def qingkong_mulu_one(self,mulu_path):
        r"""清空一个目录"""
        m = f"""del /q /s "{mulu_path}\\*" """
        os.system(m)

    # 删除一个目录
    def shanchu_mulu_one(self,mulu_path):
        r"""删除一个目录"""
        m=f"""rd /s /q "{mulu_path}" """
        os.system(m)
        print(f"{mulu_path} 删除成功!")

    # 删除多个目录
    def shanchu_mulu_set(self,mulu_str):
        r"""删除多个目录"""
        z = os.system

        # mulu_str = r"""
        # E:\up1230b-1\StaticFiles\*
        # E:\up1230b-2\StaticFiles\*
        # E:\up1230b-1\App_Data\Logs\*
        # E:\up1230b-2\App_Data\Logs\*
        # """
        if type(mulu_str)==str:
            path_set = [line.strip('"') for line in mulu_str.splitlines() if line.strip()]
            print(*path_set, sep="\n")

            for p in path_set:
                m = f"""rd /s /q "{p}" """
                z(m)
                print(f"{p} 删除成功!")
        if type(mulu_str)==list or type(mulu_str)==tuple:
            for p in mulu_str:
                m = f"""rd /s /q "{p}" """
                z(m)
                print(f"{p} 删除成功!")

    # 复制目录到哪里
    def fuzhi_mulu_to(self,mulu,to_mulu):
        r"""复制目录到哪里"""
        shutil.copytree(mulu, to_mulu)

    # 打开目录
    def dakai_mulu(self,mulu):
        r"""打开目录"""
        os.startfile(mulu)

    # 是目录还是文件
    def is_mulu_or_wenjian(self,path):
        r"""是目录还是文件"""
        if os.path.isdir(path):
            print("是目录")
        elif os.path.isfile(path):
            print("是文件")
        else:
            print("是特殊文件 (socket,FIFO,device file)")

    # 获取环境变量值
    def get_huanjing_bianliang_zhi_cmd(self,name):
        """使用 subprocess 获取环境变量的值"""
        # import subprocess
        try:
            # Windows 系统
            result = subprocess.run(["cmd", "/c", f"echo %{name}%"], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            return None  # 命令执行失败
        except FileNotFoundError:
            return None  # 命令没有找到

    # 打印所有环境变量值
    def get_huanjing_bianliang_zhi_python(self,name):
        r"""打印所有环境变量值"""
        existing_value = os.environ.get(name, "")
        if existing_value:
            v_l = existing_value.split(";")
            print(*v_l,sep="\n")

    # 设置环境变量
    def shezhi_huanjing_bianliang_zhuijia(self,name, value):
        """使用 setx /m 追加设置永久环境变量"""
        # 获取现有的环境变量值
        existing_value=self.get_huanjing_bianliang_zhi_cmd(name=f"{name}")
        # 判断是否已经存在该环境变量
        if existing_value:
            print(f"已经存在的旧值：{existing_value}")
            # 如果已经存在，追加新的值
            new_value = f"{existing_value};{value}"  # Windows 使用分号分隔
        else:
            # 如果不存在，直接设置新的值
            new_value = value

        # 使用 setx /m 设置环境变量
        command = f'setx /m {name} "{new_value}"'
        os.system(command)

        zuixin_value = os.environ.get(name, "")
        print(f"最新值:{zuixin_value}")

    # 设置PYTHONPATH环境变量
    def shezhi_python_mokuai_sousuo_lujing(self,pro_fu_lujing):
        r"""设置PYTHONPATH环境变量 就是项目的父目录"""
        self.shezhi_huanjing_bianliang_zhuijia(name="PYTHONPATH", value=pro_fu_lujing)
        print("PYTHONPATH",f"---> {pro_fu_lujing}  设置成功!")


if __name__ == '__main__':
    p = Mulu()
    # p.get_huanjing_bianliang_zhi_python(name="path")
    p.get_huanjing_bianliang_zhi_python(name="PYTHONPATH")
import os,inspect,shutil
import subprocess
import ctypes

class Mulu():
    def __init__(self):
        pass

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
    m = Mulu()
    f=os.path.dirname
    dangqian = os.path.abspath(__file__)
    pro_fu_lujing=f(f(f(dangqian)))
    print("经过分析，你要添加PYTHONPATH的模块搜索路径是",pro_fu_lujing)
    m.shezhi_python_mokuai_sousuo_lujing(pro_fu_lujing=pro_fu_lujing)


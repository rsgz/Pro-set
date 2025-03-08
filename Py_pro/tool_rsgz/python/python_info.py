import os,sys,pip

class Python_Info:
    def __init__(self):
        pass
    # 获取解释器位置
    def get_python_where(self):
        r"""
        获取 你现在运行的python解释器 位置在哪里
        """
        print(sys.executable)
        return sys.executable

    # 获取解释器版本
    def get_python_version(self):
        r"""获取python版本"""
        print(sys.version)
        return sys.version

    # 获取解释器安装路径
    def get_python_install_path(self):
        r"""获取python安装路径"""
        print(sys.prefix)
        return sys.prefix

    # 获取搜索路径
    def get_python_sousuo_path(self):
        r"""Python 搜索路径:"""
        print("Python 搜索路径:")
        for path in sys.path:
            print(path)

    # win10所有python解释器路径
    def get_suoyou_python(self):
        r"""获取本地所有python"""
        os.system("where python")

    # 判断 在虚拟环境中吗
    def is_xuni_huanjing_zhong(self):
        r"""判断是不是在虚拟环境中"""
        if hasattr(sys, 'real_prefix'):
            print("当前处于虚拟环境中")
            print("虚拟环境路径:", sys.prefix)
        else:
            print("当前处于系统 Python 环境中")
            print("系统 Python 路径:", sys.prefix)

    # print(os.environ.get('PATH'))

    # 获取pip版本
    def get_pip_version(self):
        r"""获取pip版本"""
        print(pip.__version__)
        return pip.__version__

    # 获取pip模块路径
    def get_pip_mokuai_path(self):
        r"""获取pip模块路径"""
        print(pip.__file__)
        return pip.__file__

    # 获取win10所有pip
    def get_suoyou_pip(self):
        r"""获取系统所有pip位置"""
        os.system("where pip")


if __name__ == '__main__':
    p = Python_Info()
    # Python_Info().get_python_where()
    # Python_Info().get_python_version()
    # Python_Info().get_python_install_path()
    # Python_Info().get_suoyou_python()
    # p.is_xuni_huanjing_zhong()
    # p.get_pip_version()
    print(p.get_python_sousuo_path())
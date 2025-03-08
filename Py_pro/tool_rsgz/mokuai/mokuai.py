import inspect

class Mokuai_Fenxi:
    def __init__(self):
        pass

    def print_suoyou_chengyuan(self,cls):
        r"""
        打印所有成员 包含 属性 方法 函数   cls 参数 传一个类进去
        """
        print(f"类名: {cls.__name__}")
        print("所有成员：")
        for name in dir(cls):
            print(f"  - {name}")

    def print_fangfa_hanshu(self,cls):
        r"""
        获取 所有类里面的方法和函数 并且有 文字注释
        """
        print("\n方法和函数：")
        for name, member in inspect.getmembers(cls, inspect.isfunction):
            doc = member.__doc__.strip() if member.__doc__ else "无注释"  # 获取文档字符串
            print(f"  - 函数: {name}  {doc}")

        for name, member in inspect.getmembers(cls, inspect.ismethod):
            doc = member.__doc__.strip() if member.__doc__ else "无注释"  # 获取文档字符串
            print(f"  - 方法: {name}  {doc}")

    def print_shuxing(self,cls):
        r"""
        获取 所有类里面的属性
        """
        print("\n属性：")
        for name, value in vars(cls).items():
            if not callable(value):  # 排除函数和方法
                print(f"  - 属性: {name}")

    def print_all(self,cls):
        r"""
        打印 类里面所有的 属性 函数 方法
        """
        self.print_suoyou_chengyuan(cls)
        self.print_fangfa_hanshu(cls)
        self.print_shuxing(cls)

if __name__ == '__main__':
    from tool_rsgz.time.time import Time
    # Mokuai_Fenxi().print_all(cls=Time)
    # Mokuai_Fenxi().print_fangfa_hanshu(cls=Time)

    m = Mokuai_Fenxi()
    m.print_fangfa_hanshu(Time)
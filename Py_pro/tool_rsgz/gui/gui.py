from tkinter import messagebox

class Gui:
    def __init__(self):
        pass

    def tishi_gui(self,infos):
        # 创建主窗口并隐藏之（因为我们只想要一个消息框）
        # root = tk.Tk()
        # root.withdraw()  # 隐藏主窗口

        # 显示消息框
        messagebox.showinfo("提示", infos)

        # 如果您希望程序在此等待用户关闭消息框后才退出，可以添加如下代码：
        # root.mainloop()
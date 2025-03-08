import subprocess
import urllib.parse
import time


class Yingyong:
    def __init__(self):
        pass

    # 打开everything 搜索
    def dakai_everything_sousuo(self, query):
        r"""打开everything 搜索"""
        """
        发送搜索查询到Everything，并确保路径中的空格和其他特殊字符被正确编码。
        :param query: 要搜索的字符串或路径
        """
        # 对查询中的特殊字符进行URL编码
        encoded_query = urllib.parse.quote(query)
        # 使用Everything的URI scheme来触发搜索
        search_url = f"es:{encoded_query}"
        subprocess.Popen(['start', search_url], shell=True)

    # 批量打开everything搜索
    def dakai_everything_sousuo_piliang(self, path_list):
        r"""批量打开everything搜索"""
        path_list = [
            r"E:\pic\shangpin\800x800",
            r"E:\pic\leimu\Hoodies\800x800",
            r"E:\pic\leimu\Coats\800x800",
        ]

        for path in path_list:
            self.dakai_everything_sousuo(path)
            # 为了避免所有搜索同时发起导致界面混乱，可以在每次搜索之间添加一个小延迟
            time.sleep(0.8)

    def guanbi_everything_gui(self):
        """
        使用taskkill命令关闭所有Everything进程。
        """
        # 使用taskkill命令，/IM指定要关闭的程序映像名称，/F表示强制终止
        try:
            subprocess.run(["taskkill", "/IM", "Everything.exe", "/F"], check=True)
        except Exception as e:
            print(e)




if __name__ == '__main__':
    y = Yingyong()
    y.guanbi_everything_gui()
    path_list=r"""
    r"E:\pic\shangpin\800x800",
            r"E:\pic\leimu\Hoodies\800x800",
            r"E:\pic\leimu\Coats\800x800",
    """
    # y.dakai_everything_sousuo_piliang(path_list)
import subprocess
import urllib.parse
import time

def open_everything_search(query):
    """
    发送搜索查询到Everything，并确保路径中的空格和其他特殊字符被正确编码。

    :param query: 要搜索的字符串或路径
    """
    # 对查询中的特殊字符进行URL编码
    encoded_query = urllib.parse.quote(query)
    # 使用Everything的URI scheme来触发搜索
    search_url = f"es:{encoded_query}"
    subprocess.Popen(['start', search_url], shell=True)

if __name__ == '__main__':
    # 示例搜索路径列表
    paths_to_search = [
                          r"E:\pic\shangpin\800x800",
                          r"E:\pic\leimu\Hoodies\800x800",
                          r"E:\pic\leimu\Jackets\800x800",
                          r"E:\pic\leimu\Sweater\800x800",
                          r"E:\pic\leimu\T-Shirts\800x800",
                          r"E:\pic\leimu\Blouses\800x800",
                      r"E:\pic\leimu\Pants\800x800",
                      r"E:\pic\leimu\Dress\800x800",
                      r"E:\pic\leimu\Skirt\800x800",
                      r"E:\pic\leimu\Party Dress\800x800",
                      r"E:\pic\leimu\Mini Dresses\800x800",
    ]

    for path in paths_to_search:
        open_everything_search(path)
        # 为了避免所有搜索同时发起导致界面混乱，可以在每次搜索之间添加一个小延迟
        time.sleep(0.8)
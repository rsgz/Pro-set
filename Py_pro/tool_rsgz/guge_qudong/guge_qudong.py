from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from tool_rsgz.str.str import Str

r"""
pip install selenium -i https://mirrors.aliyun.com/pypi/simple
"""


class Guge_qudong:
    def __init__(self):
        self.s=Str()
        pass

    # 创建 google driver
    def xinjian_google_driver(self,IP_Port, chromedriver):
        r"""
        这个函数 用来创建谷歌driver
        # "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9530 --no-first-run --no-default-browser-check --user-data-dir="C:\Users\Administrator\Desktop\芒果代码\改价格\user_data"
        IP_Port = "127.0.0.1:9530"
        chromedriver = "F:\python\chromedriver.exe"
        browser = creat_google_driver(IP_Port, chromedriver)
        返回 browser,service
        """
        service = Service(chromedriver)
        service.command_line_args()
        service.start()

        options = Options()
        options.add_experimental_option("debuggerAddress", IP_Port)  # 这个IP 和端口 不要改动

        browser = webdriver.Chrome(service=service, options=options)  # service接收谷歌驱动 options接收 IP 和端口
        return browser, service

    # 输出谷歌浏览器 驱动配置信息
    def shezhi_guge_liulanqi_xinxi(self):
        r"""输出谷歌浏览器 驱动配置信息"""
        f1 = r'''
        方法1：
        "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9530 --no-first-run --no-default-browser-check --user-data-dir="C:\Users\Administrator\Desktop\芒果代码\改价格\user_data"
        '''

        l=self.s.str_to_list(u_str=f1)
        print(*l,sep="\n")

    # 谷歌搜索技巧
    def guge_sousuo_jiqiao(self):
        f1 = r'''
            关键字 site:www.amazon.com dress
            图片  www.amazon.com dress 1464*600
            txt site:*.*.* 抖音富婆通讯录 filetype:txt
        '''
        l=self.s.str_to_list(u_str=f1)
        print(*l,sep="\n")

if __name__ == '__main__':
    g=Guge_qudong()
    IP_Port = "127.0.0.1:9530"
    chromedriver = r"F:\python\chromedriver.exe"
    # browser = g.xinjian_google_driver(IP_Port, chromedriver)
    # print(browser.title)

    g.shezhi_guge_liulanqi_xinxi()
    g.guge_sousuo_jiqiao()
import requests
from settings import authorization
import customtkinter as ctk
import requests
from threading import Thread
import time


# weketu 操作逻辑
import pyautogui,os
import time
from tool_rsgz.find_pic.find_pic import find_pic_click_center_keep,find_pic_move_center,gdiScreenCapture

r"""
pip install customtkinter requests

写一个简单的 gui界面 最新版的 customtkinter
上方 有两个按钮  开始 关闭
点击开始按钮 就隔20秒钟 执行 
def get_kucun():
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    data = response.json()
    zong_ku_ucn = data['response']['recordCount']
    print("总库存：",zong_ku_ucn)
    return zong_ku_ucn

这个函数 把 zong_ku_ucn 渲染到 gui上面

点击关闭按钮 就停止 这个过程 
"""

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'goods.search',
    'authorization': authorization,
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://b08-admin.shop6888.com',
    'priority': 'u=1, i',
    'referer': 'https://b08-admin.shop6888.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

json_data = {
    'pageIndex': 1,
    'pageSize': 20,
    'searchHierarchyMethod': 3,
}

# def get_kucun():
#     response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
#     data = response.json()
#     zong_ku_ucn = data['response']['recordCount']
#     print("总库存：",zong_ku_ucn)
#     return zong_ku_ucn

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.kucun_zengliang=0
        self.kucun=0
        self.title("库存查询")
        self.geometry("300x290")

        self.running = False

        # 创建并放置开始按钮
        self.start_button = ctk.CTkButton(master=self, text="开始 库存监控", command=self.start_process)
        self.start_button.pack(pady=10)

        # 创建并放置关闭按钮
        self.stop_button = ctk.CTkButton(master=self, text="关闭 库存监控", command=self.stop_process)
        self.stop_button.pack(pady=10)

        # 刷新 任务按钮
        self.shuaxin_button = ctk.CTkButton(master=self, text="刷新任务", command=self.start_shuaxin_renwu_process)
        self.shuaxin_button.pack(pady=10)

        # 刷新 任务按钮
        self.lianxu_kaiqi_button = ctk.CTkButton(master=self, text="连续开启", command=self.lianxu_kaiqi_process)
        self.lianxu_kaiqi_button.pack(pady=10)

        # 创建并放置用于显示库存的标签
        self.label = ctk.CTkLabel(master=self, text="")
        self.label.pack(pady=20)

    # 监控库存
    def start_process(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.run_periodically)
            self.thread.start()

    def stop_process(self):
        self.running = False

    def run_periodically(self):
        while self.running:
            now = int(time.time())  # 获得当前时间时间戳
            timeArray = time.localtime(now)  # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

            result = self.get_kucun()
            self.label.configure(text=f"总库存：{otherStyleTime}\n{result}--->+{self.kucun_zengliang}")
            for _ in range(20):  # 每20秒检查一次是否需要停止，以允许更精细的控制
                if not self.running:
                    break
                time.sleep(1)

    # 刷新任务 线程
    def start_shuaxin_renwu_process(self):
        self.thread = Thread(target=self.start_shuaxin_renwu)
        self.thread.start()

    # 连续开启 线程
    def lianxu_kaiqi_process(self):
        self.thread = Thread(target=self.lianxu_kaiqi_func)
        self.thread.start()

    # 连续开启 函数
    def lianxu_kaiqi_func(self):
        os.chdir(r"D:\0-code\youmi_pro")
        xy = find_pic_move_center(small=r".\weketu\004.jpg", big=gdiScreenCapture(), xiangsidu=0.90)
        x = int(xy[0])

        os.chdir(r"C:\Users\Administrator\Desktop")
        # os.chdir(r"D:\0-code\youmi_pro")
        os.rename("x.exe", f"{x}.exe")
        os.system(f"{x}.exe")
        time.sleep(2)
        os.rename(f"{x}.exe", "x.exe")

    # 刷新任务
    def start_shuaxin_renwu(self):
        i=0
        while self.running==True:
            if self.running==False:
                break
            time.sleep(8)
            # cli_set = [(123,1058),(123+47,1058),(123+47*2,1058),(123+47*3,1058)]
            cli_set = [(450,1058),(600,1058),(750,1058),(900,1058)]
            x=cli_set[i%4][0]
            y=cli_set[i%4][1]
            pyautogui.click(x=x, y=y, duration=0.1)  # 点击
            i=i+1

            os.chdir(r"D:\0-code\youmi_pro")
            pyautogui.moveTo(500, 500)
            time.sleep(1)
            pyautogui.rightClick()
            find_pic_click_center_keep(small=r".\weketu\001.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
            find_pic_click_center_keep(small=r".\weketu\002.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
            time.sleep(1)
            pyautogui.moveTo(500, 500)
            pyautogui.rightClick()
            find_pic_click_center_keep(small=r".\weketu\003.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
            find_pic_click_center_keep(small=r".\weketu\002.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
            time.sleep(8)
            xy = find_pic_move_center(small=r".\weketu\004.jpg", big=gdiScreenCapture(), xiangsidu=0.90)
            x = int(xy[0])

            os.chdir(r"C:\Users\Administrator\Desktop")
            os.rename("x.exe", f"{x}.exe")
            os.system(f"{x}.exe")
            time.sleep(2)
            os.rename(f"{x}.exe", "x.exe")

    def get_kucun(self):
        try:
            # response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
            response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
            data = response.json()
            zong_ku_ucn = data['response']['recordCount']
            print("总库存：", zong_ku_ucn)
            self.kucun_zengliang=zong_ku_ucn-self.kucun
            self.kucun = zong_ku_ucn
            return zong_ku_ucn
        except Exception as e:
            print(f"Error: {e}")
            return "获取失败"

if __name__ == "__main__":
    app = App()
    app.mainloop()
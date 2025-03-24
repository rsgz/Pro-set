import requests
from settings import authorization
import customtkinter as ctk
import requests
from threading import Thread
import time

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

        self.title("库存查询")
        self.geometry("300x200")

        self.running = False

        # 创建并放置开始按钮
        self.start_button = ctk.CTkButton(master=self, text="开始", command=self.start_process)
        self.start_button.pack(pady=10)

        # 创建并放置关闭按钮
        self.stop_button = ctk.CTkButton(master=self, text="关闭", command=self.stop_process)
        self.stop_button.pack(pady=10)

        # 创建并放置用于显示库存的标签
        self.label = ctk.CTkLabel(master=self, text="")
        self.label.pack(pady=20)

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
            self.label.configure(text=f"总库存：{otherStyleTime}\n{result}")
            for _ in range(20):  # 每20秒检查一次是否需要停止，以允许更精细的控制
                if not self.running:
                    break
                time.sleep(1)

    def get_kucun(self):
        try:
            # response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
            response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
            data = response.json()
            zong_ku_ucn = data['response']['recordCount']
            print("总库存：", zong_ku_ucn)
            return zong_ku_ucn
        except Exception as e:
            print(f"Error: {e}")
            return "获取失败"

if __name__ == "__main__":
    app = App()
    app.mainloop()
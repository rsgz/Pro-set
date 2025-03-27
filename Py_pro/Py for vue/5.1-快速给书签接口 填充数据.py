r"""
pip install requests
"""
import requests,random



# 定义URL和数据
url = "http://127.0.0.1:8081/api/bookmarks"

def suiji_one_hang(txt):
    s= random.choice([line.strip().split() for line in open(txt, 'r', encoding='utf-8') if line.strip()])[0]
    print(s)
    return s
# data = {
#     "id": "1",
#     "name": "迪迦",
#     "purpose": "娱乐",
#     "source": "小红书",
#     "tag": "AI,GPT",
#     "url": "https://tongyi.xxx.com/"
#  }

data = {
    "id": "1",
    "name": suiji_one_hang(txt="data/url_name.txt"),
    "purpose": suiji_one_hang(txt="data/yong_tu.txt"),
    "source": suiji_one_hang(txt="data/ping_tai.txt"),
    "tag": suiji_one_hang(txt="data/biao_qian.txt"),
    "url": suiji_one_hang(txt="data/url.txt")
 }

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

for i in range(0,250):
    data = {
        "id": "1",
        "name": suiji_one_hang(txt="data/url_name.txt"),
        "purpose": suiji_one_hang(txt="data/yong_tu.txt"),
        "source": suiji_one_hang(txt="data/ping_tai.txt"),
        "tag": suiji_one_hang(txt="data/biao_qian.txt"),
        "url": suiji_one_hang(txt="data/url.txt")
    }
    response = requests.post(url, json=data, headers=headers)
    # 打印响应内容
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
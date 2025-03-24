r"""
pip install requests
"""

import requests

# 定义URL和数据
url = "http://127.0.0.1:8081/api/bookmarks"
data = {
    "id": "1",
    "name": "迪迦",
    "purpose": "娱乐",
    "source": "小红书",
    "tag": "AI,GPT",
    "url": "https://tongyi.xxx.com/"
 }

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

for i in range(0,280):
    # response = requests.post(url, json=data, headers=headers)
    response = requests.post(url, json=data)
    # 打印响应内容
    print("Status Code:", i,response.status_code)
    print("Response Body:", response.text)

import requests
from youmi_pro.settings import *

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-website.search',
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
    # 'pageSize': 4000,
    'pageSize': 4000,
}

response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
web_list = response.json()['response']['items']
# print(web_list)

shopServerId_num={
    1:"1 - 美国洛杉矶 (199.33.126.154:59880)",
    3:"3 - 美国加利福尼亚 (199.33.127.106:22)",
    4:"4 - 第三台服务器 (199.33.122.90:22)",
    5:"(45.136.118.6:20566)",
}

start=216
end=479
for web in web_list:
    id = web["id"]
    if start<=id<=end:
        domain=web["domain"]
        memo=web["memo"]
        goodsCount=web['goodsCount']
        shopServerId=web["shopServerId"]
        # s=f"{id} {domain} {memo} 产品数量:{goodsCount} 服务器：{shopServerId_num[shopServerId]}"
        # s=f'"{id}":"{domain}",'
        s=f'{domain}'
        print(s)


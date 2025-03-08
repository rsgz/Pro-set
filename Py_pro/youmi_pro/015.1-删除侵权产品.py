import requests
from settings import authorization
# pip install aiohttp

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'goods.delete-batch',
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

qinquan_l = [
"Bogner",
"Moncler",
"canada goose",
"abuse",
"Clothes Mentor",
"DANDY WORLDWIDE",
"Bharat Kapoor",
"TIMBERLAND",
"Fire+Ice",
"Willy Bogner GmbH",
"Let's Watch the Sunset",
# "Maje",
"Marq Vision",
"Gestuz"
]

for qinquan in qinquan_l:
    json_data = {
        'keywords': qinquan,
        'searchHierarchyMethod': 3,
        'limitCount': 20000,
    }
    print("侵权词：↓↓↓↓↓↓↓↓↓↓ {} ↓↓↓↓↓↓↓↓↓↓".format(qinquan))
    # requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print("状态:",response.json()["message"])
    # print(response.json()["status"])

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"keywords":"Bogner","searchHierarchyMethod":3,"limitCount":20000}'
#response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, data=data)
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods-classification.read-all',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOiIxIiwiVXNlckFjY291bnRJZCI6IjEiLCJOaWNrbmFtZSI6IueUsOS8r-WFiSIsIlJvbGUiOiJhZG1pbiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJhZG1pbiIsImV4cCI6MTczOTY3MTYzOCwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MjAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MjAwIn0.zhzVVwTKX90nMl8PzDTi7EqXdEPmxrvHKMzoD1DyEVw',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://b03-admin.shop6888.com',
    'priority': 'u=1, i',
    'referer': 'https://b03-admin.shop6888.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

json_data = {
    'websiteId': 1041,
}

response = requests.post('https://b03-api.shop6888.com/apis/Action', headers=headers, json=json_data)
print(response)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"websiteId":1041}'
#response = requests.post('https://b03-api.shop6888.com/apis/Action', headers=headers, data=data)
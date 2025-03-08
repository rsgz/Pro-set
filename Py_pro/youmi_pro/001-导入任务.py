import requests
from settings import authorization,startx,endx,zuojige

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods-data-import-task.add',
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

classificationIds = ["2251937252638720","2252074725146624","2252349603053568","2252349770825728","2252487025229824","2252487109115904","2252624682287104","2252624464183296","2252761936691200","2252761919913984"]
# start=920
start=startx
for websiteId in range(start+1,start+zuojige):
# for websiteId in range(start+1,endx+1):
    json_data = {
        'websiteId': websiteId,
        'minCount': 400,
        'maxCount': 400,
        # 'classificationIds': ["2251937252638720","2252074725146624","2252349770825728","2252487025229824","2252487042007040","2252487310442496","2252624464183296","2252761936691200","2252762054131712","2252761919913984"],
        'classificationIds': classificationIds,
        'usageTimes': 0,
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print(websiteId,response)
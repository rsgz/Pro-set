import requests
from settings import authorization

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


web_indfos = [
(973,"https://cccm.fun",4992,8),
(972,"https://bbby.fun",4989,11),
(970,"https://ccch.fun",4995,5),
(963,"https://iiic.fun",4980,20),
(962,"https://iiit.fun",4983,17),
(955,"https://iiij.fun",4997,3),
(954,"https://hhhv.fun",4999,1),
(952,"https://iiio.fun",4999,1),
(951,"https://jjjk.fun",4999,1),
(950,"https://jjjz.fun",4997,3)
]

# start,end=216,949
for id,yuming,num,quekou_num in (web_indfos):
    print(id,yuming,num,quekou_num)
    try :
        json_data = {
            'websiteId': id,
            'minCount': quekou_num,
            'maxCount': quekou_num,
            'classificationIds': [
                '2252761936691200',
            ],
            'usageTimes': 0,
        }

        response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    except:
        print(id,"导入产品有问题")
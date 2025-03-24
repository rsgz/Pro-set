import requests
from settings import authorization

# 这个使用 一定要注意
start,end = 999,1018
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-website.save.header-menu',
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

for websiteId in range(start,end+1):
    json_data = {
        'websiteId': websiteId,
        'menuItems': [
            {
                'title': 'Hoodies & Sweatshirts ',
                'url': '/womensclothing-hoodiessweatshirts-1',
            },
            {
                'title': "Women's Jackets ",
                'url': '/womensclothing-outerwear-womensjackets-1',
            },
            {
                'title': 'Sweater ',
                'url': '/womensclothing-sweaters-sweater-1',
            },
            {
                'title': 'T-Shirts',
                'url': '/womensclothing-tops-t-shirts-t-1',
            },
            {
                'title': 'Blouses ',
                'url': '/womensclothing-tops-blousesshirts-blouses-1',
            },
            {
                'title': 'Pants ',
                'url': '/womensclothing-bottoms-pants-1',
            },
            {
                'title': 'Dress',
                'url': '/womensclothing-dresses-dress-1',
            },
            {
                'title': 'Skirt ',
                'url': '/womensclothing-dresses-skirt-1',
            },
            {
                'title': 'Party Dress',
                'url': '/womensclothing-dress-party-wear-1',
            },
            {
                'title': 'Mini Dresses',
                'url': '/womensclothing-dresses-mini-1',
            },
        ],
    }
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print(websiteId, response)

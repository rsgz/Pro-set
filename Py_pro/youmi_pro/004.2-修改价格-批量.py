import requests
from settings import authorization,startx,endx,zuojige,qujian

# 'shop-goods.reset-selling-price-random-floating'  售价
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods.reset-selling-price-random-floating',
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

# 'shop-goods.reset-market-price-random-floating-rate'  市场价
headers2 = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods.reset-market-price-random-floating-rate',
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

for websiteId in range(startx,endx+1):
# for websiteId in qujian:
    # 网站编号
    # websiteId = 524
    print("↓↓↓↓↓↓↓↓↓↓{}↓↓↓↓↓↓↓↓↓↓↓".format(websiteId))

    # 售价整体范围
    json_data = {
        'options': {
            'searchHierarchyMethod': 3,
            'websiteId': websiteId,
        },
        'minUnitPrice': 45,
        'maxUnitPrice': 70,
    }
    # 整体售价范围
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print("整体售价:{}".format(response))

    # 修改售价
    def shoujia(websiteId,name,id,headers,minUnitPrice,maxUnitPrice):
        r"""
        websiteId  websiteId
        name 连帽衫
        id  类目id   2251937252638720
        headers headers
        minUnitPrice  35
        maxUnitPrice  39
        """
        # 1 连帽衫
        json_data = {"options":{"classificationId":id,"searchHierarchyMethod":3,"websiteId":websiteId},"minUnitPrice":minUnitPrice,"maxUnitPrice":maxUnitPrice}
        response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
        print(f"{name}:{response.json()}")

    # 这个变量没卵用

    # 主要是在这里 name id 填写好 然后价格区间
    shoujia(websiteId=websiteId, name="Hoodies & Sweatshirts 连帽衫和运动衫", id="2251937252638720", headers=headers,
            minUnitPrice=39, maxUnitPrice=45)
    shoujia(websiteId=websiteId, name="T-Shirts T恤衫", id="2252487025229824", headers=headers, minUnitPrice=27,
            maxUnitPrice=37)
    shoujia(websiteId=websiteId, name="Legging 紧身裤", id="2252624531304448", headers=headers, minUnitPrice=35,
            maxUnitPrice=48)
    shoujia(websiteId=websiteId, name="Pants 长裤", id="2252624464183296", headers=headers, minUnitPrice=31,
            maxUnitPrice=42)
    shoujia(websiteId=websiteId, name="Sweatpants 运动裤", id="2252624564846592", headers=headers, minUnitPrice=33,
            maxUnitPrice=46)
    shoujia(websiteId=websiteId, name="Jeans 牛仔裤", id="2252624598401024", headers=headers, minUnitPrice=38,
            maxUnitPrice=55)
    shoujia(websiteId=websiteId, name="Dress 连衣裙", id="2252761936691200", headers=headers, minUnitPrice=55,
            maxUnitPrice=68)
    shoujia(websiteId=websiteId, name="Party Dress 派对礼服", id="2252761919913984", headers=headers, minUnitPrice=55,
            maxUnitPrice=68)
    shoujia(websiteId=websiteId, name="Mini Dresses 迷你连衣裙", id="2252761987022848", headers=headers, minUnitPrice=38,
            maxUnitPrice=58)
    shoujia(websiteId=websiteId, name="Swimsuit 泳装", id="2252899509862400", headers=headers, minUnitPrice=38,
            maxUnitPrice=55)

    # 市场价
    json_data = {"options":{"searchHierarchyMethod":3,"websiteId":websiteId},"minUnitPriceRate":1.1,"maxUnitPriceRate":1.25}
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers2, json=json_data)
    print("市场价:{}".format(response))
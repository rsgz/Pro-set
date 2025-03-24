import requests
from settings import authorization

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

startx,endx=1139,1208

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
        'minUnitPrice': 55,
        'maxUnitPrice': 99,
    }
    # 整体售价范围
    response = requests.post('https://b03-api.shop6888.com/apis/Action', headers=headers, json=json_data)
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
    # shoujia(websiteId=websiteId, name="Hoodies & Sweatshirts 连帽衫和运动衫", id="2251937252638720", headers=headers,
    #         minUnitPrice=39, maxUnitPrice=45)
    # shoujia(websiteId=websiteId, name="Coats 外套", id="2252074809032704", headers=headers, minUnitPrice=59, maxUnitPrice=75)
    # shoujia(websiteId=websiteId, name="Women's Jackets 夹克", id="2252074725146624", headers=headers, minUnitPrice=55,
    #         maxUnitPrice=99)
    # shoujia(websiteId=websiteId, name="Blazers 西装外套", id="2252074859364352", headers=headers, minUnitPrice=62,
    #         maxUnitPrice=71)
    # shoujia(websiteId=websiteId, name="Cardigans 开衫", id="2252349586276352", headers=headers, minUnitPrice=42,
    #         maxUnitPrice=66)
    # shoujia(websiteId=websiteId, name="Sweater 毛衣", id="2252349770825728", headers=headers, minUnitPrice=38,
    #         maxUnitPrice=55)
    # shoujia(websiteId=websiteId, name="T-Shirts T恤衫", id="2252487025229824", headers=headers, minUnitPrice=27,
    #         maxUnitPrice=37)
    # shoujia(websiteId=websiteId, name="Tank Tops & Camis 背心", id="2252487042007040", headers=headers, minUnitPrice=29,
    #         maxUnitPrice=35)
    # shoujia(websiteId=websiteId, name="Trousers 裤子", id="2252624682287104", headers=headers, minUnitPrice=30,
    #         maxUnitPrice=38)
    # shoujia(websiteId=websiteId, name="Dress 连衣裙", id="2252761936691200", headers=headers, minUnitPrice=55, maxUnitPrice=68)

    # 市场价
    json_data = {"options":{"searchHierarchyMethod":3,"websiteId":websiteId},"minUnitPriceRate":1.1,"maxUnitPriceRate":1.2}
    response = requests.post('https://b03-api.shop6888.com/apis/Action', headers=headers2, json=json_data)
    print("市场价:{}".format(response))
import requests
import json
from settings import authorization

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'frontend.send',
    'authorization': authorization,
    'content-type': 'application/json;charset=UTF-8',
    'frontend': 'Order',
    'frontendactionname': 'order.search',
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
    'pageSize': 20,
    'orderOwner': '803b08',
}

response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
data = json.loads(response.json()["response"])
items =data['response']['items']
record_count = data['response']['recordCount']  // 6

# 打印总订单数
print("-" * 40)
print(f"总订单数: {record_count}")

# 打印每个订单的信息
print("-" * 40)
for item in items:
    print(f"网站ID: {item['websiteId']}")
    print(f"订单号: {item['orderNo']}")
    print(f"物流号: {item['transactionNo']}")
    print(f"顾客IP: {item['clientIp']}")
    print(f"总价: {item['totalPrice']}")
    print(f"实际价格: {item['amount']}")
    print(f"订单币种: {item['originalCurrencyCode']}")
    print(f"付款时间: {item['paymentDate']}")
    print(f"优惠金额: {item['couponFee']}")
    print(f"下单域名: {item['orderHost']}")
    print(f"网站作者: {item['orderOwner']}")
    print(f"付款人: {item['billFirstname']} {item['billLastname']}")
    print(f"手机号码: {item['billPhone']}")
    print(f"城市: {item['billCity']}")
    print(f"街道: {item['billStreet']}")
    print(f"邮编: {item['billPostalcode']}")
    print(f"顾客邮箱: {item['billEmail']}")
    print("-" * 40)
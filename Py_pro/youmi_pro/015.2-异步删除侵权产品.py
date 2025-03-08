import requests
from settings import authorization
# pip install aiohttp
import aiohttp
import asyncio


async def fetch(session, url, headers, json_data):
    async with session.post(url, headers=headers, json=json_data) as response:
        return await response.json()


async def main(qinquan_l, headers):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for qinquan in qinquan_l:
            json_data = {
                'keywords': qinquan,
                'searchHierarchyMethod': 3,
                'limitCount': 20000,
            }
            print("侵权词：↓↓↓↓↓↓↓↓↓↓ {} ↓↓↓↓↓↓↓↓↓↓".format(qinquan))
            task = asyncio.create_task(fetch(session, 'https://b08-api.shop6888.com/apis/Action', headers=headers, json_data=json_data))
            tasks.append(task)

        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
        for result in results:
            print("状态:", result["message"])


# 示例数据
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
"Maje",
"Marq Vision",
"Gestuz"
]
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

# 运行异步任务
asyncio.run(main(qinquan_l, headers))
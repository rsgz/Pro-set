import requests
import random
from settings import authorization,web_site_set,startx,endx,zuojige
from tool_rsgz.time.time import Time
# 身份已经同步

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-website.update',
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


# 底部政策块肯定 21-25之间随机
def sui21():
    return str(random.randint(21, 25))


# startx,endx=277,281

tianbiao_l=[]

web_dict = web_site_set


jishu = 1
for i,(k,v) in enumerate(web_dict.items()):
    web_id = int(k)
    # 650-726
    start = startx
    # if web_id in [228,229,231,232,233,234]:
    if web_id>=start and web_id<=endx:  # 默认的
        sui = sui21()
        leimu = "女夹克连衣裙{}".format(jishu)
        # 🌸 🍁 🍄 🐥 🍓 🍅 🍑 🦞 🧊 🏺 🔥 ☀️ 🎀 🎉  🧡 💛 ❤️💙 💜 🤎 🖤 🤍 👾
        biao_qing = ['🌸', '🍁', '🍄', '🐥', '🍓', '🍅', '🍑', '🦞', '🧊', '🏺', '🔥', '☀️', '🎀', '🎉', '🧡', '💛', '❤️💙',
                 '💜', '🤎','🖤', '🤍', '👾']
        bq=biao_qing[1]  # 0-22
        # http://www.360doc.com/showweb/0/0/1142185192.aspx
        # beizhu = f"{Time().get_current_date_xingqi()} 🧊 模板30"  #
        beizhu = f"2025-03-13 星期四 {bq} 模板22 小李时期  二改重做"  #
        domain = v
        r"""
# 1 - 美国洛杉矶 (199.33.126.154:59880)
# 3 - 美国加利福尼亚 (199.33.127.106:22)
# 4 - 第三台服务器 (199.33.122.90:22)
# 5 - (45.136.118.6:20566)
        """
        json_data = {
            'id': web_id,
            'domain': domain,
            'description':leimu,
            'language': 'en',
            'memo':beizhu,
            'shopServerId': 4,  #
            # 'creationTime': f'{Time().get_current_date_time()}',
            'creationTime': f'2025-03-13 09:01:01',
            'goodsCount': 0,
            'jsonConfig': f'''{{"globalConfig":{{"bannels":[],"pageConfig":{{"pageTitle":"","pageDescription":"","pageKeywords":"","headerCode":"","footerCode":"","defvalCurrencyCode":"","showTranslateTool":false}},"parameters":[]}},"headerMenu":[],"footerMenu":[{{"title":"Contact Us","url":"/article/contactus{sui}.html","menuType":0}},{{"title":"Accessibility","url":"/article/accessibility{sui}.html","menuType":0}},{{"title":"Privacy","url":"/article/privacy{sui}.html","menuType":0}},{{"title":"Supply Chain Transparency","url":"/article/supply{sui}.html","menuType":0}},{{"title":"Terms of Use","url":"/article/termsofuse{sui}.html","menuType":0}},{{"title":"About us","url":"/article/aboutus{sui}.html","menuType":0}}],"navigationMenu":[]}}''',
        }
        jishu = jishu+1
        response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
        print(response, json_data)

        tianbiao_l.append(f'''{json_data['id']}-{json_data['domain']} 旧网站''')

print(*tianbiao_l[::-1],sep="\n")

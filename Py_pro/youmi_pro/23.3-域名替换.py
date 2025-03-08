from tool_rsgz.json.json import Json
import requests
from settings import authorization


# 获取域名信息
def get_info_web(id):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'action-name': 'shop-website.read',
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

    json_data = {
        'id': id,
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    r"""
        ...
    """
    return response

# 设置域名信息  参考
def set_info_web(id,domain):

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

    json_data = {
        'id': id,
        'domain': domain,
        'description': '女夹克连衣裙5',
        'language': 'en',
        'shopServerId': 5,
        'memo': '2025-02-20 星期四 ❤ 模板23',
        'creationTime': '2024-12-23 14:38:18',
        'goodsCount': 3600,
        'generateTempType': 2,
        'jsonConfig': '{"globalConfig":{"bannels":[{"pic":"/uploads/images/2025-02/17a86b1e98d145929dfbabcbc78799c4.webp","title":" ","description":"","url":"/womensclothing-dresses-dress-1","target":""},{"pic":"/uploads/images/2025-02/de266f1381c946ccabf7381b90fbe7e3.webp","title":" ","description":"","url":"/womensclothing-tops-t-shirts-t-1","target":""}],"pageConfig":{"logo":"/uploads/images/2025-03/logo_LLLC_wm3.webp","footerLogo":"/uploads/images/2025-02/13c0beb1fd9e4028bfdc5b071f30d399.webp","ico":"/uploads/images/2025-03/ico_xyner_44l.webp","pageTitle":"Women\'s Graphic Print Hoodie Jackets - Trendy and Comfortable for Outdoor Style.","pageDescription":"Relaxed Fit Sweaters for Women: Soft, Cozy, and Perfect for Fall","pageKeywords":"Women\'s zip-up hoodies, fleece-lined jackets, floral maxi skirts, high-waisted shorts, printed tops, wool cardigans, striped long-sleeve T-shirts, pencil pants, tiered mini dresses, winter trench coats, summer wide-leg pants, off-shoulder tops, faux leather pants, oversized cardigans, graphic hoodies, distressed jeans, wrap dresses, jogger skirts, thermal shirts, lace tops, wide-leg jumpsuits, bodycon mini dresses, quilted vests, pleated trousers, turtleneck dresses, boyfriend shorts, chiffon blouses, paperbag pants, sequin skirts, parka jackets, slip skirts, cargo jumpsuits, halter tops, quilted coats","headerCode":"","footerCode":"","email":"lllc.shop@gmail.com","phone":"+1 (445) 753-4243","defvalCurrencyCode":"USD","sloganText":"Return it in 30 days for a full refund, no questions asked.","showTranslateTool":false,"skin":"xf023","homePageDataBlocks":[{"title":"Exclusive Discounts","description":"","parameters":"","dataCount":8,"sort":0,"dataType":1},{"title":"","description":"","cssClass":"ad-card-2","parameters":"","dataCount":0,"sort":0,"dataType":0,"adItems":[{"pic":"/uploads/images/2025-02/5c4c3d38592e48ff854d67719296e114.webp","title":"","description":"","url":"/womensclothing-dresses-dress-1","target":""},{"pic":"/uploads/images/2025-02/a7dfc82a3fb04e79989bcc3bd4a7cf81.webp","title":"","description":"","url":"/womensclothing-tops-bodysuits-1","target":""}]},{"title":"Time-Limited Free Trial","description":"","cssClass":"ad-card-3","parameters":"","dataCount":0,"sort":0,"dataType":0,"adItems":[{"pic":"/uploads/images/2025-02/8a864534fd1247b5b75259c799f5c0cc.webp","title":"Exclusive Deal!","description":"Illusion Bodysuit Short Comfortable Ribbed Bodysuit","url":"/goods/illusion-bodysuit.html","target":""},{"pic":"/uploads/images/2025-02/e9bf04d54f9c4a02ae4f737fb4fe619b.webp","title":"Shop for Less!","description":"Elation Bodysuit Short Stylish Bodysuit with Pockets","url":"/goods/elation-bodysuit-short.html","target":""},{"pic":"/uploads/images/2025-02/c0f67777382a4963967262bf1f72f5b7.webp","title":"Best Offers Here!","description":"Performance Bodysuit Short Comfortable Shaping Bodysuit","url":"/goods/performance-bodysuit-short.html","target":""}]},{"title":"Unbeatable Prices","description":"","parameters":"","dataCount":8,"sort":0,"dataType":1}]},"parameters":[]},"headerMenu":[{"title":"Hoodies & Sweatshirts ","url":"/womensclothing-hoodiessweatshirts-1","menuType":0},{"title":"Women\'s Jackets ","url":"/womensclothing-outerwear-womensjackets-1","menuType":0},{"title":"Sweater ","url":"/womensclothing-sweaters-sweater-1","menuType":0},{"title":"T-Shirts","url":"/womensclothing-tops-t-shirts-t-1","menuType":0},{"title":"Tank Tops & Camis ","url":"/womensclothing-tops-tanktopscamis-1","menuType":0},{"title":"Bodysuits ","url":"/womensclothing-tops-bodysuits-1","menuType":0},{"title":"Jersey ","url":"/womensclothing-tops-jersey-1","menuType":0},{"title":"Dress","url":"/womensclothing-dresses-dress-1","menuType":0},{"title":"Skirt ","url":"/womensclothing-dresses-skirt-1","menuType":0}],"footerMenu":[{"title":"Contact Us","url":"/article/contactus23.html","menuType":0},{"title":"Accessibility","url":"/article/accessibility23.html","menuType":0},{"title":"Privacy","url":"/article/privacy23.html","menuType":0},{"title":"Supply Chain Transparency","url":"/article/supply23.html","menuType":0},{"title":"Terms of Use","url":"/article/termsofuse23.html","menuType":0},{"title":"About us","url":"/article/aboutus23.html","menuType":0}],"navigationMenu":[]}',
        'flags': 0,
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)

# 设置域名信息  用这个
def set_info_web2(json_data,id,domain):

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

    # json_data = {
    #     'id': id,
    #     'domain': domain,
    #     'description': '女夹克连衣裙5',
    #     'language': 'en',
    #     'shopServerId': 5,
    #     'memo': '2025-02-20 星期四 ❤ 模板23',
    #     'creationTime': '2024-12-23 14:38:18',
    #     'goodsCount': 3600,
    #     'generateTempType': 2,
    #     'jsonConfig': '{"globalConfig":{"bannels":[{"pic":"/uploads/images/2025-02/17a86b1e98d145929dfbabcbc78799c4.webp","title":" ","description":"","url":"/womensclothing-dresses-dress-1","target":""},{"pic":"/uploads/images/2025-02/de266f1381c946ccabf7381b90fbe7e3.webp","title":" ","description":"","url":"/womensclothing-tops-t-shirts-t-1","target":""}],"pageConfig":{"logo":"/uploads/images/2025-03/logo_LLLC_wm3.webp","footerLogo":"/uploads/images/2025-02/13c0beb1fd9e4028bfdc5b071f30d399.webp","ico":"/uploads/images/2025-03/ico_xyner_44l.webp","pageTitle":"Women\'s Graphic Print Hoodie Jackets - Trendy and Comfortable for Outdoor Style.","pageDescription":"Relaxed Fit Sweaters for Women: Soft, Cozy, and Perfect for Fall","pageKeywords":"Women\'s zip-up hoodies, fleece-lined jackets, floral maxi skirts, high-waisted shorts, printed tops, wool cardigans, striped long-sleeve T-shirts, pencil pants, tiered mini dresses, winter trench coats, summer wide-leg pants, off-shoulder tops, faux leather pants, oversized cardigans, graphic hoodies, distressed jeans, wrap dresses, jogger skirts, thermal shirts, lace tops, wide-leg jumpsuits, bodycon mini dresses, quilted vests, pleated trousers, turtleneck dresses, boyfriend shorts, chiffon blouses, paperbag pants, sequin skirts, parka jackets, slip skirts, cargo jumpsuits, halter tops, quilted coats","headerCode":"","footerCode":"","email":"lllc.shop@gmail.com","phone":"+1 (445) 753-4243","defvalCurrencyCode":"USD","sloganText":"Return it in 30 days for a full refund, no questions asked.","showTranslateTool":false,"skin":"xf023","homePageDataBlocks":[{"title":"Exclusive Discounts","description":"","parameters":"","dataCount":8,"sort":0,"dataType":1},{"title":"","description":"","cssClass":"ad-card-2","parameters":"","dataCount":0,"sort":0,"dataType":0,"adItems":[{"pic":"/uploads/images/2025-02/5c4c3d38592e48ff854d67719296e114.webp","title":"","description":"","url":"/womensclothing-dresses-dress-1","target":""},{"pic":"/uploads/images/2025-02/a7dfc82a3fb04e79989bcc3bd4a7cf81.webp","title":"","description":"","url":"/womensclothing-tops-bodysuits-1","target":""}]},{"title":"Time-Limited Free Trial","description":"","cssClass":"ad-card-3","parameters":"","dataCount":0,"sort":0,"dataType":0,"adItems":[{"pic":"/uploads/images/2025-02/8a864534fd1247b5b75259c799f5c0cc.webp","title":"Exclusive Deal!","description":"Illusion Bodysuit Short Comfortable Ribbed Bodysuit","url":"/goods/illusion-bodysuit.html","target":""},{"pic":"/uploads/images/2025-02/e9bf04d54f9c4a02ae4f737fb4fe619b.webp","title":"Shop for Less!","description":"Elation Bodysuit Short Stylish Bodysuit with Pockets","url":"/goods/elation-bodysuit-short.html","target":""},{"pic":"/uploads/images/2025-02/c0f67777382a4963967262bf1f72f5b7.webp","title":"Best Offers Here!","description":"Performance Bodysuit Short Comfortable Shaping Bodysuit","url":"/goods/performance-bodysuit-short.html","target":""}]},{"title":"Unbeatable Prices","description":"","parameters":"","dataCount":8,"sort":0,"dataType":1}]},"parameters":[]},"headerMenu":[{"title":"Hoodies & Sweatshirts ","url":"/womensclothing-hoodiessweatshirts-1","menuType":0},{"title":"Women\'s Jackets ","url":"/womensclothing-outerwear-womensjackets-1","menuType":0},{"title":"Sweater ","url":"/womensclothing-sweaters-sweater-1","menuType":0},{"title":"T-Shirts","url":"/womensclothing-tops-t-shirts-t-1","menuType":0},{"title":"Tank Tops & Camis ","url":"/womensclothing-tops-tanktopscamis-1","menuType":0},{"title":"Bodysuits ","url":"/womensclothing-tops-bodysuits-1","menuType":0},{"title":"Jersey ","url":"/womensclothing-tops-jersey-1","menuType":0},{"title":"Dress","url":"/womensclothing-dresses-dress-1","menuType":0},{"title":"Skirt ","url":"/womensclothing-dresses-skirt-1","menuType":0}],"footerMenu":[{"title":"Contact Us","url":"/article/contactus23.html","menuType":0},{"title":"Accessibility","url":"/article/accessibility23.html","menuType":0},{"title":"Privacy","url":"/article/privacy23.html","menuType":0},{"title":"Supply Chain Transparency","url":"/article/supply23.html","menuType":0},{"title":"Terms of Use","url":"/article/termsofuse23.html","menuType":0},{"title":"About us","url":"/article/aboutus23.html","menuType":0}],"navigationMenu":[]}',
    #     'flags': 0,
    # }
    json_data["id"]=int(id)
    json_data["domain"]=domain

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print(response.json())

if __name__ == '__main__':
    j = Json()

    yuming_dict = {
        "964": "https://iiil.fun",
        "963": "https://iiic.fun",
        "962": "https://iiit.fun",
        "961": "https://hhhy.fun",
        "960": "https://kkku.fun",
        "959": "https://kkkf.fun",
        "958": "https://kkko.fun",
        "957": "https://gggj.fun",
        "956": "https://hhhc.fun",
        "955": "https://iiij.fun",
        "954": "https://hhhv.fun",
        "953": "https://iiib.fun",
        "952": "https://iiio.fun",
        "951": "https://jjjk.fun",
        "950": "https://jjjz.fun",
        "949": "https://kkkb.fun",
        "948": "https://kkki.fun",
        "947": "https://jjjp.fun",
        "946": "https://kkkl.fun",
        "945": "https://jjjs.fun",
        "944": "https://iiie.fun",
        "943": "https://hhhq.fun",
        "942": "https://hhho.fun",
        "941": "https://iiih.fun",
        "940": "https://iiig.fun",
        "939": "https://jjjn.fun",
        "938": "https://iiiw.fun",
        "937": "https://jjju.fun",
        "936": "https://jjjw.fun",
        "935": "https://jjjf.fun",
        "934": "https://hhhj.fun",
        "933": "https://iiiz.fun",
        "932": "https://jjjb.fun",
        "931": "https://iiix.fun",
        "930": "https://jjjh.fun",
        "929": "https://jjjy.fun",
        "928": "https://jjjo.fun",
        "927": "https://iiiv.fun",
        "926": "https://jjjv.fun",
        "925": "https://iiiy.fun",
        "924": "https://kkkm.fun",
        "923": "https://jjjq.fun",
        "922": "https://kkka.fun",
        "921": "https://kkkg.fun",
        "920": "https://kkke.fun",
        "919": "https://iiin.fun",
        "918": "https://jjje.fun",
        "917": "https://jjjg.fun",
        "916": "https://jjjm.fun",
        "914": "https://jjjr.fun",
        "912": "https://llle.shop",
        "911": "https://lllu.shop",
        "910": "https://llla.shop",
        "909": "https://lllm.shop",
        "908": "https://mmmd.shop",
        "907": "https://kkkx.shop",
        "906": "https://llli.shop",
        "904": "https://nnnj.shop",
        "903": "https://llld.shop",
        "902": "https://mmma.shop",
        "901": "https://lllj.shop",
        "900": "https://jjjp.shop",
        "899": "https://jjjc.shop",
        "898": "https://llly.shop",
        "897": "https://lllf.shop",
        "895": "https://lllc.shop",
    }

    for id,yuming in yuming_dict.items():
        # if id==str(895):
        print(id,yuming)

        res = get_info_web(int(id)).json()["response"]
        if "shopServerPath" in res:
            del res["shopServerPath"]
        json_data=res
        # j.print_json(res)
        set_info_web2(json_data, id, domain=yuming)
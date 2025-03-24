import requests
from settings import authorization,startx,endx,zuojige,qujian


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods-classification.read-all',
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

def zhuijia(txt,content):
    # with open("output.txt", "a", encoding="utf-8") as file:
    with open(txt, "a", encoding="utf-8") as file:
        file.write("{}\n".format(content))
        # file.write("第二行\n")
        # file.write("第三行\n")

title_id_set = []  # 819
# for websiteId in range(828,835+1):  # 设置域名范围
# for websiteId in range(980,1018+1):  # 设置域名范围
for websiteId in range(startx,endx+1):  # 设置域名范围
# for websiteId in qujian:  # 设置域名范围
    # websiteId = 523
    json_data = {
        'websiteId': websiteId,
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    data = response.json()["response"]["items"]

    # 获取 数据里面的foregroundText
    def get_leaf_texts(data):
        if isinstance(data, list):
            return [text for item in data for text in get_leaf_texts(item)]
        if isinstance(data, dict):
            if data.get('children') is None:
                return [data.get('foregroundText', '').strip()]
            return get_leaf_texts(data['children'])
        return []

    # 使用方式相同
    data = response.json()["response"]["items"]
    texts = get_leaf_texts(data)
    # print('\n'.join(texts))
    print(websiteId,texts)
    s = websiteId, texts
    zhuijia(txt=r"C:\Users\Administrator\Desktop\0.txt", content=s)
    r"""
    下面这个方法 会获取17个
    web_id,title_id_dict = (523, {"Women's Clothing 女装": '2251799813685248', 
                              'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720', 
                              'Outerwear 外套': '2252074691592192', 
                              "Women's Jackets 夹克": '2252074725146624', 
                              'Sweaters 毛衣': '2252349569499136', 
                              'Sweater 毛衣': '2252349770825728', 
                              'Tops 上装': '2252487008452608', 
                              'T-Shirts T恤衫': '2252487025229824', 
                              'Bottoms 下装': '2252624447406080', 
                              'Leggings 紧身裤': '2252624531292160', 
                              'Legging 紧身裤': '2252624531304448', 
                              'Jeans 牛仔裤': '2252624598401024', 
                              'Dresses 连衣裙': '2252761886359552', 
                              'Skirt 裙子': '2252762054131712', 
                              'Mini Dresses 迷你连衣裙': '2252761987022848', 
                              'Midi Dresses 中长连衣裙': '2252762003800064', 
                              'Maxi Dresses 长连衣裙': '2252762020577280'})
    """

    # 获取 数据里面的title 和id组成字典
    def extract_title_id_pairs(data, result=None):
        r"""
        内层外层都会获取
        :param data:
        :param result:
        :return:
        """
        if result is None:
            result = {}

        # 处理列表
        if isinstance(data, list):
            for item in data:
                extract_title_id_pairs(item, result)

        # 处理字典
        elif isinstance(data, dict):
            # 如果同时存在 title 和 id，添加到结果中
            if 'title' in data and 'id' in data:
                result[data['title']] = data['id']

            # 递归处理 children
            if 'children' in data and data['children']:
                extract_title_id_pairs(data['children'], result)

        return result


    # title_id_pairs = extract_title_id_pairs(data)
    # title_id_set.append((websiteId, title_id_pairs))

    # 这个是获取最内层的 title和id
    def get_leaf_title_id_pairs(data, result=None):
        if result is None:
            result = {}

        # 处理列表
        if isinstance(data, list):
            for item in data:
                get_leaf_title_id_pairs(item, result)

        # 处理字典
        elif isinstance(data, dict):
            # 只处理没有children或children为None的节点
            if ('children' not in data or data['children'] is None) and 'title' in data and 'id' in data:
                result[data['title']] = data['id']
            # 如果有children，继续递归
            elif 'children' in data and data['children']:
                get_leaf_title_id_pairs(data['children'], result)

        return result

    # 假设你的 JSON 数据存储在 json_data 变量中
    title_id_pairs = get_leaf_title_id_pairs(data)
    title_id_set.append((websiteId,title_id_pairs))

    # # 打印结果
    # for title, id in title_id_pairs.items():
    #     print(f"'{title}': '{id}'")

for website in title_id_set:
    print(website)
    zhuijia(txt=r"C:\Users\Administrator\Desktop\0.txt", content=website)

print('\n',*[{k:v} for k,v in title_id_set[1][1].items()],sep=",\n")

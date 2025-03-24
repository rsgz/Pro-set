r"""
这个模块可以获取商品图
54-查询类目 可以生成这个
(523, {"Women's Clothing 女装": '2251799813685248', 'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720', 'Outerwear 外套': '2252074691592192', "Women's Jackets 夹克": '2252074725146624', 'Sweaters 毛衣': '2252349569499136', 'Sweater 毛衣': '2252349770825728', 'Tops 上装': '2252487008452608', 'T-Shirts T恤衫': '2252487025229824', 'Bottoms 下装': '2252624447406080', 'Leggings 紧身裤': '2252624531292160', 'Legging 紧身裤': '2252624531304448', 'Jeans 牛仔裤': '2252624598401024', 'Dresses 连衣裙': '2252761886359552', 'Skirt 裙子': '2252762054131712', 'Mini Dresses 迷你连衣裙': '2252761987022848', 'Midi Dresses 中长连衣裙': '2252762003800064', 'Maxi Dresses 长连衣裙': '2252762020577280'})

顺便还会保存商品数据到了 D:\0-code\rust_pro\rust_pro_git\编程语法\Python3\tool\muban\pic_json.json  里面
{
    "data": [
        {
            "title": "Waves | Embroidered Unisex Hoodie",
            "pic_ulr": "https://b08-api.shop6888.com/uploads/pics/20241109/waves-embroidered-unisex-hoodie.webp",
            "web_url": "/goods/waves-embroidered-unisex-hoodie.html",
            "pic_bendi": "E:\\pic\\shangpin22\\waves-embroidered-unisex-hoodie.png"
        },
"""
import requests
import aiohttp
import asyncio
import os,json
from urllib.parse import urlparse
from settings import authorization,web_n
import subprocess


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'action-name': 'shop-goods.search',
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


async def download_image(session, url, save_dir):
    try:
        # 获取文件名
        filename = os.path.basename(urlparse(url).path)
        save_path = os.path.join(save_dir, filename)
        # 下载图片
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                # 保存图片
                with open(save_path, 'wb') as f:
                    f.write(content)
                print(f"成功下载: {filename}")
            else:
                print(f"下载失败 {url}: HTTP {response.status}")
    except Exception as e:
        print(f"下载失败 {url}: {str(e)}")

async def download_all_images(urls, save_dir='downloaded_images'):
    # 创建保存目录
    os.makedirs(save_dir, exist_ok=True)
    # 创建会话
    async with aiohttp.ClientSession() as session:
        # 创建下载任务
        tasks = [download_image(session, url, save_dir) for url in urls]
        # 执行所有任务
        await asyncio.gather(*tasks)

# 删除文件
def del_file_or_mulu(directory):
    import os
    import shutil

    def delete_all_in_directory(directory):
        """
        删除指定目录中的所有文件和子目录。
        """
        if not os.path.exists(directory):
            print(f"目录 {directory} 不存在")
            return

        # 遍历目录中的所有内容
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    # 如果是文件或符号链接，直接删除
                    os.unlink(item_path)
                    print(f"已删除文件: {item_path}")
                elif os.path.isdir(item_path):
                    # 如果是子目录，递归删除
                    shutil.rmtree(item_path)
                    print(f"已删除目录: {item_path}")
            except Exception as e:
                print(f"删除 {item_path} 时出错: {e}")

    # 指定目录
    # directory = r"E:\pic\shangpin"

    # 调用函数删除所有内容
    delete_all_in_directory(directory)
# 收集所有图片URL
# pic_urls = ["https://b08-api.shop6888.com" + item["pic"] for item in s]

# # 运行异步下载
# asyncio.run(download_all_images(pic_urls))

del_file_or_mulu(directory=r"E:\pic\shangpin")

# 先去  54-查询类目里面获取所有类目 信息
# web_id,title_id_dict =(757, {
web_id,title_id_dict = (997, {'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720', "Women's Jackets 夹克": '2252074725146624', 'Sweater 毛衣': '2252349770825728', 'T-Shirts T恤衫': '2252487025229824', 'Blouses 衬衫': '2252487075573760', 'Pants 长裤': '2252624464183296', 'Dress 连衣裙': '2252761936691200', 'Skirt 裙子': '2252762054131712', 'Party Dress 派对礼服': '2252761919913984', 'Mini Dresses 迷你连衣裙': '2252761987022848'})
# web_id,title_id_dict =(649, { 'Mini Dresses 迷你连衣裙': '2252761987022848',})

# json_data1 = {"websiteId":web_id,"pageIndex":1,"pageSize":50,"searchHierarchyMethod":0,"classificationId":"2252349770825728"}  # 毛衣
# json_data2 = {"websiteId":web_id,"pageIndex":1,"pageSize":50,"searchHierarchyMethod":0,"classificationId":"2252761886359552"}  # Dresses 连衣裙
# json_data3 = {"websiteId":web_id,"pageIndex":1,"pageSize":50,"searchHierarchyMethod":0,"classificationId":"2251937252638720"}  # Hoodies & Sweatshirts 连帽衫和运动衫

# 每个类目图片数量
pic_num = 80
pic_urls = []

# 遍历这个网站的十个类目
pic_json = {"data":[]}
for i,(k,w) in enumerate(title_id_dict.items()):
    print("=================",i,"下载类目商品",k,"=================")
    json_data = {
        'websiteId': web_id,
        'pageIndex': 1,
        'pageSize': pic_num,
        'searchHierarchyMethod': 0,
        'classificationId': w,
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    # print("response-->", response.json())
    s = response.json()["response"]["items"]

    for j in range(pic_num):
        try:
            # https://b08-api.shop6888.com/uploads/pics/20241029/nina-parker-womens-colorblock-long-maxi-dress.webp
            pic_ulr = "https://b08-api.shop6888.com"+s[j]["pic"]  # 图片地址 0 1 2 里面的pic属性

            title = s[j]["title"]  # 商品标题
            web_url = "/goods/"+s[j]["urlKeywords"]+".html"  # 商品地址
            print(title)
            print(pic_ulr)
            print(web_url,"\n")
            pic_urls.append(pic_ulr)

            item_data = {
                "title": title,
                "pic_ulr": pic_ulr,
                "web_url": web_url,
                "pic_bendi":r"E:\pic\shangpin22\{}.png".format(s[j]["urlKeywords"])
            }
            pic_json["data"].append(item_data)
        except:
            print("j:-->第{}张  超了 应该这个分类 少了几张".format(j+1))

file_path = "pic_json.json"
# 将更新后的数据保存回 json 文件
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(pic_json, f, ensure_ascii=False, indent=4)

asyncio.run(download_all_images(pic_urls,r"E:\pic\shangpin"))
    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"websiteId":531,"pageIndex":1,"pageSize":20,"searchHierarchyMethod":0,"classificationId":"2252074725146624"}'
    # response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, data=data)

# 调用另一个 Python 脚本
script_path = r"008-图片尺寸分类.py"
result = subprocess.run(["python", script_path], capture_output=True, text=True, encoding="utf-8")
print("标准输出:", result.stdout)

script_path = r"009-打印子目录图片数量.py"
# result = subprocess.run(["python", script_path], capture_output=True, text=True)
result = subprocess.run(["python", script_path], capture_output=True, text=True, encoding="utf-8")
print("标准输出:", result.stdout)

print("web_id",web_id,"图片下载完毕!")
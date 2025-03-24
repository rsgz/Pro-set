from settings import startx,endx




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
from settings import authorization


import os
from PIL import Image

# 目录分类  根据图片尺寸
def fenlei(image_folder):
    # 定义图片文件夹路径
    # image_folder = r'E:\pic\shangpin'

    # 遍历文件夹中的所有图片
    for filename in os.listdir(image_folder):
        # 获取文件的完整路径
        file_path = os.path.join(image_folder, filename)

        # 确保是文件而不是文件夹
        if os.path.isfile(file_path):
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 获取图片尺寸
                    size = img.size
                    # 创建子目录名称，格式为 "宽度x高度"
                    size_folder = os.path.join(image_folder, f"{size[0]}x{size[1]}")

                    # 如果子目录不存在，则创建
                    if not os.path.exists(size_folder):
                        os.makedirs(size_folder)
                    img.close()  # 显式关闭文件句柄
                    # 移动图片到对应的子目录
                    new_file_path = os.path.join(size_folder, filename)
                    os.rename(file_path, new_file_path)

            except Exception as e:
                print(f"无法处理文件 {filename}: {e}")

    print("图片分类完成！")

# 这个下载几个类目图片
def start(id=762,leimu = {'Mini Dresses 迷你连衣裙': '2252761987022848'},save = r"E:\pic\leimu\leimu1"):
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

    # 先去  54-查询类目里面获取所有类目 信息
    # web_id,title_id_dict =(762, {
    #                              # 'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720',
    #                              # "Women's Jackets 夹克": '2252074725146624',
    #                              # 'Sweater 毛衣': '2252349770825728',
    #                              # 'T-Shirts T恤衫': '2252487025229824',
    #                              # 'Blouses 衬衫': '2252487075573760',
    #                              # 'Pants 长裤': '2252624464183296',
    #                              # 'Jeans 牛仔裤': '2252624598401024',
    #                              # 'Skirt 裙子': '2252762054131712',
    #                              # 'Mini Dresses 迷你连衣裙': '2252761987022848',
    #                              # 'Maxi Dresses 长连衣裙': '2252762020577280'
    #                              })
    web_id, title_id_dict = (id, leimu)
    # 每个类目图片数量
    # 每个类目图片数量
    pic_num = 400
    pic_urls = []

    # 遍历这个网站的十个类目
    pic_json = {"data": []}
    for i, (k, w) in enumerate(title_id_dict.items()):
        print("=================", i, "下载类目商品", k, "=================")
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
                pic_ulr = "https://b08-api.shop6888.com" + s[j]["pic"]  # 图片地址 0 1 2 里面的pic属性

                title = s[j]["title"]  # 商品标题
                web_url = "/goods/" + s[j]["urlKeywords"] + ".html"  # 商品地址
                print(title)
                print(pic_ulr)
                print(web_url, "\n")
                pic_urls.append(pic_ulr)

                item_data = {
                    "title": title,
                    "pic_ulr": pic_ulr,
                    "web_url": web_url,
                    "pic_bendi": r"E:\pic\shangpin22\{}.png".format(s[j]["urlKeywords"])
                }
                pic_json["data"].append(item_data)
            except:
                print("j:-->第{}张  超了 应该这个分类 少了几张".format(j + 1))
    # asyncio.run(download_all_images(pic_urls,r"E:\pic\shangpin2"))
    asyncio.run(download_all_images(pic_urls,save))

# 这个判断 共同尺寸目录
def gongtong_chicun_mulu(parent_dirs):
    import os

    # 定义多个父目录
    # parent_dirs = [
    #     r"E:\pic\leimu\leimu1",
    #     r"E:\pic\leimu\leimu2",
    #     r"E:\pic\leimu\leimu3",
    #     r"E:\pic\leimu\leimu4"
    # ]

    # 获取每个父目录中的所有子目录
    subdirs_list = []
    for parent_dir in parent_dirs:
        subdirs = {d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))}
        subdirs_list.append(subdirs)

    # 找出所有父目录中共同的子目录
    common_subdirs = set.intersection(*subdirs_list)

    for d in parent_dirs:
        print(d)

    # 输出结果
    if common_subdirs:
        print("所有目录中共同的子目录：")
        for subdir in common_subdirs:
            # print(subdir)
            s = ""
            for d in parent_dirs:
                tong = os.path.join(d,subdir)
                s=s+"/"+str(len(os.listdir(tong)))
            print(subdir,'--->',s)
    else:
        print("没有共同的子目录。")

# 清空目录列表图片
def del_file(leimu_l):
    import os
    import shutil
    from concurrent.futures import ThreadPoolExecutor

    # 定义目录列表
    # leimu_l = [
    #     r"E:\pic\leimu\leimu1",
    #     r"E:\pic\leimu\liemu2",
    #     r"E:\pic\leimu\liemu3",
    #     r"E:\pic\leimu\liemu4",
    #     r"E:\pic\leimu\liemu5",
    #     r"E:\pic\leimu\liemu6"
    # ]

    # 清空目录中的所有文件
    def clear_directory(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                # 如果是文件，直接删除
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print(f"已删除文件: {file_path}")
                # 如果是目录，递归删除
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"已删除目录: {file_path}")
            except Exception as e:
                print(f"删除失败 {file_path}: {e}")

    # 使用多线程清空所有目录
    with ThreadPoolExecutor() as executor:
        for directory in leimu_l:
            if os.path.exists(directory):
                print(f"正在清空目录: {directory}")
                executor.submit(clear_directory, directory)
            else:
                print(f"目录不存在: {directory}")

# id = 820
kaishi,jieshu = startx,endx
leimu = [
# {'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720'},
# {"Women's Jackets 夹克": '2252074725146624'},
# {'Pullovers 套头衫': '2252349603053568'},
# {'Sweater 毛衣': '2252349770825728'},
# {'T-Shirts T恤衫': '2252487025229824'},
# {'Crop Top  短款上衣': '2252487109115904'},
# {'Trousers 裤子': '2252624682287104'},
# {'Pants 长裤': '2252624464183296'},
# {'Dress 连衣裙': '2252761936691200'},
# {'Party Dress 派对礼服': '2252761919913984'},
# {'Romper 连身裤': '2252624833282048'},
# {'Bomber Jacket 飞行员夹克': '2252075228463104'},
# {'Polo Shirts 马球衫': '2252487327219712'},
#   {'Sweatpants 运动裤': '2252624564846592'}
{'Coats 外套': '2252074809032704'},
{'Cardigans 开衫': '2252349586276352'},
{'Trousers 裤子': '2252624682287104'},
]

leimu_l = [
r"E:\pic\leimu\Coats",
r"E:\pic\leimu\Cardigans",
r"E:\pic\leimu\Trousers",
# r"E:\pic\leimu\Sweatpants",
# r"E:\pic\leimu\Hoodies",
# r"E:\pic\leimu\Jackets",
# r"E:\pic\leimu\Pullovers",
# r"E:\pic\leimu\Sweater",
# r"E:\pic\leimu\T-Shirts",
# r"E:\pic\leimu\Crop Top",
# r"E:\pic\leimu\Trousers",
# r"E:\pic\leimu\Pants",
# r"E:\pic\leimu\Dress",
# r"E:\pic\leimu\Party Dress",
# r"E:\pic\leimu\Romper",
# r"E:\pic\leimu\Bomber Jacket",
# r"E:\pic\leimu\Polo Shirts",
           ]
shanchutupian=0  # 删除图片
xiaziafenlei=1  # 下载分类
chicunfenlei=1  # 尺寸分类
tongchicun=1  # 统计尺寸

if shanchutupian==1:
    del_file(leimu_l)

if xiaziafenlei==1:
    for id in range(kaishi,jieshu):
        print(50*"=========={}==========\n".format(id))
        for i in range(len(leimu_l)):
            start(id=id,leimu =leimu[i] ,save = leimu_l[i])
    # start(id=id,leimu =leimu[1] ,save = leimu_l[1])
    # start(id=id,leimu =leimu[2] ,save = leimu_l[2])
    # start(id=id,leimu =leimu[3] ,save = leimu_l[3])
    # start(id=id,leimu =leimu[4] ,save = leimu_l[4])
if chicunfenlei==1:
    for i,k in enumerate(leimu_l):
        fenlei(image_folder=k)
    # fenlei(image_folder=leimu_l[1])
    # fenlei(image_folder=leimu_l[2])
    # fenlei(image_folder=leimu_l[3])
    # fenlei(image_folder=leimu_l[4])
if tongchicun==1:
    gongtong_chicun_mulu(parent_dirs=leimu_l)
import json,requests,time,os,base64
from youmi_pro.settings import authorization

# 假设你已经有了下载图片和上传图片的函数
def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # 检查请求是否成功

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    except requests.exceptions.RequestException as e:
        print(f"下载图片失败: {e}")
        return False
    except IOError as e:
        print(f"保存图片失败: {e}")
        return False

# 转换成base64
def convert_image_to_base64(image_path):
    # 以二进制模式读取 PNG 图像
    with open(image_path, "rb") as image_file:
        # 将图片编码为 base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    # 构建 JSON 对象
    result = {
        "filename": image_path.split(os.sep)[-1],  # 获取文件名（不包含路径）
        "base64Data": f"data:image/png;base64,{encoded_string}"  # 格式化 base64 字符串
    }
    # return json.dumps(result, indent=4)  # 返回格式化后的 JSON 数据
    return result

# 发送图片
def send_one_pic(image_path):
    r"""
    image_path = r"D:\Backup\Downloads\001.png"
    pic_web_path = send_one_pic(image_path)
    """
    # 上传图片 upload-image.base64
    headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'action-name': 'upload-image.base64',
            'authorization': authorization,
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://b08-admin.shop6888.com',
            'priority': 'u=1, i',
            'referer': 'https://b08-admin.shop6888.com/',
            'resourcestoreconfigname': 'RandomNameImagesLocalResourceStoreConfig',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

    # 头部 菜单数据

    json_result = convert_image_to_base64(image_path)
    json_data = json_result
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print(response)
    # print(response.json()["response"]["url"])  # /uploads/images/2024-12/f0c914cf980d4757abe665df369a301f.webp
    pic_web_path = response.json()["response"]["url"]
    print("上传图片:{}--->{}".format(response,pic_web_path))
    return pic_web_path

# 随机元素 返回列表
def suiji_yuansu(my_list,n):
    import random
    if n > len(my_list):
        raise ValueError("选择的元素数量不能大于列表的长度")
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 从列表中随机选择5个不重复的元素
    random_elements = random.sample(my_list, n)
    # print(random_elements)
    return random_elements

# 上传一张
def one(image_path):
    # pic_web_path = send_one_pic(image_path=r"D:\Backup\Downloads\模板16\1_ad-grid-2-1-2\1.5.png")
    pic_web_path = send_one_pic(image_path)
    full_path = "{}--{}{}".format(os.path.basename(image_path),"https://b08-api.shop6888.com",pic_web_path)
    print(pic_web_path,full_path)
    return pic_web_path

# 上传一张并且删除本地图片
def one_and_del(image_path):
    pic_web_path = send_one_pic(image_path)
    full_path = "{}--{}{}".format(os.path.basename(image_path), "https://b08-api.shop6888.com", pic_web_path)
    print(pic_web_path, full_path)
    os.remove(image_path)
    return pic_web_path

# 随机 上传一张并且删除本地图片  这个好用
def one_and_del_suiji(pic_dir):
    r"""
    pic_web_path = one_and_del_suiji(pic_dir=r"E:\pic\600-700\Midi Dresses")
    """
    pic_set = get_all_file(path=pic_dir)
    image_path = suiji_yuansu(my_list=pic_set, n=1)[0]
    pic_web_path = one_and_del(image_path)
    return pic_web_path

muban_json = {
    "websiteId": 0,
    "globalConfig": {
        "bannels":[],
        "pageConfig": {},
        "parameters": []
    }
}

# 获取网站数据
def get_web_json(websiteId,authorization):
    import requests

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'action-name': 'shop-website.read.global-config',
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
        'websiteId': websiteId,
        'id': 'GlobalConfig',
    }

    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)

    # print(response.json())
    return response.json()

# 更新网站数据
def update_web(json_data):
    # 保存网站全局配置
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'action-name': 'shop-website.save.global-config',
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
    response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=headers, json=json_data)
    print("{}-->上传:{}".format(websiteId, response))

# 获取本地所有文件
def get_all_file(path):
    import os
    j = os.path.join
    f = os.path.dirname(os.path.basename(__file__))
    f_l=[]
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # print(os.path.join(dirpath, filename))  # 这是没有排序的
            f=os.path.join(dirpath, filename)
            f_l.append(f)
    return f_l

# 字符串转列表
def str_to_list(u_str):
    r"""
    pic_l2 = r'''
"E:\pic\shangpin\800x800\mylie-deep-slit-maxi-dress.webp"
"E:\pic\shangpin\800x800\wrap-up-coverup-skirt-royal-blue.webp"
    '''
    """
    return [line.strip('"') for line in u_str.splitlines() if line.strip()]


# start = 765
# start = 788
start = 831
end = 955
for websiteId in range(start,end+1):
    # if websiteId==764:
    #     continue
    print("websiteId--->",websiteId)
    res = get_web_json(websiteId=websiteId,authorization=authorization)
    bannels = res['response']["bannels"]
    pageConfig = res['response']["pageConfig"]
    homePageDataBlocks=pageConfig["homePageDataBlocks"]
    # print(json.dumps(pageConfig, indent=4, ensure_ascii=False))
    # print(json.dumps(homePageDataBlocks, indent=4, ensure_ascii=False))

    # 打造成类的形式 可以链式调用 self返回对象本身
    class pageConfig_obj:
        def __init__(self, pageConfig):
            self.pageConfig = pageConfig  # 初始化时传入配置数据

        def mokuai(self, n):
            """获取第 n 个模块"""
            self.current_mokuai = self.pageConfig["homePageDataBlocks"][n - 1]  # 模块 n=1 表示 [0]
            return self  # 返回 self 以实现链式调用

        def zhang(self, n):
            """获取第 n 个张"""
            if hasattr(self, 'current_mokuai'):  # 检查是否已经调用了 mokuai 方法
                return self.current_mokuai["adItems"][n - 1]  # 张 n=1 表示 [0]
            else:
                raise ValueError("请先调用 mokuai 方法选择模块")

    # 使用示例
    pageConfig_obj = pageConfig_obj(pageConfig)  # 这个对象包含了 所有的 模块
    # p = pageConfig_obj.mokuai(1).zhang(2)  # 获取第1个模块的第2个张

    # 可以根据规律总结一下  更新商品图  不用删除原图
    def update_zhang_info(module_num, zhang_num, pic_path):
        r"""
        更新指定模块和张的信息
        # 更新模块2的  第一张和第二张
        for i, pic_path in enumerate(str_to_list(pic_l2), start=1):
            update_zhang_info(module_num=2, zhang_num=i, pic_path=pic_path)
        """
        zhang = pageConfig_obj.mokuai(module_num).zhang(zhang_num)
        zhang["pic"] = one(pic_path)
        # zhang["pic"] = one_and_del_suiji(pic_path)
        zhang["description"], zhang["url"] = find_info_by_path(pic_path)

    # 更新大类图 信息  会删除原图
    def update_dalei(module_num, zhang_num, pic_path,dalei_url):
        r"""
        更新指定模块和张的信息
        # 更新模块2的  第一张和第二张
        for i, pic_path in enumerate(str_to_list(pic_l2), start=1):
            update_dalei(module_num=1, zhang_num=i, pic_path = pic_path,dalei_url=dalei_l[i-1])
        """
        zhang = pageConfig_obj.mokuai(module_num).zhang(zhang_num)
        # zhang["pic"] = one(pic_path)
        zhang["pic"] = one_and_del(pic_path)
        # zhang["description"], zhang["url"] = find_info_by_path(pic_path)
        zhang["url"] = dalei_url

    # 更新你的ad card 1
    def update_ad(module_num, zhang_num, pic_path):
        r"""
        更新指定模块和张的信息
        # 更新模块2的  第一张和第二张
        for i, pic_path in enumerate(str_to_list(pic_l2), start=1):
            update_dalei(module_num=1, zhang_num=i, pic_path = pic_path,dalei_url=dalei_l[i-1])
        """
        zhang = pageConfig_obj.mokuai(module_num).zhang(zhang_num)
        zhang["pic"] = one(pic_path)
        # zhang["pic"] = one_and_del(pic_path)

    ############################################## 修改商品 ##############################################
    baocun_pic = r"C:\Users\Administrator\Desktop\数据\pic"
    for mokuai in homePageDataBlocks:
        if mokuai["dataType"] == 0:
            if not mokuai["adItems"] is None:
                for tu in mokuai["adItems"]:
                    if not tu["pic"].startswith("/uploads/images/"):
                        image_url = tu["pic"]
                        print("xxxxxxxxxxxxxxx",image_url)
                        image_name = image_url.split("/")[-1]  # 获取图片名称
                        # image_path = os.path.join(os.getcwd(), image_name)  # 在当前目录保存图片
                        image_path = os.path.join(baocun_pic, image_name)  # 在当前目录保存图片

                        if download_image(image_url, image_path):
                            pic_url=one_and_del(image_path)
                            tu["pic"] = pic_url

                else:
                    print("图片路径以/uploads/images/开头，无需下载和上传。")

    print("新的 homePageDataBlocks")
    print(json.dumps(homePageDataBlocks, indent=4, ensure_ascii=False))
    pageConfig["homePageDataBlocks"]=homePageDataBlocks

    time.sleep(2)
    muban_json["globalConfig"]["bannels"]=bannels
    muban_json["globalConfig"]["pageConfig"]=pageConfig
    muban_json["websiteId"] = websiteId
    muban_json_str = json.dumps(muban_json, indent=4, ensure_ascii=False)

    # print(bannels)
    print(muban_json_str)
    update_web(json_data=muban_json)

print(websiteId,"处理完毕")
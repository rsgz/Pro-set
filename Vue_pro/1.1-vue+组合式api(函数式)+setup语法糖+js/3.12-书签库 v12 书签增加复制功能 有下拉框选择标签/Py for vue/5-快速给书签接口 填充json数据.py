r"""
pip install requests
"""
import requests,random
import json

# json文件数据
def load_image_path_mapping(file_path="web_path.json"):
    r"""
    file_path="web_path.json"
    data = load_image_path_mapping(file_path)
    pic_web_path = data.get(image_path)
    """
    # 尝试读取 JSON 文件并返回映射字典
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或者文件格式有误，返回一个空字典
        print("文件未找到或格式错误。")
        return {}



# 定义URL和数据
url = "http://127.0.0.1:8081/api/bookmarks"

def suiji_one_hang(txt):
    s= random.choice([line.strip().split() for line in open(txt, 'r', encoding='utf-8') if line.strip()])[0]
    # print(s)
    return s
# data = {
#     "id": "1",
#     "name": "迪迦",
#     "purpose": "娱乐",
#     "source": "小红书",
#     "tag": "AI,GPT",
#     "url": "https://tongyi.xxx.com/"
#  }

data = {
    "id": "1",
    "name": suiji_one_hang(txt="data/url_name.txt"),
    "purpose": suiji_one_hang(txt="data/yong_tu.txt"),
    "source": suiji_one_hang(txt="data/ping_tai.txt"),
    "tag": suiji_one_hang(txt="data/biao_qian.txt"),
    "url": suiji_one_hang(txt="data/url.txt")
 }

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

shuqian_obj = load_image_path_mapping(file_path="shuqian.json")
# print(shuqian_obj)
shuqian_obj_l = shuqian_obj["RECORDS"]
for i in range(0,len(shuqian_obj_l)):
    data = {
        "id": "1",
        "name": shuqian_obj_l[i]["name"],
        "purpose": shuqian_obj_l[i]["purpose"],
        "source": shuqian_obj_l[i]["source"],
        "tag": shuqian_obj_l[i]["tag"],
        "url": shuqian_obj_l[i]["url"],
    }
    print(data)
    response = requests.post(url, json=data, headers=headers)
    # # 打印响应内容
    print("Status Code:", response.status_code)
    # print("Response Body:", response.text)
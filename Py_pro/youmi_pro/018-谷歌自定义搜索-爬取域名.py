import requests,time
from urllib.parse import urlparse

# 替换为你的 API 密钥和搜索引擎 ID
API_KEY = r'AIzaSyCAjQP6jh4DcXnI7FH9EV815G04kf7GteQ'
SEARCH_ENGINE_ID = r'd73fefa4a65494122'



# 每页的结果数（最大为 10）
results_per_page = 10

# 要提取的页数
# start = 1  # 开始页数
# num_pages = 12  # 结束页数

# start,num_pages=1,3
# start,num_pages=4,6
# start,num_pages=7,10
start,num_pages=1,10


# 存储所有域名
domains = set()

# 保存域名
def write_history(file_txt,info):
    try:
        with open(file_txt, 'a+', encoding="utf-8") as f:
            f.write(str(info))
            f.write("\n")
    except OSError as err:
        print(file_txt, "写入信息的时候出现了问题")
        print(err)
    else:
        print(file_txt, "已经写入到本地!!!")


# 获取域名列表
# def get_yuming(kw=r"Cozy Knit Cardigan"):
def get_yuming(kw):
    # 搜索关键词
    # kw = r"Cozy Knit Cardigan"
    query = f"{kw} site:myshopify.com"
    print(f"关键词：========================{kw}========================\n"*10)
    for page in range(start-1,num_pages):
        # 计算起始索引
        start_index = page * results_per_page + 1

        # API 请求 URL
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}&start={start_index}"
        time.sleep(6)
        # 发送请求
        response = requests.get(url)
        data = response.json()
        print(f"条数：{start_index}  数据：{data}")
        error_code = data.get('error', {}).get('code')
        if error_code == 429:
            print("429 接口频率限制!!!")
            break

        # 提取域名
        if 'items' in data:
            for item in data['items']:
                link = item['link']  # https://immaculatevegan.myshopify.com/products/green-glitter-heels-wedding-shoes-70133
                # 提取域名
                # domain = link.split('/')[2]
                parsed_url = urlparse(link)
                domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
                domains.add(domain)

    # 打印所有域名
    for domain in domains:
        print(domain)

    result = '\n'.join(map(str, domains))

    write_history(file_txt=r"C:\Users\Administrator\Desktop\yuming.txt",info=result)

# 读取关键字列表
def read_txt_to_list(file_path=r"C:\Users\Administrator\Desktop\数据\0-关键词\关键词2 1032.txt"):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_l = [d.strip() for d in file.readlines()]
        return data_l


start_hang_kw = 17
kw_list = read_txt_to_list(file_path=r"C:\Users\Administrator\Desktop\数据\0-关键词\关键词2 1032.txt")
for kw in kw_list[start_hang_kw:]:
    get_yuming(kw=kw)
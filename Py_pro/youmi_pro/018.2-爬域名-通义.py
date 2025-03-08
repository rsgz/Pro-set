import requests,time
from urllib.parse import urlparse

domains = set()

def google_search(query, api_key, cse_id, start=1):
    url = "https://customsearch.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'num': 10,  # 每页最多返回10条结果
        'start': start
    }
    response = requests.get(url, params=params)
    return response.json()

def get_all_pages_results(query, api_key, cse_id):
    start = 1
    for _ in range(10):  # 获取前10页的结果
        results = google_search(f"{query} site:myshopify.com", api_key, cse_id, start)
        error_code = results.get('error', {}).get('code')
        if error_code == 429:
            print("429 接口频率限制!!!")
            break

        if 'items' in results:
            for item in results['items']:
                link = item['link']  # https://immaculatevegan.myshopify.com/products/green-glitter-heels-wedding-shoes-70133
                # 提取域名
                # domain = link.split('/')[2]
                parsed_url = urlparse(link)
                domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
                print(domain)
                domains.add(domain)
        else:
            break  # 如果没有更多结果，则退出循环
        start += 10  # 更新开始索引以获取下一页的结果
        if 'nextPage' not in results['queries']:
            break  # 如果没有更多页面，则退出循环
        time.sleep(2)

    result = '\n'.join(map(str, domains))
    print(result)
    write_history(file_txt=r"C:\Users\Administrator\Desktop\yuming.txt", info=result)

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

# 读取关键字列表
def read_txt_to_list(file_path=r"C:\Users\Administrator\Desktop\数据\0-关键词\关键词2 1032.txt"):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_l = [d.strip() for d in file.readlines()]
        return data_l



if __name__ == '__main__':
    API_KEY = r'AIzaSyCAjQP6jh4DcXnI7FH9EV815G04kf7GteQ'
    SEARCH_ENGINE_ID = r'd73fefa4a65494122'

    api_key = API_KEY
    cse_id = SEARCH_ENGINE_ID

    start_hang_kw = 99
    kw_list = read_txt_to_list(file_path=r"C:\Users\Administrator\Desktop\数据\0-关键词\关键词2 1032.txt")
    for kw in kw_list[start_hang_kw:]:
        print(f"开始第几行 {start_hang_kw}")
        get_all_pages_results(query=kw, api_key=api_key, cse_id=cse_id)
        time.sleep(200)
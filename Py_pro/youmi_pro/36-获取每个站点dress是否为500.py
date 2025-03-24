import requests
from bs4 import BeautifulSoup
from settings import web_site_set

# 网站列表
# domains = [
#     "https://example1.com",
#     "https://example2.com",
#     # 添加更多域名...
# ]

# 要访问的路径
path = "/womensclothing-dresses-dress-1/"

# 保存结果
results = {}

# 访问每个网站并提取信息
for i, domain in web_site_set.items():
# for domain in domains:
    if int(i)<974:
        url = domain + path  # 构造完整的 URL
        print(fr"{i}-{url}",end='')
        try:
            # 发起 GET 请求
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # 检查请求是否成功

            # 解析 HTML 内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 找到 class="total-info" 的 <a> 标签
            total_info = soup.find_all("a", class_="total-info")

            # 提取字符串内容
            info_strings = [a.text.strip() for a in total_info]
            results[domain] = info_strings
            print(f"--->{info_strings}")

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {url}, 错误: {e}")
            results[domain] = f"请求失败: {e}"

# 输出结果
print("\n汇总结果:")
for domain, info in results.items():
    print(f"{domain}: {info}")

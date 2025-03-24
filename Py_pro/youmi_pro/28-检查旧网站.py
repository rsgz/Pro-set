r"""
第一次需要细看

第二次检查
大部分第一次检查后 就不用二次检查 细看了

只需要 这个能下载 就说明 网站能访问
https://mmmu.shop/images/logo.webp
"""
import os
import requests
from settings import web_site_set


save_directory = r"E:\logo_web"
os.makedirs(save_directory, exist_ok=True)

for i, web_site in web_site_set.items():
    try:
        logo_url = f"{web_site}/images/logo.webp"
        response = requests.get(logo_url, timeout=30)  # Timeout to avoid hanging requests
        response.raise_for_status()  # Raise an error for HTTP issues

        file_path = os.path.join(save_directory, f"{i}_mmmu.shop.webp")
        with open(file_path, "wb") as file:
            file.write(response.content)

        # print(f"Downloaded: {i} - {logo_url}")
    except requests.exceptions.RequestException as e:
        # print(f"Failed to download: {i} - {web_site} | Error: {e}")
        print(f"{i}---{web_site}")
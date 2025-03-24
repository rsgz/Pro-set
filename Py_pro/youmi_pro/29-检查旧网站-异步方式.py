import os
import asyncio
import aiohttp
from aiohttp import ClientSession
from settings import web_site_set

save_directory = r"E:\logo_web"
os.makedirs(save_directory, exist_ok=True)

async def download_logo(i, web_site, session):
    try:
        logo_url = f"{web_site}/images/logo.webp"
        async with session.get(logo_url, timeout=30) as response:
            if response.status == 200:  # Ensure HTTP 200 response
                file_path = os.path.join(save_directory, f"{i}_mmmu.shop.webp")
                with open(file_path, "wb") as file:
                    file.write(await response.read())
                # print(f"Downloaded: {i} - {logo_url}")
            else:
                # print(f"Failed: {i} - {logo_url} | HTTP Status: {response.status}")
                print(f'"{i}":"{web_site}", # 网络')
    except Exception as e:
        # print(f"Error: {i} - {web_site} | {e}")
        print(f'"{i}":"{web_site}"')

async def main():
    start,end=216,973
    async with ClientSession() as session:
        tasks = []
        for i, web_site in web_site_set.items():
            if int(i)>=start and int(i)<=end:
                tasks.append(download_logo(i, web_site, session))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

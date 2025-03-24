import asyncio,os
from pyppeteer import launch
from tool_rsgz.txt.txt import Txt
r"""
pip install pyppeteer
"""
from settings import web_site_set

t=Txt()
async def capture_screenshot(url, output_path):
    browser = await launch(headless=True,executablePath=r"E:\Win_x64_1182793_chrome-win\chrome-win\chrome.exe")  # 启动无头浏览器
    page = await browser.newPage()
    await page.goto(url)  # 打开网址
    await page.setViewport({'width': 1920, 'height': 1080})  # 设置视口大小
    await page.screenshot({'path': output_path, 'fullPage': True})  # 截取全屏
    await browser.close()

async def main():
    # urls = ["https://example.com", "https://python.org"]  # 网址列表
    save_directory = r"E:\jietu"
    for i, url in web_site_set.items():
        if int(i)<403:
    # for i, url in enumerate(urls):
            print(f"--->{i},{url}")
            try:
                output_path = f"{save_directory}\\{i}.png"
                await capture_screenshot(url, output_path)
                # print(f"已保存截图: {output_path}")
            except:
                info = f"{i}-{url}"
                t.zhuijia_str_to_txt(str_content=info,txt_path=r"E:\访问失败网站.txt")
                print("xxxxxx",info)
asyncio.get_event_loop().run_until_complete(main())
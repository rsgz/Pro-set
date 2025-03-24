import asyncio
from pyppeteer import launch
from tool_rsgz.txt.txt import Txt
from settings import web_site_set

t = Txt()


async def capture_screenshot(url, output_path, browser):
    try:
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'load'})  # 确保页面加载完成
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.screenshot({'path': output_path, 'fullPage': True})
        await page.close()
        print(f"已保存截图: {output_path}")
    except Exception as e:
        print(f"截图失败: {url}, 错误: {e}")
        info = f"{url}"
        t.zhuijia_str_to_txt(str_content=info, txt_path=r"E:\访问失败网站.txt")


async def process_urls_concurrently(urls, save_directory):
    # 启动一个共享的无头浏览器
    browser = await launch(headless=True, executablePath=r"E:\Win_x64_1182793_chrome-win\chrome-win\chrome.exe")
    tasks = []

    # 创建任务队列，每个任务处理一个网址
    for i, (id, url) in enumerate(urls.items()):
        if int(id) < 969:
            output_path = f"{save_directory}\\{id}.png"
            task = capture_screenshot(url, output_path, browser)
            tasks.append(task)

    # 并发运行所有任务
    await asyncio.gather(*tasks)
    await browser.close()


async def main():
    save_directory = r"E:\jietu"
    await process_urls_concurrently(web_site_set, save_directory)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # 为 Windows 修复事件循环问题
asyncio.get_event_loop().run_until_complete(main())

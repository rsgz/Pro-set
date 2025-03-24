import pyautogui,keyboard
import time
from tool_rsgz.find_pic.find_pic import find_pic_click_center_keep,find_pic_move_center,gdiScreenCapture


def start():
    time.sleep(0.5)
    pyautogui.click(x=514, y=1056, duration=0.1)  # 点击
    time.sleep(0.5)
    pyautogui.click(x=600, y=600, duration=0.1)  # 点击
    time.sleep(0.5)
    pyautogui.rightClick()
    # pyautogui.click(x=701, y=663, duration=0.1)  # 点击
    # xy = find_pic_move_center(small=r".\weketu\006.jpg", big=gdiScreenCapture(), xiangsidu=0.90)
    find_pic_click_center_keep(small=r".\weketu\006.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
    find_pic_click_center_keep(small=r".\weketu\008.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)
    find_pic_click_center_keep(small=r".\weketu\007.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
    find_pic_click_center_keep(small=r".\weketu\009.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
    find_pic_click_center_keep(small=r".\weketu\010.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
    time.sleep(0.3)
    pyautogui.click(x=119, y=1056, duration=0.1)  # 点击

    # pyautogui.hotkey('alt', 'tab')

# # 创建键盘事件监听器
# def on_press(key):
#     global ctrl_pressed
#
#     try:
#         # 检测是否按下了 Ctrl 键
#         if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
#             ctrl_pressed = True
#
#         # 如果 Ctrl 已按下，并且按下了 'c' 键
#         if ctrl_pressed and key.char == 'c':
#             start()
#
#     except AttributeError:
#         # 忽略没有 char 属性的特殊键（如 Shift、Alt 等）
#         pass
#
# def on_release(key):
#     global ctrl_pressed
#
#     # 当释放 Ctrl 键时，重置标志
#     if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
#         ctrl_pressed = False
#
#
# # 启动键盘监听
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     print("开始监听键盘事件，按下 Ctrl+C 执行程序...")
#     listener.join()


start()
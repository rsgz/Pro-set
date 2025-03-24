import pyautogui,os
import time
from tool_rsgz.find_pic.find_pic import find_pic_click_center_keep,find_pic_move_center,gdiScreenCapture

pyautogui.moveTo(500, 500)
time.sleep(1)
pyautogui.rightClick()
find_pic_click_center_keep(small=r".\weketu\001.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
find_pic_click_center_keep(small=r".\weketu\002.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(1)
pyautogui.moveTo(500, 500)
pyautogui.rightClick()
find_pic_click_center_keep(small=r".\weketu\003.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
find_pic_click_center_keep(small=r".\weketu\002.jpg", jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(3)
xy=find_pic_move_center(small=r".\weketu\004.jpg", big=gdiScreenCapture(), xiangsidu=0.90)
x=int(xy[0])
os.chdir(r"C:\Users\Administrator\Desktop")
os.rename("x.exe",f"{x}.exe")
os.system(f"{x}.exe")
time.sleep(2)
os.rename(f"{x}.exe","x.exe")




if __name__ == '__main__':
    pass
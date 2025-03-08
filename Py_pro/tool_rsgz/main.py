from tool_rsgz.time.time import Time
from tool_rsgz.python.python_info import Python_Info
from tool_rsgz.mokuai.mokuai import Mokuai_Fenxi
from tool_rsgz.mulu.mulu import Mulu
from tool_rsgz.txt.txt import Txt
from tool_rsgz.cmd.cmd import Cmd


# m=Mokuai_Fenxi()
# m.print_fangfa_hanshu(Python_Info)

t=Txt()

txt = r"C:\Users\Administrator\Desktop\task - 副本.json"
l= t.get_txt_to_list(txt)

l2=l[0].split(",")
t.list_to_txt_append(l2,r"C:\Users\Administrator\Desktop\0.txt")
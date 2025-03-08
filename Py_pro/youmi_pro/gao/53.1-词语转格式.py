from tool_rsgz.txt.txt import Txt
from tool_rsgz.file.file import File

import os

t = Txt()
f = File()
mu = r"C:\Users\Administrator\Desktop\长尾词2"
file_set = f.get_all_file(mu)

for txt in file_set:
    # txt = r"C:\Users\Administrator\Desktop\长尾词2\Blazers.txt"
    # print(txt)
    l=t.get_txt_to_list_gaoxiao(txt)
    base = os.path.basename(txt).replace(".txt","")+'_l=r"""'
    # print(base)
    l=[' '+d for d in l]
    l=[base]+l+['"""']
    t.list_to_txt_append(l,r"C:\Users\Administrator\Desktop\长尾词2.txt")
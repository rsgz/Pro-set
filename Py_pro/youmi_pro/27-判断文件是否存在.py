from tool_rsgz.str.str import Str
from tool_rsgz.list.list import List
import os

image_paths = r"""
E:\pic\leimu\Dress\800x800\206109d390bb4457924ebcb68e478aeb.webp
E:\pic\leimu\Trousers\800x800\10f20bce4bfa4a1bae27a4479c86ee69.webp
E:\pic\leimu\Tank Tops\800x800\0e50113b3a1841ebaa99582e825cd1a0.webp
E:\pic\leimu\T-Shirts\800x800\165e2fd75e0849d19eb9181abadae4bb.webp
E:\pic\leimu\Sweater\800x800\18feba39f51a4566bb7f930a8b96652d.webp
E:\pic\leimu\Cardigans\800x800\06e5b0a3e08349e686ce18472347d751.webp
E:\pic\leimu\Blazers\800x800\blazer-by-skies-are-blue-in-black-size-2x-132-13219-294719.webp
E:\pic\leimu\Coats\800x800\231b23bbec0448a2a541b497ceafe75b.webp
E:\pic\leimu\Jackets\800x800\0a7e9eb7add04cce88e26f4acdf35a9f.webp
E:\pic\leimu\Hoodies\800x800\17d7e2351aac462b9c13da9d1e651520.webp
                        """

s=Str()
flag=0
img_set=s.str_to_list(image_paths)
for p in img_set:
    if not os.path.exists(p):
        flag=1
        print(p,"不存在!!!")
if flag==0:
    print("所有数据都存在")

l=List()
img_set = l.suiji_yuansu_n(img_set,10)
print(*img_set,sep="\n")
import re

new_lei = r"""
{'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720'},
{"Women's Jackets 夹克": '2252074725146624'},
{'Sweater 毛衣': '2252349770825728'},
{'T-Shirts T恤衫': '2252487025229824'},
{'Blouses 衬衫': '2252487075573760'},
{'Pants 长裤': '2252624464183296'},
{'Dress 连衣裙': '2252761936691200'},
{'Skirt 裙子': '2252762054131712'},
{'Party Dress 派对礼服': '2252761919913984'},
{'Mini Dresses 迷你连衣裙': '2252761987022848'},
"""

path_map = r"""
{'Blouses 衬衫': '2252487075573760'},-->r"E:\pic\leimu\Blouses\800x800"
{'Coats 外套': '2252074809032704'},-->r"E:\pic\leimu\Coats\800x800"
{'Cardigans 开衫': '2252349586276352'},-->r"E:\pic\leimu\Cardigans\800x800"
{'Trousers 裤子': '2252624682287104'},-->r"E:\pic\leimu\Trousers\800x800"
{'Sweatpants 运动裤': '2252624564846592'},-->r"E:\pic\leimu\Sweatpants\800x800"
{'Mini Dresses 迷你连衣裙': '2252761987022848'},-->r"E:\pic\leimu\Mini Dresses\800x800"
{'Swimsuit 泳装': '2252899509862400'},-->r"E:\pic\leimu\Swimsuit\800x800"
{'Bomber Jacket 飞行员夹克': '2252075228463104'},-->r"E:\pic\leimu\Bomber Jacket\800x800"
{'Polo Shirts 马球衫': '2252487327219712'},-->r"E:\pic\leimu\Polo Shirts\800x800"
{'Swimsuit 泳装': '2252899509862400'},-->r"E:\pic\leimu\Swimsuit\800x800"
{'Bras 胸罩': '3377974615220224'},-->r"E:\pic\leimu\Bras\800x800"
{'Crop Top  短款上衣': '2252487109115904'},-->r"E:\pic\leimu\Crop Top\800x800"
{'Bodysuits 连体衣': '2252487310442496'},-->r"E:\pic\leimu\Bodysuits\800x800"
{'Legging 紧身裤': '2252624531304448'},-->r"E:\pic\leimu\Legging\800x800"
{'Jersey 球衣': '2252487260110848'},-->r"E:\pic\leimu\Jersey\800x800"
{'Jeans 牛仔裤': '2252624598401024'},-->r"E:\pic\leimu\Jeans\800x800"
{'Romper 连身裤': '2252624833282048'},-->r"E:\pic\leimu\Romper\800x800"
{'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720'},-->r"E:\pic\leimu\Hoodies\800x800"
{"Women's Jackets 夹克": '2252074725146624'},-->r"E:\pic\leimu\Jackets\800x800"
{'Blazers 西装外套': '2252074859364352'},-->r"E:\pic\leimu\Blazers\800x800"
{'T-Shirts T恤衫': '2252487025229824'},-->r"E:\pic\leimu\T-Shirts\800x800"
{'Pants 长裤': '2252624464183296'},-->r"E:\pic\leimu\Pants\800x800"
{'Jumpsuit  连体裤': '2252624480960512'},-->r"E:\pic\leimu\Jumpsuit\800x800"
{'Dress 连衣裙': '2252761936691200'},-->r"E:\pic\leimu\Dress\800x800"
{'Skirt 裙子': '2252762054131712'},-->r"E:\pic\leimu\Skirt\800x800"
{'Party Dress 派对礼服': '2252761919913984'},-->r"E:\pic\leimu\Party Dress\800x800"
{'Bikini 比基尼': '2252899409199104'},-->r"E:\pic\leimu\Bikini\800x800"
{'Pullovers 套头衫': '2252349603053568'},-->r"E:\pic\leimu\Pullovers\800x800"
{'Sweater 毛衣': '2252349770825728'},-->r"E:\pic\leimu\Sweater\800x800"
{'Tank Tops & Camis 背心': '2252487042007040'},-->r"E:\pic\leimu\Tank Tops\800x800"
"""

line2_mei_zhao_dao_l=[]
# 上面的new_lei 来打印对应顺序的路径，路径数据path_map也有提供  使用python
def get_paths_by_lei(new_lei_str, path_map_str):
    # 解析 path_map 字符串   数据库
    print(r'''r"E:\pic\shangpin\800x800",''')
    for line2 in new_lei.strip().split('\n'):  # 输入数据 类目
        for line_sql in path_map_str.strip().split('\n'):
            leimu, path = line_sql.split("-->")
            if leimu in line2:
                print(f"{path},")
                flag=1
                break
            else:
                flag=0
        if flag==0:
            tiqu_data = line2.split(':')[0].replace("{", "")[1:-1]  # 'Pullovers 套头衫'
            line2_mei_zhao_dao_l.append(f'{line2}-->r"E:\pic\leimu\\{tiqu_data}\800x800",')

# 获取路径
get_paths_by_lei(new_lei, path_map)

print("没找到的数据")
print(*line2_mei_zhao_dao_l,sep="\n")
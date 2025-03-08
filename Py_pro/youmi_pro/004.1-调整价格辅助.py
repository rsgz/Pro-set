# 定义 web_lei 和 price_qujian

data = (235, {'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720', 'T-Shirts T恤衫': '2252487025229824', 'Legging 紧身裤': '2252624531304448', 'Pants 长裤': '2252624464183296', 'Sweatpants 运动裤': '2252624564846592', 'Jeans 牛仔裤': '2252624598401024', 'Dress 连衣裙': '2252761936691200', 'Party Dress 派对礼服': '2252761919913984', 'Mini Dresses 迷你连衣裙': '2252761987022848', 'Swimsuit 泳装': '2252899509862400'})
web_lei =data[1]

price_qujian = {
    "Hoodies & Sweatshirts 连帽衫和运动衫": (39, 45),
    "Coats 外套": (59, 75),
    "Sweatpants 运动裤": (33, 46),
    "Women's Jackets 夹克": (55, 99),
    'Blazers 西装外套': (62, 71),
    'Cardigans 开衫': (42, 66),
    'Knit Tops 毛织上衣': (38, 48),
    'T-Shirts T恤衫': (27, 37),
    # 'Jersey 球衣': (32, 36),
    'Trousers 裤子': (30, 38),
    'Dress 连衣裙': (55, 68),
    'Party Dress 派对礼服': (55, 68),
    "Sweater 毛衣":(38,55),
    "Crop Top  短款上衣":(28,38),
    "Pants 长裤":(31,42),
    "Skirt 裙子":(38,70),
    "Outerwears 外套":(38,70),
    "Bodysuits 连体衣":(38,50),
    "Parka 派克大衣":(55,79),
    "Tank Tops & Camis 背心":(29,35),
    "Pullovers 套头衫":(38,65),
    "Shawl 披肩":(38,65),
    "Jersey 球衣":(32,45),
    "Legging 紧身裤":(35,48),
    "Jumpsuit  连体裤":(38,55),
    "Mini Dresses 迷你连衣裙":(38,58),
    "Bikini 比基尼":(38,55),
    "Jeans 牛仔裤":(38,55),
    "Romper 连身裤":(38,55),
    "Bomber Jacket 飞行员夹克":(62,99),
    "Polo Shirts 马球衫":(38,55),
    "Swimsuit 泳装":(38,55),
    "Bras 胸罩":(35,55),
}

# 假设 websiteId 和 headers 已经定义
websiteId = 836

# 遍历 web_lei 并生成 shoujia 函数调用
not_name_l = []
print("已经匹配的价格")
for name, id in web_lei.items():
    if name in price_qujian:
        minUnitPrice, maxUnitPrice = price_qujian[name]
        print(f'shoujia(websiteId=websiteId, name="{name}", id="{id}", headers=headers, minUnitPrice={minUnitPrice}, maxUnitPrice={maxUnitPrice})')
    else:
        not_name_l.append(name)
print("\n需要定义的价格函数")
print(*not_name_l,sep='\n')
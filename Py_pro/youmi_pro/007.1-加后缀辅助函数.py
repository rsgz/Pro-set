# 定义 web_data 和 func_l
web_data = (974, {'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720', "Women's Jackets 夹克": '2252074725146624', 'Sweater 毛衣': '2252349770825728', 'T-Shirts T恤衫': '2252487025229824', 'Blouses 衬衫': '2252487075573760', 'Pants 长裤': '2252624464183296', 'Dress 连衣裙': '2252761936691200', 'Skirt 裙子': '2252762054131712', 'Party Dress 派对礼服': '2252761919913984', 'Mini Dresses 迷你连衣裙': '2252761987022848'})

func_l = r"""
    add_houzhui(websiteId=websiteId, classificationId='2252624564846592', newValue=Sweatpants_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487327219712', newValue=Polo_Shirts_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624833282048', newValue=Romper_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2251937252638720', newValue=Hoodie_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074809032704', newValue=Coats_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074725146624', newValue=Jackets_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349586276352', newValue=Cardigans_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349770825728', newValue=Sweater_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349603053568', newValue=Pullovers_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487025229824', newValue=T_Shirts_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487109115904', newValue=Crop_Top_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487042007040', newValue=Tank_Tops_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624682287104', newValue=Trousers_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761936691200', newValue=Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761919913984', newValue=Party_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762054131712', newValue=Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074859364352', newValue=Blazers_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349653385216', newValue=Knit_Tops_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487260110848', newValue=Jersey_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075329126400', newValue=Outerwears_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075262017536', newValue=Overalls_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074993582080', newValue=Overcoat_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074892918784', newValue=Vest_Coats_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075228463104', newValue=Bomber_Jacket_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487075573760', newValue=Blouses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624497737728', newValue=Shorts_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487276888064', newValue=Bottoming_Shirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487293665280', newValue=Sun_Protection_Clothing_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624665509888', newValue=Overalls_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349754048512', newValue=Woolen_Sweater_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624548069376', newValue=Bottom_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252899509862400', newValue=Swimsuit_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='3377974615220224', newValue=Bras_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762205126656', newValue=Floral_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075043913728', newValue=Raincoat_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074775478272', newValue=Down_Coats_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075278794752', newValue=Ski_Suit_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075027136512', newValue=Cape_Coats_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487193001984', newValue=Top_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624464183296', newValue=Pants_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074758701056', newValue=Trench_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252075362680832', newValue=Shawl_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074708369408', newValue=Waistcoats_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487075565568', newValue=Short_Sleeve_Shirts_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761987022848', newValue=Mini_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762020577280', newValue=Maxi_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624598401024', newValue=Jeans_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624531304448', newValue=Legging_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762003800064', newValue=Midi_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762070908928', newValue=Wrap_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252487310442496', newValue=Bodysuits_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252624480960512', newValue=Jumpsuit_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252899409199104', newValue=Bikini_l.rstrip())
"""

# 提取 data 字典（假设 web_data 已定义）
data = web_data[1]

# 提取 data 中的所有 id
ids = set(data.values())

# 将 func_l 按行拆分为列表
func_lines = func_l.strip().split('\n')
func_lines = [f.strip() for f in func_lines]

# 遍历 func_lines，检查是否包含 data 中的 id
not_found = []
found_l = []
print("已经有的id")
for id in ids:  # 这是每个网站的id
    found = False
    for func in func_lines:  # 这是历史函数列表
        if id in func:
            found_l.append(func)
            found = True
    if not found:
        not_found.append(id)
print("xxxxxxxx",*found_l, sep='\n')

print("没找到的id")
# print(*[kv for kv in data.items() if kv[1] in not_found],sep='\n')
not_fonund_dict = [f'''add_houzhui(websiteId=websiteId, classificationId='{kv[1]}', newValue={kv[0]}_l.rstrip())''' for kv in data.items() if kv[1] in not_found]
print(*not_fonund_dict,sep='\n')
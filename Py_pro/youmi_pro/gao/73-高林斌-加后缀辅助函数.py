# 定义 web_data 和 func_l
web_data =(1,{'Hoodies & Sweatshirts 连帽衫和运动衫': '2251937252638720',
'Sweater 毛衣': '2252349754048512',
'Mini Dresses 迷你连衣裙': '2252761987022848',
'Midi Dresses 中长连衣裙': '2252762003800064',
'Maxi Dresses 长连衣裙': '2252762020577280',
'Party Dress 派对连衣裙': '2252761919913984',
'Wedding Dress 婚礼连衣裙': '2252761953468416',
'Floral Dress 碎花连衣裙': '2252762054131712',
'Unclassified Dresses 未分类连衣裙': '2252761936691200',
'Unclassified Skirt 未分类裙子': '2252761970245632',
'Mini Skirt 迷你裙': '2252762087686144',
'Midi Skirt 中长裙': '2252762104463360',
'Maxi Skirt 长裙': '2252762121240576',
'Suspender Dress 吊带连衣裙': '2252762138017792',
'Sequin Dress 亮片连衣裙': '2252762171572224',
'Tulle Dress 薄纱连衣裙': '2252762188349440',
'Shirt Dress 衬衫连衣裙': '2252762205126656',
'Denim Skirt 牛仔裙': '2252762221903872',
'Lace Dress 蕾丝连衣裙': '2252762255458304',
'Pencil Skirt 铅笔裙': '2252762272235520',
'Tank Dress 背心连衣裙': '2252762154795008',
'Sweater Dresses 毛织连衣裙': '2252762238681088',
'Swimsuit 泳衣': '2252899509862400',})

func_l = r"""
    add_houzhui(websiteId=websiteId, classificationId='2252899509862400', newValue=Swimsuit_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074725146624', newValue=Womens_Jackets_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252349754048512', newValue=Sweater_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761987022848', newValue=Mini_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762003800064', newValue=Midi_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762020577280', newValue=Maxi_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761903136768', newValue=Bodycon_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761919913984', newValue=Party_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761953468416', newValue=Wedding_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762037354496', newValue=Plus_Size_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762054131712', newValue=Floral_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761936691200', newValue=Unclassified_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252761970245632', newValue=Unclassified_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762087686144', newValue=Mini_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762104463360', newValue=Midi_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762121240576', newValue=Maxi_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762171572224', newValue=Sequin_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762188349440', newValue=Tulle_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762205126656', newValue=Shirt_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762221903872', newValue=Denim_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762255458304', newValue=Lace_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762238681088', newValue=Sweater_Dresses_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='3377837176258560', newValue=Pajama_Sets_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='3377837193035776', newValue=Robe_Gown_Sets_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762070908928', newValue=Long_Sleeved_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762272235520', newValue=Pencil_Skirt_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762138017792', newValue=Suspender_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252762154795008', newValue=Tank_Dress_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2251937252638720', newValue=Hoodies_Sweatshirts_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074859364352', newValue=Blazers_l.rstrip())
    add_houzhui(websiteId=websiteId, classificationId='2252074876141568', newValue=Pullovers_l.rstrip()) 
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
print(*found_l, sep='\n')

print("没找到的id")
# print(*[kv for kv in data.items() if kv[1] in not_found],sep='\n')
not_fonund_dict = [f'''add_houzhui(websiteId=websiteId, classificationId='{kv[1]}', newValue={kv[0]}_l.rstrip())''' for kv in data.items() if kv[1] in not_found]
print(*not_fonund_dict,sep='\n')
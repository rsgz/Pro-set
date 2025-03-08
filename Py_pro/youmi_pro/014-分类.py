import json,requests,os
from settings import authorization
# authorization 同步
from tool_rsgz import s,info

class Fen:
    def __init__(self,keywords,paichu_str,classificationId_daiding,newValue):
        # self.keywords = keywords
        # self.classificationId_daiding = classificationId_daiding
        # self.paichu_str = paichu_str
        # self.newValue = newValue
        self.action_name = "goods.update.batch"
        self.authorization = authorization
        self.json_data = {
            'options': {
                'keywords': keywords,
                'classificationId': classificationId_daiding,
                'searchHierarchyMethod': 0,
                "shieldLabels": paichu_str,
            },
            'updateColumns': [
                {
                    'name': 'classificationId',
                    'operator': 0,
                    'newValue': newValue,
                },
            ],
            "updateDetailColumns": []
        }

        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'action-name': self.action_name,
            'authorization': self.authorization,
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://b08-admin.shop6888.com',
            'priority': 'u=1, i',
            'referer': 'https://b08-admin.shop6888.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        print("执行分类操作!")
        self.fenlei()

    def fenlei(self):
        response = requests.post('https://b08-api.shop6888.com/apis/Action', headers=self.headers, json=self.json_data)
        print(response.json())
        num = response.json()["message"].replace("成功更新 ","").replace(" 条记录","")
        print("{} 条！！！！！！！\n".format(num)*5)
        # info("{} 条！！！！！！！\n".format(num))

def load_inputs(filename="inputs.json"):
    if os.path.exists(filename):
        with open(filename, "r",encoding="utf-8") as file:
            return json.load(file)
    return {}

# 读取网站所有类目 id
suoyou_leimu_json = r"suoyouleimu.json"
suoyou_leimu_json_data = load_inputs(filename=suoyou_leimu_json)

obj = suoyou_leimu_json_data["response"]
def tiqu(obj,find_id):
    zu_dict = {}
    for zu in obj:
        if not zu["children"]:
            # print(zu["id"], "-->", zu["title"])
            # print(find_id,zu["id"],zu["title"])
            if find_id==zu["id"]:
                # print(zu["title"])
                return zu["title"]

        else:
            zu2 = zu["children"]
            result = tiqu(obj=zu2,find_id=find_id)
            if result is not None:
                return result

# print(suoyou_leimu_json_data)
if __name__ == '__main__':
    n_set = [305,306,307,14,16,17,18,19,20,21,22,23,24,26,25,6,28,29,119,120,121,30,122,123,124,125,126,31,32,33,34,35,36,37,39,40,41,42,43,
46,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,
92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,116,117,44,127,128,129,130,131,132,133,134,135,
136,137,138,139,140,141,142,143,144,145,146,147,148,15,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,
168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,
201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,
234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,
267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,
300,301,302,303,13,12,11,10,9,7,6,5,4,3,2,1,
44, 61, 62, 115
             # 44,61,62,115
             ]
    for n in n_set:
        # n=n_set[-1]  # 开始分类哪一个类目
        # n=14  # 开始分类哪一个类目
        fenlei_data = load_inputs("fenlei_id.json")
        def find_n(n):
            return [data for data in fenlei_data["data"] if data["id"]==n][0]
        data = find_n(n=n)
        keywords=data["guanjianci"]
        if data['paichu_guanjianci'] == "":
            paichu_str = s(keywords)
        else:
            paichu_str = data['paichu_guanjianci']+","+s(keywords)

        classificationId_daiding=data["laiyuanid"]
        newValue =data["xin_id"]
        find_title = tiqu(obj, newValue)
        print(newValue,'-->',find_title,"验证？")
        laiyuan_leimu_ming = data["laiyuan_leimu_ming"]
        xin_leimu_ming = data["xin_leimu_ming"]
        if find_title.strip()==xin_leimu_ming.strip():
            print("=============数据验证正确!!!=============")
            print(classificationId_daiding, "-->", laiyuan_leimu_ming)
            print("包含：",keywords)
            print("屏蔽：",paichu_str)
            print(newValue,"-->",xin_leimu_ming,"--->",n)
            Fen(keywords,paichu_str,classificationId_daiding,newValue)
        else:
            print("=============数据可能有问题!=============")
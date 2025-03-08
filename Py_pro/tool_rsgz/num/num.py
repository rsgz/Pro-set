import random


class Num:
    def __init__(self):
        pass

    # 生成美国电话
    def shengcheng_meiguo_haoma(self):
        r"""生成美国号码"""
        r"""
        # 示例调用
        random_phone = shengcheng_meiguo_haoma()
        print(random_phone)
        """
        # 随机生成区号（3位数字，避免以0开头）
        area_code = random.randint(200, 999)

        # 随机生成电话号的前3位
        first_part = random.randint(100, 999)

        # 随机生成电话号的后4位
        second_part = random.randint(1000, 9999)

        # 组合成电话号码格式
        phone_number = f"+1 ({area_code}) {first_part}-{second_part}"
        return phone_number
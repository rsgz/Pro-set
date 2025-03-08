import random


class List:
    def __init__(self):
        pass


    # 列表随机几个元素
    def suiji_yuansu_n(self,my_list,n):
        r"""列表随机几个元素"""
        r"""
        s = suiji_yuansu(my_list=lanmu_biaoti,n=3)
        print(s)  # ['Consumption Voucher Distribution', 'Best-Selling Products', 'Mega Sale']
        """
        # import random
        if n > len(my_list):
            raise ValueError("选择的元素数量不能大于列表的长度")
        # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 从列表中随机选择5个不重复的元素
        random_elements = random.sample(my_list, n)
        # print(random_elements)
        return random_elements

    # 随机一个元素
    def suiji_one(self,my_list):
        r"""随机一个元素"""
        return self.suiji_yuansu_n(my_list=my_list, n=1)[0]

    
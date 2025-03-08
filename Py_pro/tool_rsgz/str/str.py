

class Str:
    def __init__(self):
        pass

    # 竖着打印变量
    def prints(self,list_obj):
        r"""竖着打印变量"""
        print(*list_obj,sep="\n")

    # 一行打印几个
    def print_hang(self,l, n):
        r"""
        一行打印几个
        """
        r"""
        hang(l=zhichi_format,n=5)
        :param n: 将集合打印出来的话  你要求打印出一列 多个少元素
        :param l: 就是你想打印的 集合
        """
        for i, kv in enumerate(l):
            if i != 0 and i % n == 0:
                print()  # 换行
            print(kv, end=" ")

    # 字符串转列表
    def str_to_list(self,u_str):
        r"""
        pic_l2 = r'''
            "E:\pic\shangpin\800x800\mylie-deep-slit-maxi-dress.webp"
            "E:\pic\shangpin\800x800\wrap-up-coverup-skirt-royal-blue.webp"
        '''
        """
        return [line.strip('"').strip() for line in u_str.splitlines() if line.strip()]

    # 分组打印
    def dayin_dijizu(self,list_data,yizu_jige,dijizu,head_info=""):
        r"""分组打印  之前填表用的 改标题 优米科技"""
        l=list_data
        l2 = [head_info + str(data) for data in list_data]
        # i = 8  # 8-->3-1
        n = dijizu * yizu_jige
        print(*l2[0 + n:yizu_jige + n], sep="\n")

if __name__ == '__main__':
    s = Str()
    # s.prints([1,2,3])
    u_str=r"""
    111
    """
    s.str_to_list(u_str=u_str)
    l=[1,2,3,4,5,6,7,8,9]
    s.dayin_dijizu(list_data=l,yizu_jige=2,dijizu=2)



web_set = r"""
xyvon.store
kyxon.store
sytox.store
uvixy.store
bynix.store
koxen.store
hexum.store
duvex.store
daxor.store
fynor.store
xelro.store
nexix.store
jivex.store
sivon.store
tovex.store
vevol.store
zoryx.store
givon.store
uvexi.store
syxon.store
xivex.store
tixum.store
zyrex.store
vovox.store
ralvo.store
xirra.store
yuxer.store
wynor.store
zexum.store
syvex.store
oryxe.store
kevix.store
qubera.store
sygix.store
wivix.store
quvix.store
pimex.store
firdo.store
yalvo.store
vixon.store
"""

# 字符串转列表
def str_to_list(u_str):
    r"""
    pic_l2 = r'''
"E:\pic\shangpin\800x800\mylie-deep-slit-maxi-dress.webp"
"E:\pic\shangpin\800x800\wrap-up-coverup-skirt-royal-blue.webp"
    '''
    """
    return [line.strip('"') for line in u_str.splitlines() if line.strip()]

start=925
l=str_to_list(web_set)
l2=[f'"{i+start:}":"https://{k}",' for i,k in enumerate(l)]
l3=l2[::-1]
# print(*l2,sep="\n")  # 小-->大
print(*l3,sep="\n")  # 大-->小
from tool_rsgz.str.str import Str

# 这个是 某一天给的域名  包含了 有效的 和失效的 两种
hao_17={
"964":"https://vixon.store",  # 2025-02-24 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
"963":"https://yalvo.store",
"962":"https://firdo.store",
"961":"https://pimex.store",
"960":"https://quvix.store",
"959":"https://wivix.store",
"958":"https://sygix.store",
"957":"https://qubera.store",
"956":"https://kevix.store",
"955":"https://oryxe.store",
"954":"https://syvex.store",  # 2025-02-24
"953":"https://zexum.store",
"952":"https://wynor.store",
"951":"https://yuxer.store",
"950":"https://xirra.store",
"949":"https://ralvo.store",
"948":"https://vovox.store",
"947":"https://zyrex.store",
"946":"https://tixum.store",
"945":"https://xivex.store",
"944":"https://syxon.store",
"943":"https://uvexi.store",
"942":"https://givon.store",
"941":"https://zoryx.store",
"940":"https://vevol.store",
"939":"https://tovex.store",
"938":"https://sivon.store",
"937":"https://jivex.store",
"936":"https://nexix.store",
"935":"https://xelro.store",
"934":"https://fynor.store",
"933":"https://daxor.store",
"932":"https://duvex.store",
"931":"https://hexum.store",
"930":"https://koxen.store",
"929":"https://bynix.store",
"928":"https://uvixy.store",
"927":"https://sytox.store",
"926":"https://kyxon.store",
"925":"https://xyvon.store", # 2025-02-24 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
"924":"https://nivro.store", # 2025-02-17 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
"923":"https://vexol.store",
"922":"https://zylvo.store",
"921":"https://pixyo.store",
"920":"https://zexly.store",
"919":"https://zifyo.store",
"918":"https://wovix.store",
"917":"https://wixio.store",
"916":"https://zioxy.store",
"914":"https://zzyxo.store",
"912":"https://zexyl.store",
"911":"https://zixlo.store",
"910":"https://zlyra.store",
"909":"https://vexzo.store",
"908":"https://zyzol.store",
"907":"https://zymex.store",
"906":"https://lyzor.store",
"904":"https://zifro.store",
"903":"https://vynex.store",
"902":"https://mixro.store",
"901":"https://vezlo.store",
"900":"https://zimro.store",
"899":"https://zizlo.store",
"898":"https://wexlo.store",
"897":"https://zolzo.store",
"895":"https://xyner.store",  # 2025-02-17 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑
}

# 这个是能用的域名
nengyong=r"""
xyzol.store
zyxor.store
zyxra.store
vexzi.store
xivro.store
tiexo.store
gexro.store
zixxa.store
zimor.store
mixza.store
zyxro.store
zypix.store
syvio.store
zynzo.store
"""

# 打印出 没失效的
s=Str()
neng_l = s.str_to_list(u_str=nengyong)
for n in neng_l:
    for i,k in hao_17.items():
        if n in k:
            print(i,k)

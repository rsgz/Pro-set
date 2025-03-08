import tkinter as tk
from tkinter import messagebox

# 分析特殊单词去掉了 dress +es
def panduan_es_danci(mubiao):
    es_danci = ["dress"]
    for danci in es_danci:
        if danci.lower() in mubiao.lower():
            return 1

# 分析一个单词
def z(base_string):
    # base_string = "vest"
    combinations = []
    # 遍历所有小写字母
    for letter in map(chr, range(ord('a'), ord('z') + 1)):
        combinations.append(letter + base_string)
        if letter=="s":
            continue
        if letter=="e" and panduan_es_danci(mubiao=base_string):
            continue
        combinations.append(base_string+letter)
    return combinations


# 分析一群单词 去掉了s
def s(str_s):
    dict_big = []
    for danci in str_s.split(","):
        danci = danci.strip()
        dict = z(danci)
        dict_big = dict_big+dict
    str_danci = ','.join(dict_big)
    return str_danci

# print(s("vest, gao, haode ,zhen"))
# avest,vesta,bvest,vestb,cvest,vestc,dvest,vestd,evest,veste,fvest,vestf,gvest,vestg,hvest,vesth,ivest,vesti,jvest,vestj,kvest,vestk,lvest,vestl,mvest,vestm,nvest,vestn,ovest,vesto,pvest,vestp,qvest,vestq,rvest,vestr,svest,tvest,vestt,uvest,vestu,vvest,vestv,wvest,vestw,xvest,vestx,yvest,vesty,zvest,vestz,agao,gaoa,bgao,gaob,cgao,gaoc,dgao,gaod,egao,gaoe,fgao,gaof,ggao,gaog,hgao,gaoh,igao,gaoi,jgao,gaoj,kgao,gaok,lgao,gaol,mgao,gaom,ngao,gaon,ogao,gaoo,pgao,gaop,qgao,gaoq,rgao,gaor,sgao,tgao,gaot,ugao,gaou,vgao,gaov,wgao,gaow,xgao,gaox,ygao,gaoy,zgao,gaoz,ahaode,haodea,bhaode,haodeb,chaode,haodec,dhaode,haoded,ehaode,haodee,fhaode,haodef,ghaode,haodeg,hhaode,haodeh,ihaode,haodei,jhaode,haodej,khaode,haodek,lhaode,haodel,mhaode,haodem,nhaode,haoden,ohaode,haodeo,phaode,haodep,qhaode,haodeq,rhaode,haoder,shaode,thaode,haodet,uhaode,haodeu,vhaode,haodev,whaode,haodew,xhaode,haodex,yhaode,haodey,zhaode,haodez,azhen,zhena,bzhen,zhenb,czhen,zhenc,dzhen,zhend,ezhen,zhene,fzhen,zhenf,gzhen,zheng,hzhen,zhenh,izhen,zheni,jzhen,zhenj,kzhen,zhenk,lzhen,zhenl,mzhen,zhenm,nzhen,zhenn,ozhen,zheno,pzhen,zhenp,qzhen,zhenq,rzhen,zhenr,szhen,tzhen,zhent,uzhen,zhenu,vzhen,zhenv,wzhen,zhenw,xzhen,zhenx,yzhen,zheny,zzhen,zhenz



def info(infos):
    # 创建主窗口并隐藏之（因为我们只想要一个消息框）
    # root = tk.Tk()
    # root.withdraw()  # 隐藏主窗口

    # 显示消息框
    messagebox.showinfo("提示",infos)

    # 如果您希望程序在此等待用户关闭消息框后才退出，可以添加如下代码：
    # root.mainloop()
#程序内部结构一览
import time
import random
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y
rzl='''
 21:
 10/20(beta)
 10/21(beta)
 10/30(beta)
 10/31(beta)
 11/4(beta)
 11/5(v1.0)正式版上线
 11/6(v1.1)加入防沉迷系统(未实装)
'''
zzrmd='''
 制作人:
 NNzyo
 制作指导：
 NNzyo
 辅助:
 NNzyo
 赞助:
 NNzyo
'''
xiex1='''————————————————————————————'''
xiex2='''|
|
|
|
|
|
|
|
|
|
|
|
|
|

'''
tips = ['tip:履刑者抽卡全保底(','tip:tips','tip:这是很冷的冷知识','tip:这是很烫的热知识','tip:在？植个发？','tip:原来你也玩原神?','tip:我们联合!','tip:为斯卡蒂献上心脏!','tip:来跟我读p-r-o','tip:有BUG咩?','tip:这里是船馨版本','tip:告诉你tip有12条!']
upkac = ['可莉(火)五星','诺艾尔(岩)四星','班尼特(火)四星','以理服人(二星)','砂糖(风)四星','训练大刀(一星)']
wpkac = ['四风原典(五星)','试作斩岩(四星)','以理服人(二星)','咸鱼大剑(四星)','训练大刀(一星)']
yuanshi=0
def egg():#egg
    exit()
def mian_choice():#选择
    window=tk.Tk()
    window.title('选择')
    window.geometry('400x250')#窗口
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
    tk.Label(window,text='please choice',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
    c1=tk.Button(window, text='原神',font=('wtf',20),width=7,height=1,command=Genshen)
    c1.place(x=60, y=150)
    c2=tk.Button(window, text='明日方舟',font=('wtf',20),width=7,height=1,command=Mrfz)
    c2.place(x=220, y=150)
def setr():#设置
    window=tk.Tk()
    window.title('设置')
    window.geometry('400x250')
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
    tk.Button(window, text='日志',font=('wtf',20),width=5,height=1,command=doubt).place(x=60, y=150)
    tk.Button(window, text='制作人',font=('wtf',20),width=5,height=1,command=zzr).place(x=160, y=150)
def zzr():#制作人名单
    window=tk.Tk()
    window.title('制作人名单')
    window.geometry('200x350')#窗口
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=320)
    tk.Label(window,text=zzrmd,font=('Arial',15)).place(x=0, y=0)
def doubt():#更新日志
    window=tk.Tk()
    window.title('更新日志')
    window.geometry('400x250')#窗口
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
    tk.Label(window,text=rzl,font=('wtf',15)).place(x=0, y=0)
def Genshen():#原神
    def wqc():
        window=tk.Tk()
        window.title('原神WQ')
        window.geometry('700x500')#窗口
        tip=random.choice(tips)
        tk.Label(window,text=tip,font=('wtf',15)).place(x=0, y=470)
        tk.Label(window,text=xiex1,font=('wtf',15)).place(x=60, y=40)
        tk.Label(window,text=xiex1,font=('wtf',15)).place(x=60, y=315)
        tk.Label(window,text=xiex2,font=('wtf',15)).place(x=60,y=47)
        tk.Label(window,text=xiex2,font=('wtf',15)).place(x=610,y=47)
        tk.Label(window,text='武器',font=('wtf',100)).place(x=310,y=150)
        tk.Label(window,text='概率UP',font=('wtf',20)).place(x=70,y=100)
        def wqcx1():
            window=tk.Tk()
            window.title('结果')
            window.geometry('400x250')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
            tk.Label(window,text='你获得了:',font=('wtf',17)).place(x=0,y=0)
            time.sleep(3)
            jg=random.choices(wpkac,weights=[0.6,2.5,7,2.5,8])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=30)
            print('ys武器池x1:',jg)
        def wqcx10():
            window=tk.Tk()
            window.title('结果')
            window.geometry('400x370')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=340)
            tk.Label(window,text='你获得了:',font=('wtf',17)).place(x=0,y=0)
            time.sleep(3)
            print('ys武器池x10:')
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=30)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=60)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=90)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=120)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=150)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=180)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=210)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=240)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=270)
            print(jg)
            jg=random.choices(wpkac,weights=[0.06,0.25,4,0.25,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=300)
            print(jg)
        def wqckxm():
            window=tk.Tk()
            window.title('卡池')
            window.geometry('850x150')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=120)
            tk.Label(window,text='池子:',font=('wtf',17)).place(x=0,y=0)
            tk.Label(window,text=wpkac,font=('wtf',17)).place(x=0,y=30)
        tk.Button(window, text='☆:∞',font=('wtf',12),width=6,height=1).place(x=640, y=0)
        tk.Button(window, text='池子',font=('wtf',12),width=6,height=1,command=wqckxm).place(x=640, y=30)
        tk.Button(window, text='一发 160',font=('wtf',15),width=9,height=1,command=wqcx1).place(x=360, y=315)
        tk.Button(window, text='十发 1600',font=('wtf',15),width=9,height=1,command=wqcx10).place(x=490, y=315)
    def upc():
        window=tk.Tk()
        window.title('原神UP')
        window.geometry('700x500')#窗口
        tip=random.choice(tips)
        tk.Label(window,text=tip,font=('wtf',15)).place(x=0, y=470)
        tk.Label(window,text=xiex1,font=('wtf',15)).place(x=60, y=40)
        tk.Label(window,text=xiex1,font=('wtf',15)).place(x=60, y=315)
        tk.Label(window,text=xiex2,font=('wtf',15)).place(x=60,y=47)
        tk.Label(window,text=xiex2,font=('wtf',15)).place(x=610,y=47)
        tk.Label(window,text='人',font=('wtf',100)).place(x=410,y=150)
        tk.Label(window,text='概率UP',font=('wtf',20)).place(x=70,y=100)
        def upcx1():
            window=tk.Tk()
            window.title('结果')
            window.geometry('400x250')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
            tk.Label(window,text='你获得了:',font=('wtf',17)).place(x=0,y=0)
            time.sleep(3)
            jg=random.choices(upkac,weights=[0.5,2,2,7,2,8])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=30)
            print('ysup池x1:',jg)
        def upcx10():
            window=tk.Tk()
            window.title('结果')
            window.geometry('400x370')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=340)
            tk.Label(window,text='你获得了:',font=('wtf',17)).place(x=0,y=0)
            time.sleep(3)
            print('ysup池x10:')
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=30)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=60)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=90)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=120)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=150)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=180)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=210)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=240)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=270)
            print(jg)
            jg=random.choices(upkac,weights=[0.05,0.2,0.2,2,0.2,3])
            tk.Label(window,text=jg,font=('wtf',17)).place(x=0,y=300)
            print(jg)
        def upckxm():
            window=tk.Tk()
            window.title('卡池')
            window.geometry('850x150')#窗口
            tip=random.choice(tips)
            tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=120)
            tk.Label(window,text='池子:',font=('wtf',17)).place(x=0,y=0)
            tk.Label(window,text=upkac,font=('wtf',17)).place(x=0,y=30)
        tk.Button(window, text='☆:',font=('wtf',12),width=6,height=1).place(x=640, y=0)
        tk.Button(window, text='池子',font=('wtf',12),width=6,height=1,command=upckxm).place(x=640, y=30)
        tk.Button(window, text='一发 160',font=('wtf',15),width=9,height=1,command=upcx1).place(x=360, y=315)
        tk.Button(window, text='十发 1600',font=('wtf',15),width=9,height=1,command=upcx10).place(x=490, y=315)
    def Genshin_choice():
        window=tk.Tk()
        window.title('卡池选择')
        window.geometry('400x250')#窗口
        tip=random.choice(tips)
        tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
        tk.Label(window,text='please choice',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
        c3=tk.Button(window, text='UP池',font=('wtf',20),width=7,height=1,command=upc)
        c3.place(x=60, y=150)
        c4=tk.Button(window, text='武器池',font=('wtf',20),width=7,height=1,command=wqc)
        c4.place(x=220, y=150)
    Genshin_choice()
def Mrfz():#明日方舟
    window=tk.Tk()
    window.title('明日方舟')
    window.geometry('700x500')#窗口
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=470)
    tk.Label(window,text=('敬请期待(预计v2.0)'),font=('wtf',50)).place(x=50,y=50)
def fcmty():
    window=tk.Tk()
    window.title('《用户隐私保护》')
    window.geometry('400x250')#窗口
    tk.Label(window,text='无法连接服务器',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
def fcm18():
    window=tk.Tk()
    window.title('防沉迷系统')
    window.geometry('400x250')#窗口
    tk.Label(window,text='tip:You 18↓ or 18↑?',font=('wtf',15)).place(x=0,y=220)
    tk.Label(window,text='防沉迷系统',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
    tk.Label(window,text='根据国家规定打造',font=('wtf',20),width=16, height=1).place(x=84,y=85)
    tk.Label(window,text='验证即自动同意',font=('wtf',10),width=16, height=1).place(x=90,y=115)
    def fcm18mian1():
        window.title('防沉迷系统')
        window.geometry('400x250')#窗口
        tk.Label(window,text='tip:You 18↓ or 18↑?',font=('wtf',15)).place(x=0,y=220)
        tk.Label(window, text='真实姓名: ').place(x=10, y=10)
        tk.Entry(window).place(x=150, y=10)
        tk.Label(window, text='身份证号: ').place(x=10, y=50)
        tk.Entry(window).place(x=150, y=50)
    tk.Button(window, text='《用户隐私保护》',font=('wtf',8),width=15,height=1,command=fcmty).place(x=195, y=115)
    tk.Button(window, text='开验',font=('wtf',20),width=5,height=1,command=fcm18mian1).place(x=75, y=150)
    tk.Button(window, text='退出',font=('wtf',20),width=5,height=1,command=exit).place(x=240, y=150)
def fcm18():
    window=tk.Tk()
    window.title('防沉迷系统')
    window.geometry('400x250')#窗口
    tk.Label(window,text='tip:You 18↓ or 18↑?',font=('wtf',15)).place(x=0,y=220)
    tk.Label(window,text='防沉迷系统',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
    tk.Label(window,text='根据国家规定打造',font=('wtf',20),width=16, height=1).place(x=84,y=85)
    tk.Label(window,text='验证即自动同意',font=('wtf',10),width=16, height=1).place(x=90,y=115)
    def fcm18mian1():
        window=tk.Tk()
        window.title('防沉迷系统')
        window.geometry('500x250')#窗口
        tk.Label(window,text='tip:身份证绑定成功后不能更改',font=('wtf',15)).place(x=0,y=220)
        tk.Label(window, text='真实姓名: ',font=('wtf',20)).place(x=10, y=10)
        tk.Entry(window,font=('wtf',20)).place(x=150, y=10)
        tk.Label(window, text='身份证号: ',font=('wtf',20)).place(x=10, y=50)
        tk.Entry(window,font=('wtf',20)).place(x=150, y=50)
        tk.Button(window, text='验证',font=('wtf',20),width=5,height=1,command=mian).place(x=240, y=100)
    tk.Button(window, text='《用户隐私保护》',font=('wtf',8),width=15,height=1,command=fcmty).place(x=195, y=115)
    tk.Button(window, text='开验',font=('wtf',20),width=5,height=1,command=fcm18mian1).place(x=75, y=150)
    tk.Button(window, text='退出',font=('wtf',20),width=5,height=1,command=exit).place(x=240, y=150)
def mian():#主页
    #time.sleep(5)
    window=tk.Tk()
    window.title('抽卡模拟器')
    window.geometry('400x250')#窗口
    tip=random.choice(tips)
    tk.Label(window,text=tip,font=('wtf',15)).place(x=0,y=220)
    tk.Label(window,text='Welcome use',font=('wtf',30),width=20, height=3).place(x=-5,y=0)
    tk.Label(window,text='抽卡模拟器',font=('wtf',20),width=16, height=1).place(x=84,y=85)
    tk.Label(window,text='v1.1',font=('wtf',10),width=4, height=1).place(x=270,y=85)#版本号
    tk.Button(window, text='开始',font=('wtf',20),width=5,height=1,command=mian_choice).place(x=75, y=150)
    tk.Button(window, text='设置',font=('wtf',20),width=5,height=1,command=setr).place(x=157, y=150)
    tk.Button(window, text='退出',font=('wtf',20),width=5,height=1,command=exit).place(x=240, y=150)
    tk.Button(window, text='彩蛋',font=('wtf',10),width=4,height=1,command=egg).place(x=240, y=550)
    window.mainloop()
def xz():#后台
    global xz1
    xz1=input('>>')
def zbt():#启动装置   
    print('抽卡模拟器Pro')
    print('by NNzyo')
    print('当前版本:v1.1正式版')
    print('注意:抽卡概率不与游戏相关(我有时间再搞)')
    time.sleep(0.5)
    print('加载中...')
    time.sleep(2)
    print('加载成功(请勿关掉我)')
    print('抽卡记录:')
    mian()
zbt()

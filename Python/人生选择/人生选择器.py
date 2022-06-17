import time
import random
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y
ptsth=['奖励自己','做作业','打电动','睡觉','写代码','看书']#事情
gasth=['minecraft','terraria','genshin']
zdysth=['语文','数学','英语','物理','政治','生物','地理','历史']
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
window=tk.Tk()
window.title('人生选择器')
window.geometry('300x200')#窗口
def zc_choice():
    choice0=random.choice(ptsth)
    tk.Label(window,text='                            ',font=('wtf',15)).place(x=160,y=82)
    tk.Label(window,text=choice0,font=('wtf',20)).place(x=160,y=80)
def game_choice():
    choice0=random.choice(gasth)
    tk.Label(window,text='                            ',font=('wtf',15)).place(x=160,y=82)
    tk.Label(window,text=choice0,font=('wtf',20)).place(x=160,y=80)
def zdy_choice():
    choice0=random.choice(zdysth)
    tk.Label(window,text='                            ',font=('wtf',15)).place(x=160,y=82)
    tk.Label(window,text=choice0,font=('wtf',20)).place(x=160,y=80)
tk.Label(window,text='日常:',font=('wtf',12)).place(x=55,y=15)
tk.Button(window,text='选择',font=('wtf',12),width=5,height=1,command= zc_choice).place(x=50, y=40)
tk.Label(window,text='游戏:',font=('wtf',12)).place(x=55,y=70)
tk.Button(window,text='选择',font=('wtf',12),width=5,height=1,command= game_choice).place(x=50, y=95)
tk.Label(window,text='复习科:',font=('wtf',12)).place(x=47,y=125)
tk.Button(window,text='选择',font=('wtf',12),width=5,height=1,command= zdy_choice).place(x=50, y=150)
tk.Label(window,text=xiex2,font=('wtf',12)).place(x=140,y=-5)
tk.Label(window,text='结果',font=('wtf',20)).place(x=190,y=0)
tk.Label(window,text='v1.0').place(x=0,y=180)

window.mainloop()
#所有权归CN_NZ所有

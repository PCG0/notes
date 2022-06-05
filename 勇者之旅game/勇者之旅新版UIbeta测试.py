import time
import random
import tkinter
import tkinter as tk
import tkinter.messagebox
import pickle
from main_jm_cn import Logo_cn
from sys import exit
from random import choices, randint
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y
from tkinter import *
from tool import xiex2
from PIL import Image, ImageTk
from random import *
from tkinter.ttk import Treeview


def main_qdqjm():
    qdq = tk.Tk()
    qdq.title('Hello  勇者の旅! Beta v3.5.2')
    qdq.geometry('789x458')
    qdq.resizable(width=False, height=False)
    tk.Label(qdq,text='|勇者の旅|',font=('wtf',50)).place(x=180, y=0)
    tk.Label(qdq,text='Journey of the Brave',font=('wtf',20)).place(x=205, y=70)
    tk.Label(qdq,text=xiex2,font=('wtf',13),width=0,height=30).place(x=184, y=-5)
    def help_us():
        help=tk.Tk()
        help.title('关于我们')
        help.geometry('470x250')
        def help_us_dq():
            help=tk.Tk()
            help.title('给点吃的')
            help.geometry('400x250')
            tk.Label(help,text='求求了,给孩子一口饭吃吧!',font=('wtf',20)).place(x=40, y=100)
            tk.Button(help,text='wechat',font=('wtf',15),width=9,height=1,).place(x=50,y=200)
            tk.Button(help,text='zfb',font=('wtf',15),width=9,height=1,).place(x=250,y=200)
        tk.Label(help,text='作者:NNzyo(tg:NNzyo)',font=('wtf',20)).place(x=10,y=10)
        tk.Label(help,text='剧情:Rrction(tg:Rrction)',font=('wtf',20)).place(x=10,y=40)
        tk.Label(help,text='质监:Meng_yan332(tg:Meng_yan332)',font=('wtf',20)).place(x=10,y=70)
        tk.Button(help,text='给点吃的',font=('wtf',20),width=9,height=1,command=help_us_dq).place(x=10,y=150)
    #def qdq_game_language():
    #    time.sleep(1)
    #    language=tk.Tk()
    #    language.title('language语言')
    #    language.geometry('400x250')
    #    tk.Label(language,text='|choice language|',font=('wtf',30)).place(x=29, y=10)
    #    def qdq_game_language_CN():
    #        language.destroy()
    #        qdq.destroy()
    #        Logo_cn()
    #    tk.Button(language,text='|     CN     |',font=('wtf',20),width=13,height=1,command=qdq_game_language_CN).place(x=105,y=90)
    #    def qdq_game_language_EN():
    #        language.destroy()
    #        qdq.destroy()
    #        main_qdqjm()
    #    tk.Button(language,text='|     EN     |',font=('wtf',20),width=13,height=1,command=qdq_game_language_EN).place(x=105,y=140)
    tk.Button(qdq,text='|  启动游戏  |',font=('wtf',20),width=13,height=1,command=Logo_cn).place(x=560,y=399)
    tk.Button(qdq, text='۩', font=('wtf', 20),width=1, height=1).place(x=753, y=399)
    tk.Button(qdq, text='۞ 设置',font=('wtf',15),width=18,height=1).place(x=0,y=370)
    tk.Button(qdq, text='⇌ 联机',font=('wtf',15),width=18,height=1).place(x=0,y=335)
    tk.Button(qdq, text='⇩ 下载',font=('wtf',15),width=18,height=1).place(x=0,y=250)
    tk.Button(qdq, text='≡ 菜单',font=('wtf',15),width=18,height=1).place(x=0,y=215)
    tk.Button(qdq, text='♈ 版本',font=('wtf',15),width=18,height=1).place(x=0,y=180)
    tk.Button(qdq, text='☃ 账号',font=('wtf',15),width=18,height=1).place(x=0,y=80)
    qdq.mainloop()
main_qdqjm()

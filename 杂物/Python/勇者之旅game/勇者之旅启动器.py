from pydoc import plain
import time
import random
import sys
import tkinter.messagebox
from main_jm_cn import main_game_jm
from tool import xiex2
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter.constants import COMMAND, W, X, Y

def main_qdqjm():
    qdq=tk.Tk()
    qdq.title('勇者之旅')
    qdq.geometry('700x500')
    tk.Label(qdq,text='|勇者の旅|',font=('wtf',50)).place(x=265, y=50)
    tk.Label(qdq,text='告知:本游戏还是半成品测试中,并不代表最终效果!',font=('wtf',16)).place(x=190,y=240)
    tk.Label(qdq,text='Journey of the Brave',font=('wtf',20)).place(x=290, y=120)
    tk.Label(qdq,text='| 公告栏 |',font=('wtf',23),width=0,height=10).place(x=4,y=-120)
    tk.Label(qdq,text=xiex2,font=('wtf',8),width=0,height=50).place(x=165, y=-5)
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
        tk.Label(help,text='程序/主创:NNzyo\n(tg:NNzyo)',font=('wtf',20)).place(x=10,y=10)
        tk.Label(help,text='剧情/指导:Rrction\n(tg:Rrction)',font=('wtf',20)).place(x=10,y=70)
        tk.Label(help,text='质监/UI:Meng_yan332\n(tg:Meng_yan332)',font=('wtf',20)).place(x=10,y=130)
        tk.Button(help,text='给点吃的',font=('wtf',20),width=9,height=1,command=help_us_dq).place(x=10,y=200)
    tk.Button(qdq,text='关于我们',font=('wtf',10),width=7,height=1,command=help_us).place(x=200,y=475)
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
    tk.Label(qdq,text='Launch the game',font=('wtf',15)).place(x=450, y=385)
    def gd_logo():
        time.sleep(0.5)
        tkinter.messagebox.showinfo(title='询问', message='由于本游戏是由Pygame写的,请务必前往pip下载,否则无法正常运行!')
        qdq.destroy()
        main_game_jm()
    tk.Button(qdq,text='|  启动游戏  |',font=('wtf',20),width=13,height=1,command=gd_logo).place(x=430,y=410)
    qdq.mainloop()
time.sleep(1)
main_qdqjm()
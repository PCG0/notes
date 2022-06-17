import time
import random
import sys
import tkinter.messagebox
#from main_game_qz_cn_Fa import quname
from random import choices,randint
from sys import exit
from main_jm_en_us import en_us
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, X, Y
#def main_game_cdjm():
#    cdjm=tk.Tk()
#    cdjm.title('选择存档')
    
def language():
    language=tk.Tk()
    language.title('语言选择/language')
    width = 789
    heigh = 458
    screenwidth = language.winfo_screenwidth()
    screenheight = language.winfo_screenheight()
    language.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    language.resizable(width=False, height=False)
    tk.Label(language,text='''|    请在选项中选取你要更改的语言    |
|Please choose the language you want to change in the options|''',font=('wtf',15)).place(x=0,y=0)
    def language_zh_cn():
        time.sleep(1)
        tkinter.messagebox.showwarning(title='注意!!!',message='中英翻译并不一定100%包准')
        language.destroy()
        zh_cn()
    def language_en_us():
        time.sleep(1)
        tkinter.messagebox.showwarning(title='note!!!',message='Chinese-English translations are not necessarily 100% standard')
        language.destroy()
        en_us()
    tk.Button(language,text='简体中文(中国)',font=('wtf',15),width=15,height=1,command=language_zh_cn).place(x=0,y=100)
    tk.Button(language,text='English(US)',font=('wtf',15),width=15,height=1,command=language_en_us).place(x=0,y=150)


def zh_cn():
    time.sleep(1)
    jm=tk.Tk()
    jm.title('勇者の旅')
    width = 800
    heigh = 480
    screenwidth = jm.winfo_screenwidth()
    screenheight = jm.winfo_screenheight()
    jm.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    tk.Label(jm,text='|勇者の旅|',font=('wtf',40)).place(x=265, y=10)
    def main_game_open():
        time.sleep(0.5)
        #quname禁用时把井号删掉,quname启用时把井号加上
        tkinter.messagebox.showwarning(title='游戏公告:',message='''质监的话:
作者跑路了,对此我感到抱歉,所以敬请期待下次更新吧''')
        tk.Label(jm,text='         ',font=('wtf',1000)).place(x=0,y=0)
        jm.title('勇者の旅')
        time.sleep(3)
        jm.destroy()
        #quname()
    tk.Button(jm,text='|  开始游戏  |',font=('wtf',20),width=13,height=1,command=main_game_open).place(x=305,y=80)
    tk.Button(jm,text='|  游戏设置  |',font=('wtf',20),width=13,height=1).place(x=305,y=130)
    tk.Button(jm,text='|  退出游戏  |',font=('wtf',20),width=13,height=1,command=exit).place(x=305,y=180)
    def main_game_jm_language():
        tkinter.messagebox.showwarning(title='警告', message='此功能还在测试中!')
        jm.destroy()
        language()
    tk.Button(jm,text='文',font=('wtf',20),width=3,height=1,command=main_game_jm_language).place(x=250,y=180)
    tk.Label(jm,text='♜NHG beta                  20220105145',font=('wtf',15)).place(x=0,y=456)
    jm.mainloop()
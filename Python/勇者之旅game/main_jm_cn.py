import time
import random
import sys
import tkinter.messagebox
#from main_game_qz_cn_Fa import quname
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, X, Y






#def main_game_cdjm():
#    cdjm=tk.Tk()
#    cdjm.title('选择存档')

    

    
def main_game_jm():
    time.sleep(3)
    jm=tk.Tk()
    jm.title('勇者の旅')
    jm.geometry('400x250')#窗口
    tk.Label(jm,text='|勇者の旅|',font=('wtf',40)).place(x=65, y=10)
    def main_game_open():
        #tk.Label(jm,text='         ',font=('wtf',1000)).place(x=0,y=0)
        #jm.title('勇者の旅')
        time.sleep(3)
        jm.destroy()
        #quname()
    tk.Button(jm,text='|  开始游戏  |',font=('wtf',20),width=13,height=1,command=main_game_open).place(x=105,y=80)
    tk.Button(jm,text='|  游戏设置  |',font=('wtf',20),width=13,height=1).place(x=105,y=130)
    def main_game_jm_exit():
        jm=tk.Tk()
        jm.title('退出')
        tk.Label(jm,text='|确定要退出吗?|',font=('wtf',17)).place(x=10, y=0)
        def main_game_jm_exit_no():
            jm.destroy()
        tk.Button(jm,text='|  否  |',font=('wtf',15),command=main_game_jm_exit_no).place(x=50,y=80)
        tk.Button(jm,text='|  是  |',font=('wtf',15),command=exit).place(x=50,y=130)
    tk.Button(jm,text='|  退出游戏  |',font=('wtf',20),width=13,height=1,command=main_game_jm_exit).place(x=105,y=180)
    def main_game_jm_language():
        tkinter.messagebox.showwarning(title='警告', message='此功能还在测试中!')
        language=tk.Tk()
        language.title('language语言 | beta')
        language.geometry('400x250')
        tk.Label(language,text='告知:中英翻译并不100%准确',font=('wtf',16)).place(x=50,y=100)
    tk.Button(jm,text='文',font=('wtf',15),width=3,height=1,command=main_game_jm_language).place(x=60,y=180)
    tk.Label(jm,text='♜NHG beta                  20220105145',font=('wtf',15)).place(x=0,y=226)
#def Logo_cn():#主页
#    time.sleep(2)
#    window=tk.Tk()
#    window.title('LOGO')
#    window.geometry('400x250')#窗口
#    def Logo_main_zy():
#        window.destroy()
#        main_game_jm()
#    tk.Button(window, text='                ',font=('wtf',20),width=100,height=100,command=Logo_main_zy).place(x=0, y=0)
#    tk.Label(window,text='|touch to start|',font=('wtf',25)).place(x=60, y=140)
#    tk.Label(window,text='♜奈何游戏',font=('wtf',45)).place(x=45, y=50)
#    tk.Label(window,text='NHG',font=('wtf',18)).place(x=0, y=222)
#    tk.Label(window,text='NHG GAME 2021-2022',font=('wtf',8)).place(x=40, y=224)
#    tk.Label(window,text='WWW.NHGAME.COM',font=('wtf',8)).place(x=40, y=236)
    jm.mainloop()








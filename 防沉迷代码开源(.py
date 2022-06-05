import time
import random
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y
#窗口版
def IE():#内置浏览器(
    time.sleep(3)
    window=tk.Tk()
    window.title('Internet Explorer')
    window.geometry('400x250')#窗口
    tk.Label(window,text='无法连接至服务器\n无网络连接',font=('wtf',30),width=20, height=3).place(x=-5,y=20)
    tk.Label(window,text='127.0.0.1',font=('wtf',15),width=50,height=1).place(x=-55,y=0)
def fcm18():#主体
    window=tk.Tk()
    window.title('防沉迷系统')
    window.geometry('400x250')#窗口
    tk.Label(window,text='v0.1',font=('wtf',10),width=4, height=1).place(x=310,y=85)#版本号
    tk.Label(window,text='防沉迷系统',font=('wtf',30),width=11, height=3).place(x=85,y=0)
    tk.Label(window,text='根据国家规定打造',font=('wtf',20),width=15, height=1).place(x=90,y=85)
    tk.Label(window,text='验证即自动同意',font=('wtf',10),width=16, height=1).place(x=90,y=115)
    def fcm18mian1():
        window=tk.Tk()
        window.title('防沉迷系统')
        window.geometry('400x250')#窗口
        def fcms():
            time.sleep(5)
            tk.Label(window,text='实名认证失败,请重试',font=('wtf',12),width=18, height=1).place(x=85,y=135)
        tk.Label(window, text='真实姓名: ',font=('wtf',15)).place(x=50, y=50)
        tk.Entry(window,font=('wtf',15)).place(x=150, y=53)
        tk.Label(window, text='身份证号: ',font=('wtf',15)).place(x=50, y=90)
        tk.Entry(window,font=('wtf',15)).place(x=150, y=93)
        tk.Button(window, text='验证',font=('wtf',20),width=5,height=1,command=fcms).place(x=240, y=130)
    tk.Button(window, text='《用户隐私保护》',font=('wtf',8),width=15,height=1,command=IE).place(x=195, y=115)
    tk.Button(window, text='开验',font=('wtf',20),width=5,height=1,command=fcm18mian1).place(x=75, y=150)
    tk.Button(window, text='试玩',font=('wtf',20),width=5,height=1,).place(x=157, y=150)
    tk.Button(window, text='退出',font=('wtf',20),width=5,height=1,command=exit).place(x=240, y=150)
    window.mainloop()
#指令窗版
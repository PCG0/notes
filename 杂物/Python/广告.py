import tkinter as tk
import time
xiex1='''———————————————————————————'''
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
xiex3='''——————————————————————————————————————————————————————'''
def IE():#内置浏览器(
    window=tk.Tk()
    window.title('Internet Explorer')
    window.geometry('400x250')#窗口
    tk.Label(window,text='无法连接至服务器\n无网络连接',font=('wtf',30),width=20, height=3).place(x=-5,y=20)
    tk.Label(window,text=xiex3,font=('wtf',15),width=50,height=1).place(x=0,y=15)
    tk.Label(window,text='┃www.Pixiv.net ★┃',font=('wtf',15),width=50,height=1).place(x=-50,y=0)
    tk.Label(window,text='← → × ♜',font=('wtf',15),width=10,height=1).place(x=5,y=0)
    tk.Label(window,text='•••',font=('wtf',15),width=5,height=1).place(x=350,y=1)
def dl():#广告
    window=tk.Tk()
    window.title('广告板')
    window.geometry('300x200')#窗口
    tk.Label(window,text=xiex2,font=('wtf',12)).place(x=140,y=-5)
    #框架
    tk.Label(window,text='PhigrOS极速版',font=('wtf',15)).place(x=5,y=0)
    tk.Label(window,text='玩游戏就能赚钱',font=('wtf',15)).place(x=0,y=25)
    tk.Label(window,text='每月破万不是梦',font=('wtf',15)).place(x=0,y=50)
    tk.Label(window,text='快点击下方下载',font=('wtf',15)).place(x=0,y=75)
    tk.Button(window, text='前往下载',font=('wtf',20),width=8,height=1,command=IE).place(x=13, y=120)
    tk.Label(window,text='注:只有在本广告下载才有效',font=('wtf',10)).place(x=0,y=180)
    #一号位
    tk.Label(window,text='广告\nC位\n留给\n您！',font=('wtf',20)).place(x=190,y=25)
    tk.Label(window,text='电话:19865520887',font=('wtf',12)).place(x=155,y=140)
    #二号位
    window.mainloop()
dl()
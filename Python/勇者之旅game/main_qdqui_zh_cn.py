from pydoc import plain
import time
import random
import sys
import tkinter.messagebox
from main_jm_zh_cn import zh_cn
from tool import xiex2
from tool import xiex1
from random import choices, randint
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter.constants import COMMAND, W, X, Y



def note():
    time.sleep(1.0)
    tkinter.messagebox.showwarning(title='抱歉:',message='该功能测试中!!!')

def help_us():
    help=tk.Tk()
    help.title('关于我们')
    width = 789
    heigh = 458
    screenwidth = help.winfo_screenwidth()
    screenheight = help.winfo_screenheight()
    help.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    help.resizable(width=False, height=False)
    def help_tc():
        help.destroy()
        sz()
    tk.Label(help,text='制作人员名单:',font=('wtf',15)).place(x=0,y=0)
    tk.Label(help,text='作者:NNzyo    (tg:NNzyo)  ',font=('wtf',15)).place(x=0,y=30)
    tk.Label(help,text='剧情:Rrction  (tg:Rrction)',font=('wtf',15)).place(x=0,y=60)
    tk.Label(help,text='质监:incubus  (tg:incubus)',font=('wtf',15)).place(x=0,y=90)
    tk.Button(help,text='返回',font=('wtf',10),width=15,height=1,command=help_tc).place(x=675,y=435)

def sz():
    sz = tk.Tk()
    sz.title('Hello 勇者! |设置车间| (该功能页面为测试版,请谨慎点击) Beta v0.1.9')
    width = 789
    heigh = 458
    screenwidth = sz.winfo_screenwidth()
    screenheight = sz.winfo_screenheight()
    sz.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    sz.resizable(width=False, height=False)
    tk.Label(sz,text='|这里是设置车间|',font=('wtf',10)).place(x=0,y=0)
    tk.Label(sz,text=xiex1,font=('wtf',13),width=0,height=0).place(x=-8, y=16)
    def zz():
        time.sleep(1.0)
        tkinter.messagebox.showwarning(title='抱歉:',message='你的网页创建失败,请重试!!!')
    def wm():
        sz.destroy()
        help_us()
    def tc():
        sz.destroy()
        main_qdqjm()
    tk.Button(sz,text='关于我们',font=('wtf',10),width=7,height=1,command=wm).place(x=0,y=35)
    tk.Button(sz,text='赞助',font=('wtf',10),width=7,height=1,command=zz).place(x=0,y=65)
    tk.Button(sz,text='返回',font=('wtf',10),width=15,height=1,command=tc).place(x=675,y=435)

def main_qdqjm():
    qdq = tk.Tk()
    qdq.title('Hello 勇者! Beta v3.5.2')
    width = 789
    heigh = 458
    screenwidth = qdq.winfo_screenwidth()
    screenheight = qdq.winfo_screenheight()
    qdq.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    qdq.resizable(width=False, height=False)
    tk.Label(qdq, text='|勇者の旅|', font=('wtf', 50)).place(x=180, y=0)
    tk.Label(qdq,text='Journey of the Brave',font=('wtf',20)).place(x=205, y=70)
    tk.Label(qdq,text=xiex2,font=('wtf',13),width=0,height=30).place(x=184, y=-5)
    def gd_logo():
        time.sleep(0.5)
        tkinter.messagebox.showwarning(title='警告!!!', message='请确定你的Python装有Pygame，否则可能无法运行')
        qdq.destroy()
        zh_cn()
    def sz_logo():
        time.sleep(0.5)
        tkinter.messagebox.showwarning(title='注意:',message='该功能页面为测试版,请勿随意点击')
        qdq.destroy()
        sz()
    tk.Button(qdq,text='|  启动游戏  |',font=('wtf',20),width=13,height=1,command=gd_logo).place(x=560,y=399)
    tk.Button(qdq,text='↑', font=('wtf', 20),width=1, height=1).place(x=753, y=399)
    tk.Button(qdq,text='۞ 设置',font=('wtf',15),borderwidth = 0,width=18,height=1,command=sz_logo).place(x=-45,y=370)
    tk.Button(qdq,text='⇌ 联机',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-45,y=335)
    tk.Button(qdq,text='☏ 通知',font=('wtf', 15),borderwidth = 0, width=18, height=1,command=note).place(x=-45, y=250)
    tk.Button(qdq,text='≡ 菜单',font=('wtf', 15),borderwidth = 0,width=18, height=1,command=note).place(x=-45, y=215)
    tk.Button(qdq,text='♈ 版本',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-45,y=180)
    tk.Button(qdq,text='☃ 账号',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-45,y=80)
    tk.Label(qdq,text='账户',font=('wtf',15)).place(x=0,y=45)
    tk.Label(qdq,text='游戏',font=('wtf',15)).place(x=0,y=145)
    tk.Label(qdq,text='通用',font=('wtf',15)).place(x=0,y=300)
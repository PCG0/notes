from pydoc import plain
import time
import random
import sys
import tkinter.messagebox
from main_qdqui_zh_cn import main_qdqjm
from tool import xiex2
from tool import xiex1
from random import choices, randint
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter.constants import COMMAND, W, X, Y


def note():
    time.sleep(1.0)
    tkinter.messagebox.showwarning(title='sorry:',message='The functional test is pending!!!')

def help_us():
    help=tk.Tk()
    help.title('About us')
    width = 789
    heigh = 458
    screenwidth = help.winfo_screenwidth()
    screenheight = help.winfo_screenheight()
    help.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    help.resizable(width=False, height=False)
    def help_tc():
        help.destroy()
        sz()
    tk.Label(help,text='List of producers:',font=('wtf',15)).place(x=0,y=0)
    tk.Label(help,text='author:NNzyo    (tg:NNzyo)  ',font=('wtf',15)).place(x=0,y=30)
    tk.Label(help,text='plot:Rrction  (tg:Rrction)',font=('wtf',15)).place(x=0,y=60)
    tk.Label(help,text='Quality supervision:incubus  (tg:incubus)',font=('wtf',15)).place(x=0,y=90)
    tk.Button(help,text='return',font=('wtf',10),width=15,height=1,command=help_tc).place(x=675,y=435)

def sz():
    sz = tk.Tk()
    sz.title('Hello Daredevil! set up the workshop | | (This feature page is beta, please click carefully) Beta v0.1.9')
    width = 789
    heigh = 458
    screenwidth = sz.winfo_screenwidth()
    screenheight = sz.winfo_screenheight()
    sz.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    sz.resizable(width=False, height=False)
    tk.Label(sz,text='|Here is the set workshop|',font=('wtf',10)).place(x=0,y=0)
    tk.Label(sz,text=xiex1,font=('wtf',13),width=0,height=0).place(x=-8, y=16)
    def zz():
        time.sleep(1.0)
        tkinter.messagebox.showwarning(title='sorry:',message='Your page creation failed, please try again!!!')
    def wm():
        sz.destroy()
        help_us()
    def tc():
        sz.destroy()
        main_qdqjm1()
    tk.Button(sz,text='About us',font=('wtf',10),width=7,height=1,command=wm).place(x=0,y=35)
    tk.Button(sz,text='sponsor ',font=('wtf',10),width=7,height=1,command=zz).place(x=0,y=65)
    tk.Button(sz,text='return',font=('wtf',10),width=15,height=1,command=tc).place(x=675,y=435)

def main_qdqjm1():
    qdq1 = tk.Tk()
    qdq1.title('Hello Daredevil! Beta v3.5.2')
    width = 789
    heigh = 458
    screenwidth = qdq1.winfo_screenwidth()
    screenheight = qdq1.winfo_screenheight()
    qdq1.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    qdq1.resizable(width=False, height=False)
    tk.Label(qdq1, text='| Heros Journey|', font=('wtf', 50)).place(x=180, y=0)
    tk.Label(qdq1,text='Journey of the Brave',font=('wtf',20)).place(x=305, y=70)
    tk.Label(qdq1,text=xiex2,font=('wtf',13),width=0,height=30).place(x=184, y=-5)
    def gd_logo():
        time.sleep(0.5)
        tkinter.messagebox.showwarning(title='Sorry', message='Sorry, your language version is not yet developed, and you are switching to the full Chinese version for you to play')
        qdq1.destroy()
        main_qdqjm()
    def sz_logo():
        time.sleep(0.5)
        tkinter.messagebox.showwarning(title='note:',message='This feature page is beta, please do not click at will')
        qdq1.destroy()
        sz()
    tk.Button(qdq1,text='|  Start  |',font=('wtf',20),width=13,height=1,command=gd_logo).place(x=560,y=399)
    tk.Button(qdq1,text='↑', font=('wtf', 20),width=1, height=1).place(x=753, y=399)
    tk.Button(qdq1,text='۞ Set up ',font=('wtf',15),borderwidth = 0,width=18,height=1,command=sz_logo).place(x=-40,y=370)
    tk.Button(qdq1,text='⇌ Online ',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-40,y=335)
    tk.Button(qdq1,text='☏ notice ',font=('wtf', 15),borderwidth = 0, width=18, height=1,command=note).place(x=-40, y=250)
    tk.Button(qdq1,text='≡ menu   ',font=('wtf', 15),borderwidth = 0,width=18, height=1,command=note).place(x=-40, y=215)
    tk.Button(qdq1,text='♈ version',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-40,y=180)
    tk.Button(qdq1,text='☃ Account',font=('wtf',15),borderwidth = 0,width=18,height=1,command=note).place(x=-40,y=80)
    tk.Label(qdq1,text='account',font=('wtf',15)).place(x=0,y=45)
    tk.Label(qdq1,text='game',font=('wtf',15)).place(x=0,y=145)
    tk.Label(qdq1,text='general',font=('wtf',15)).place(x=0,y=300)
import sys
import time
import random
import tkinter as tk
import tkinter.messagebox
from sys import exit
from tkinter import *
from tool import xiex2
from tool import xiex1
from pydoc import plain
from main_jm_zh_cn import zh_cn
from main_jm_en_us import en_us
from tkinter import Place, font
from random import choices, randint
from tkinter.constants import COMMAND, W, X, Y




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
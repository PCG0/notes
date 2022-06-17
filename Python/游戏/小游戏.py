import time
import random
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y
def main():#主页
    main=tk.Tk()
    main.title('拾荒模拟器')
    main.geometry('800x480')
    


def Logo():#主页
    Logo=tk.Tk()
    Logo.title('LOGO')
    Logo.geometry('400x250')#窗口
    tk.Label(Logo,text='♜奈何娱乐',font=('wtf',45)).place(x=45, y=50)
    tk.Button(Logo, text='touch to start',font=('wtf',20),width=15,height=1,command=main).place(x=90, y=150)
    tk.Label(Logo,text='NHG',font=('wtf',18)).place(x=0, y=222)
    tk.Label(Logo,text='NHG GAME 2021-2022',font=('wtf',8)).place(x=40, y=224)
    tk.Label(Logo,text='WWW.NHGAME.COM',font=('wtf',8)).place(x=40, y=236)
    Logo.mainloop()
Logo()
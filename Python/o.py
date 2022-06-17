from distutils import command
import time
import random
import sys
import tkinter.messagebox
from turtle import width
from tool import xiex2
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import *
from tkinter.constants import COMMAND, W, X, Y

qqq=0


while True:
    jm=tk.Tk()
    jm.title('QQQ测试器')
    jm.geometry('700x500')
    tk.Label(jm,text='QQQ测试器',font=('wtf',50)).place(x=30, y=20)
    tk.Label(jm,text=xiex2,font=('wtf',50)).place(x=350, y=0)
    tk.Label(jm,text=qqq,font=('wtf',40)).place(x=160, y=240)
    def ja():
        def nz():
            global qqq
            if qqq < 1:
                qqq=qqq-1
                tk.Label(jm,text='   ',font=('wtf',40)).place(x=160, y=240)
                tk.Label(jm,text=qqq,font=('wtf',40)).place(x=160, y=240)
        global qqq
        qqq=qqq+1
        tk.Label(jm,text='   ',font=('wtf',40)).place(x=160, y=240)
        tk.Label(jm,text=qqq,font=('wtf',40)).place(x=160, y=240)
        nz()
    tk.Button(jm,text='F**K ME',font=('wtf',15),width=30,height=10,command=ja).place(x=380, y=150)
    jm.mainloop()
    
    
    
    




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
name='Resu'
jm_set=tk.Tk()
jm_set.title('答题系统 | User:'+name)
jm_set.geometry('800x700')
tk.Label(jm_set,text=('欢迎您'),font=('wtf',32)).place(x=150, y=37)
tk.Label(jm_set,text=(name),font=('wtf',32)).place(x=155, y=83)
tk.Label(jm_set,text=('|答题系统|'),font=('wtf',55)).place(x=350, y=45)
tk.Label(jm_set,text=('|选择你所在的年级|'),font=('wtf',40)).place(x=160,y=180)
tk.Button(jm_set,text=('☻'),font=('wtf',40),width=3,height=1).place(x=60, y=40)
jm_set.mainloop()
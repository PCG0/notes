import time
import random
import pickle
import tkinter.messagebox
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter.constants import COMMAND, Y
from tkinter.ttk import Button



dl_jm_ks=tk.Tk()
dl_jm_ks.title('TQW')
dl_jm_ks.geometry('300x400')
tk.Label(dl_jm_ks,text='✈',font=('wtf',90)).place(x=85,y=50)
tk.Button(dl_jm_ks,text='登录',font=('wtf',20),width=10,height=1).place(x=85,y=100)
tk.Button(dl_jm_ks,text='注册',font=('wtf',20),width=10,height=1).place(x=85,y=100)
dl_jm_ks.mainloop()


from asyncio.windows_events import NULL
from asyncore import read
from signal import set_wakeup_fd
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter.ttk import Separator
import random
from time import sleep as s
import mmap
def Pass():
    pass
window = tk.Tk()

#try:
#    with open("Us//user.txt","r+",encoding='utf8') as file:
#        #total_lines = sum(1 for line in file)
#        users = file.readlines()
#        mm = mmap.mmap(file.fileno(), 0)
#        total_lines = 0
#        while mm.readline():
#            total_lines += 1
#except:
#    users = NULL
#    with open("Us//user.txt", "w",encoding='utf8') as file:
#        file.write(str(users))

with open("Us//user.txt","r+",encoding='utf8') as file:
    users = file.readlines()
    mm = mmap.mmap(file.fileno(), 0)
    total_lines = 0
    while mm.readline():
        total_lines += 1
file.close()

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
|
|
|
|
|
|
|
|
'''
xiex3='''_________'''

opened = False

def settings():
    setw = tk.Tk()
    setw.title('应用设置')
    setw.geometry('400x400')#窗口
    setw.resizable(0,0)
def About():
    ab = tk.Tk()
    ab.title('关于')
    ab.geometry('400x400')#窗口
    '''sda = scrolledtext.ScrolledText(ab,width=400,height=400,font=('宋体',15))
    sda.place(x=1,y=1)
    f = open('about.txt','r')
    s = f.read()
    sda.insert(END,s)
    ab.mainloop()'''
    tk.Label(ab,text='Hi',font=('wtf',40)).place(x=50,y=50)
    tk.Label(ab,text='这里空空如也',font=('wtf',15)).place(x=50,y=100)
def fls():
    window.attributes('-fullscreen',True)



Main_List_1 = Button(window,width=7,text='应用设置',command=settings)
Main_List_2 = Button(window,width=7,text='',command=settings)
Main_List_3 = Button(window,width=7,text='',command=settings)
Main_List_4 = Button(window,width=7,text='',command=settings)
wg = Label(window,text=xiex3,font=('wtf',12))
about = Button(window,width=5,text='关于',command=About)
#change_new = Button(window,width=7,text='新建联系人',command=About)
fullsc = Button(window,width=5,text='全屏',command=fls)

def Main_List():
    global opened,Main_List_1
    
    if opened:
        Main_List_1.place_forget()
        Main_List_2.place_forget()
        wg.place(x=0,y=30)
        about.place(x=10,y=50)
        opened = False
    else:
        wg.place_forget()
        about.place_forget()
        Main_List_1.place(x=1,y=40)
        Main_List_2.place(x=1,y=70)
        opened = True


def Window_Main():
    global window,sep
    window.title(random.choice(['Welcom']))
    window.geometry('800x500')#窗口
    window.resizable(0,0)

    Photo_Main_List = PhotoImage(file=r'.\\Us\\Photos\\List.png')
    Photo_Main_List_Image = Photo_Main_List.subsample(1,1)
    Button(window,width=2,command=Main_List,image=Photo_Main_List_Image,compound=LEFT).place(x=2, y=1)#三条杠
    #Button(window,width=2,command=Main_List).place(x=50, y=10)

    tk.Label(window,text=xiex2,font=('wtf',12)).place(x=59,y=-5)
    about.place(x=10,y=50)
    #change_new.place(x=0,y=50)
    wg.place(x=0,y=30)
    #fullsc.place(x=10,y=80)

    List = Listbox(window,font=('wtf',12),width=20,height=30)
    List.place(x=65,y=-1)
    
    uss = [item for item in users]
    for i in range(0,total_lines):
        List.insert(END,uss[i])


    window.mainloop()



Window_Main()

from turtle import title
import pygame
import time
import random
import sys
import tkinter.messagebox
from tool import tips
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, X, Y





def quname():
    main_game=tk.Tk()
    tip=random.choice(tips)
    main_game.title('勇者之旅 | '+tip)
    width = 500
    heigh = 300
    screenwidth = main_game.winfo_screenwidth()
    screenheight = main_game.winfo_screenheight()
    main_game.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    tk.Label(main_game,text='勇者啊 你叫什么名字？',font=('wtf',17)).place(x=130,y=110)
    def Save_name():
        time.sleep(1)
        def start__game():
            time.sleep(1)
            tk.Label(main_game,text='         ',font=('wtf',1000)).place(x=0,y=0)
            tk.Label(main_game,text='开什么玩笑 这不是你的名字。',font=('wtf',17)).place(x=90,y=110)
            def start_game():
                time.sleep(1)
                tk.Label(main_game,text='         ',font=('wtf',1000)).place(x=0,y=0)
                tk.Label(main_game,text='这  根  本  不  是  你  的  名  字。',font=('wtf',17)).place(x=45,y=110)
                def start_game_2():
                    main_game.destroy()
                    time.sleep(1)
                    import main_game_cn 
                tk.Button(main_game,text='|v|',font=('wtf',17),command=start_game_2).place(x=220,y=230)
            tk.Button(main_game,text='是!',font=('wtf',15),command=start_game).place(x=220,y=230)
        if name.get() == '':
            tkinter.messagebox.showerror(title='错误', message='错误! 名字不能为空!')
        elif name.get() == 'nike':
            tkinter.messagebox.showwarning(title='警告', message='警告! 不能用这名字!')
        else:
            npf = name.get()
            with open('sever.txt', "w") as file:
                file.write(npf)
            tk.Label(main_game,text='         ',font=('wtf',1000)).place(x=0,y=0)
            with open('sever.txt', 'r')as file:
                nnamme = file.readlines()
            tk.Label(main_game,text='勇者啊 你确定这是你的名字？',font=('wtf',17)).place(x=100,y=110)
            tk.Label(main_game,text=nnamme,font=('wtf',17)).place(x=100,y=140)
            tk.Button(main_game,text='是',font=('wtf',15),command=start__game).place(x=210,y=230)
            def gd_bu():
                main_game.destroy()
                quname()
            tk.Button(main_game,text='不',font=('wtf',15),command=gd_bu).place(x=250,y=230)
    name = tk.StringVar()
    tk.Entry(main_game, textvariable=name).place(x=175,y=150)
    tk.Button(main_game,text='确定',font=('wtf',15),command=Save_name).place(x=220,y=230)
    main_game.mainloop()
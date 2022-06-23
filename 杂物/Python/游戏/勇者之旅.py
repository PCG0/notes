import time
import random
import pygame
import sys
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, X, Y

from pygame import color


tips=['C--✘ Python✔','美好的一天~','一定要加油!','↑↓']

while True:
    def main_game_cdjm():
        cdjm=tk.Tk()
        cdjm.title('选择存档')
    def main_game_jm_language():
        language=tk.Tk()
        language.title('language语言')
        language.geometry('400x250')
        
    def main_game_jm():
        #time.sleep(3)
        jm=tk.Tk()
        jm.title('勇者の旅')
        jm.geometry('400x250')#窗口
        tk.Label(jm,text='|勇者の旅|',font=('wtf',40)).place(x=65, y=10)
        tk.Button(jm,text='|  开始游戏  |',font=('wtf',20),width=13,height=1,command=main_game_cdjm).place(x=105,y=80)
        tk.Button(jm,text='|  游戏设置  |',font=('wtf',20),width=13,height=1).place(x=105,y=130)
        tk.Button(jm,text='|  退出游戏  |',font=('wtf',20),width=13,height=1).place(x=105,y=180)
        tk.Button(jm,text='文',font=('wtf',15),width=3,height=1).place(x=60,y=180)
        tk.Label(jm,text='♜NHG beta0.1               20220105145',font=('wtf',15)).place(x=0,y=226)
    def Logo():#主页
        window=tk.Tk()
        window.title('LOGO')
        window.geometry('400x250')#窗口
        tk.Button(window, text='',font=('wtf',20),width=100,height=100,command=main_game_jm).place(x=0, y=0)
        tk.Button(window,text='更多信息',font=('wtf',10),width=7,height=1).place(x=300,y=227)
        tk.Label(window,text='|touch to start|',font=('wtf',25)).place(x=60, y=140)
        tk.Label(window,text='♜奈何娱乐',font=('wtf',45)).place(x=45, y=50)
        tk.Label(window,text='NHG',font=('wtf',18)).place(x=0, y=222)
        tk.Label(window,text='NHG GAME 2021-2022',font=('wtf',8)).place(x=40, y=224)
        tk.Label(window,text='WWW.NHGAME.COM',font=('wtf',8)).place(x=40, y=236)
        window.mainloop()
    Logo()



  

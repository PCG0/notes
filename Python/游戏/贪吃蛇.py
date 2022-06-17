import time
import random
import pygame
import sys
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, Y

from pygame.time import Clock
def main_game_jm():
    window=tk.Tk()
    window.title('贪吃の蛇')
    window.geometry('400x250')#窗口
    tk.Label(window,text='|贪吃の蛇|',font=('wtf',40)).place(x=65, y=20)
    tk.Label(window, text='关闭此窗口以开始',font=('wtf',20)).place(x=90, y=130)
    tk.Label(window,text='♜NHG GAME',font=('wtf',15)).place(x=0, y=226)
    window.mainloop()
main_game_jm()
pygame.init()
pygame.display.set_caption('贪吃蛇')
clock=pygame.time.Clock()
speed=60
width,height=640,480
screen=pygame.display.set_mode((width,height))
snake_color=255,255,255
snake_x,snake_y=1,0
snake_size=15
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen,snake_color,(snake_x,snake_y,snake_size,snake_size))
    pygame.display.flip()



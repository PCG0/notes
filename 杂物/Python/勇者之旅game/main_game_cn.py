import pygame
import time
import random
import sys
import tkinter.messagebox
import datetime
import sys
from typing import List
import pygame
from pygame.locals import *
from collections import deque
from tkinter import *
import tkinter as tk
from random import choice
from time import monotonic, sleep
import threading
import os
import ctypes
import inspect
from tool import tips
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter import Place, font
from tkinter.constants import COMMAND, W, X, Y


pygame.init()
FPS = 30
width,height = 900,600
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
tip=random.choice(tips)
pygame.display.set_caption('勇者之旅 | '+tip)


pyr = "*"
spe = 0.125
speed_kin = 0
speed = spe
keys = [
    False,False,False,False,False,False,False,False,False,False,
    False,False,False,False,False,False,False,False,False,False,
    ]
x = "P"#你
xp = 'M'#sb
HP_x = 10#生命值
HP_xp = 7#sb生命值


while True:
    

    #按键检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hand_1 = False
            box_kou_p = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
            if event.key == K_TAB:
                npc_root = True               
            if event.key == K_LSHIFT:
                speed = spe*2
            if event.key == K_z:
                keys[4] = True
            if event.key == K_p:
                keys[5] = True
            if event.key == K_j:
                keys[6] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False
            if event.key == K_TAB:
                npc_root = False
            if event.key == K_LSHIFT:
                speed_kin = 0
                speed = spe
    if playerpos0 >= width:
        playerpos0 = width - (width - width + 2)
    elif playerpos0 <= 0:
        playerpos0 = 0
    if playerpos1 >= height:
        playerpos1 = height - (height - height + 2)
    elif playerpos1 <= 0:
        playerpos1 = 0
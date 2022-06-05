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
#import numpy as np

desktop_path = './FandP/'
file_name = 'save.faps'
log_name = 'log.txt'
chapter_1_name = 'Chapter 1'
def Save_player():#存档保存
    with open(desktop_path+file_name, "w") as file:
        file.write(
            str(playerpos0)+"\n"+#玩家的x轴坐标
            str(playerpos1)+"\n"+#玩家的y轴坐标
            #str(day)+"\n"+#存活天数（days）
            str(time)+"\n"+#当前时间（times）
            str(hand_1)+"\n"+
            str(box_kou_p)+"\n"+
            str(box_kou_size_1)+"\n"+
            str(box_kou_size_2)+"\n"+
            str(box_kou_size_3)+"\n"+
            str(box_kou_size_4)+"\n"
        )
        file.close()
def Load_player():#存档加载
    global playerpos1,playerpos0,day,time,zip_beta,p,box_kou_size_1,box_kou_size_2,hand_1,box_kou_size_3,box_kou_size_4,box_kou_p
    try:
        with open(desktop_path+file_name,"r") as file:
            sl = file.readlines()
            playerpos0 = int(float(sl[0].strip('\n')))
            playerpos1 = int(float(sl[1].strip('\n')))
            day = int(float(sl[2].strip('\n')))
            time = int(float(sl[3].strip('\n')))
            hand_1 = sl[4].strip('\n')
            box_kou_p = sl[5].strip('\n')
            box_kou_size_1 = int(float(sl[6].strip('\n')))
            box_kou_size_2 = int(float(sl[7].strip('\n')))
            box_kou_size_3 = int(float(sl[8].strip('\n')))
            box_kou_size_4 = int(float(sl[9].strip('\n')))
            file.close()
    except:#没有存档则创建存档并写入初始数据
        playerpos0,playerpos1,day,time = 100,40,0,8
        box_kou_size_1,box_kou_size_2,box_kou_size_3,box_kou_size_4 = 50,50,100,100
        p = False
        box_kou_p = False
        #Save_player()
        with open(desktop_path+log_name, "w") as file:
            file.write(log)
        #os.mkdir(desktop_path + 'Chapter 1')

#更新日志
log = '''
v1.0.2
时间；自动保存；
v1.0.3
拾取物品系统优化；自动保存间隔 15 -> 10；
'''

class NpcWork():
    def cooking():
        box = pygame.image.load('./FandP/aove.png').convert()

#多线程
class SaveTime(threading.Thread):#自动保存
    def run(self):
        while True:
            sleep(10)
            #Save_player()
class TimeThread(threading.Thread):#时间流逝
    def run(self):
        global time,day
        while True:
            sleep(S)
            time += 1
            if time >= 24:
                #day += 1
                time = 0
class boxKou(threading.Thread):
    def run(self):
        global box_kou_size_1,box_kou_size_2,hand_1
        hand_1 = box_kou
        while True:
            if not box_kou_p:
                break
            box_kou_size_1,box_kou_size_2 = playerpos0 - 1,playerpos1
            sleep(0.001)
class boxKou_2(threading.Thread):
    def run(self):
        global box_kou_size_3,box_kou_size_4,hand_1
        hand_1 = box_kou_2
        while True:
            if not box_kou_p:
                break
            box_kou_size_3,box_kou_size_4 = playerpos0 - 1,playerpos1
            sleep(0.001)
class TimeLoader(threading.Thread):
    def run(self):
        pass

class Desk_1(threading.Thread):
    def run(self):
        while True:
            pass

pygame.init()
FPS = 30
width,height = 900,600
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
title = [' ','  ~  今天也是好天气']
pygame.display.set_caption("F和P的苹果园" + choice(title))
clock = pygame.time.Clock()

#list_deque = deque([], 10)
#list_deque.append(" ")

pyr = "*"
spe = 0.125
speed_kin = 0
speed = spe
keys = [
    False,False,False,False,False,False,False,False,False,False,
    False,False,False,False,False,False,False,False,False,False,
    ]
#npc1pos = [69.625, 195.75]


myfont = pygame.font.Font(None,20)
npc1 = pygame.font.Font(None,20)
list_money = pygame.font.Font(None,20)
list_deque_font = pygame.font.Font(None,25)
s_b = pygame.font.Font(None,15)
Day_f = pygame.font.Font(None,15)
time_down_s = pygame.font.Font(None,15)
box_Box_site = pygame.font.Font(None,15)
desk_Box_site = pygame.font.Font(None,30)
white = 255,255,255

all_sprites = pygame.sprite.Group()


box_kou = "#"
box_kou_2 = "&"
box_kou_size_1,box_kou_size_2 = 50,50
box_kou_size_3,box_kou_size_4 = 50,50

desk = "O"
box_kou_size_5,box_kou_size_6 = 50,50



#数值设定区
x = "@"#你
#image = pygame.image.load('D:\\SetPython\\FandP\\aove.png').convert()
john = "John"
con = 0#整点重置
S = 120#对应44行，一时的流逝速度
HP_Life = 10#生命值
#x = playerpos + keys[3] - keys[0]
shift_time = 5
#print(starttime.second)
datetime_return = 0
zip_beta = 1.0
npc_root = False
foll_list = "无"
a = [foll_list,"当前任务清单：\n"]
Det = False
Lit = ["任务清单"]
Lit_roll_list = ["制作草莓蛋糕", "制作蓝莓鸡尾酒", "a", "b", "c", "d", "e"]
#Lit.insert(0,Lit_roll)
running = True

boxKou.daemon = True

o = 13#判定范围

#线程启动及循环主题
#TimeThread.daemon = True
#Load_player()#载入存档
TimeThread().start()
SaveTime().start()
#make_zip()
box_kou_p = False
while running:
    #print(playerpos0,playerpos1)

    starttime = datetime.datetime.now().second
    stime = str(starttime)
    int_stime = int(float(starttime))
    #ddd = "Days:{0}".format(day)+"    Time:{0}".format(time)
    #clock.tick(FPS)
    #print(playerpos)
    Lit_roll = choice(Lit_roll_list)
    all_sprites.update()
    desk_box_2 = desk_Box_site.render(desk,True,white)
    textImage = myfont.render(x, True, white)
    Npc1 = npc1.render(john,True,white)
    #day_image = Day_f.render(ddd,True,white)
    box_box = box_Box_site.render(box_kou,True,white)
    box_box_2 = box_Box_site.render(box_kou_2,True,white)
    
    #screen.blit(image,(0,0))
    screen.fill(0)
    screen.blit(desk_box_2,(box_kou_size_5,box_kou_size_6))
    #screen.blit(textImage,(playerpos0,playerpos1))
    #screen.blit(day_image,(0,0))
    screen.blit(box_box,(box_kou_size_1,box_kou_size_2))
    screen.blit(box_box_2,(box_kou_size_3,box_kou_size_4))
    
    #screen.blit(Npc1,npc1pos)
    all_sprites.draw(screen)
    pygame.display.flip()


    #按键检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hand_1 = False
            box_kou_p = False
            #Save_player()
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
        

    #控制反馈
    if keys[0]:
        playerpos1 -= speed
    elif keys[2]:
        playerpos1 += speed
    elif keys[4]:
        if event.type == pygame.KEYUP:
            if event.key == K_z:
                keys[4] = False
                #day += 1
                time = 7
                #Save_player()
    elif keys[6]:
        if event.type == pygame.KEYUP:
            if event.key == K_j:
                
                if (box_kou_size_1 + o) > playerpos0 > (box_kou_size_1 - o) and (box_kou_size_2 + o) > playerpos1 > (box_kou_size_2 - o):
                    box_kou_p = True
                    boxKou().start()
                elif (box_kou_size_3 + o) > playerpos0 > (box_kou_size_3 - o) and (box_kou_size_4 + o) > playerpos1 > (box_kou_size_4 - o):
                    boxKou_2().start()
                    box_kou_p = True
                keys[6] = False
                #Save_player()
        elif box_kou_p:
            box_kou_p = False
            keys[6] = False
            hand_1 = False
            #Save_player()

    if keys[1]:
        playerpos0 -= speed
    elif keys[3]:
        playerpos0 += speed
    elif keys[5]:
        if event.type == pygame.KEYUP:
            if event.key == K_p:
                p = True
                #Save_player()
                keys[5] = False
        elif p:
            p = False
            keys[5] = False
            #Save_player()
    if (box_kou_size_5 + o) > playerpos0 > (box_kou_size_5 - o) and (box_kou_size_6 + o) > playerpos1 > (box_kou_size_6 - o):
        p = False
        if not p:
            pass
        else:
            print('true')

    

    #防止玩家溢出边缘
    if playerpos0 >= width:
        playerpos0 = width - (width - width + 2)  
    elif playerpos0 <= 0:
        playerpos0 = 0
    if playerpos1 >= height:
        playerpos1 = height - (height - height + 2)
    elif playerpos1 <= 0:
        playerpos1 = 0

    
    

    
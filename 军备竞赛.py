import time
import random
from random import choices,randint
from sys import exit
zbt='''
  军备竞赛
 go  开始游戏
help 玩法介绍
'''
print(zbt)
while True:
    def xzxs():
        global xz
        xz = input('>>')
    xzxs()
    def jzbt():
        print('加载中.')
        time.sleep(1)
        print('加载中..')
        time.sleep(1)
        print('加载中...')
        time.sleep(1)


    if xz == 'go':
        jzbt()
    elif xz == 'help':
        pass

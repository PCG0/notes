import time
import random
from random import choices,randint
from sys import exit

zbt='''
  人生选择器
 a 选择
 b 退出
'''
sth=['奖励自己','做作业','打电动','睡觉','写代码','看书']#事情
print(zbt)
while True:
    def xz():#显示标题用的
        global xz1
        xz1=input('>>')
    xz()
    
    if xz1=='a':
        time.sleep(2)
        choice0=random.choice(sth)
        print('天意:',choice0)
    elif xz1=='b':
        exit()
    else:
        print('无效的输入')

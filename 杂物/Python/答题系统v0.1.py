import time
import random
from random import choices,randint
from sys import exit
tetle1='''
欢迎使用━(*｀∀´*)ノ亻!
     
    \【好好学习】/
    \【       】/
    \【天天向上】/

版本:0.1  by NNzyo   
正在加载...
'''
tetle='''
    语数英答题v0.1
  ch 语文  
  ma 数学
  en 英语
  cd 重新显示菜单
 '''
error='''
在做了在做了...
输入cd来显示菜单'''
tetled='''
    请选择难度
  EZ C卷 
  HD B卷
  DF A卷
'''
print(tetle1)
time.sleep(6)
print(tetle)
while True: 
  def cch():
    print('aaz')
  def cma():
    pass
  def cen():
    pass
  def xz():
    global xz1
    xz1=input('>>')
  xz()
  if xz1 == 'ch':
    print('加载中。')
    time.sleep(1)
    print('加载中。。')
    time.sleep(1)
    print('加载中。。。')
    time.sleep(1)
    cch()
  if xz1 == 'ma':
    print(error)
    cma()
  if xz1 == 'en':
    print(error)
    cen()
    

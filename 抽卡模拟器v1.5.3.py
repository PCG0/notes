#程序内部结构一览
import time
import random
from random import choices,randint
from sys import exit
zbt='''
   欢迎使用nt抽卡系统  
  up up卡池x1 
  upc up卡池x10 
  pt 普通卡池 
  ptc 普通卡池x10 
  wp 武器卡池x1 
  wpc 武器卡池x10 
  lck 卡池一览
  get 每日签到
  ye 查看余额
  cz 充值
  help 重新显示菜单
  wh 仓库
  mka 卖出卡片
  *** 敬请期待
  md 制作人名单
  rz 开发日志
  esc 退出
''' #主页面
fbt='''
     菜单
  up up卡池x1 
  upc up卡池x10 
  pt 普通卡池x1 
  ptc 普通卡池x10 
  wp 武器卡池x1 
  wpc 武器卡池x10 
  get 每日签到
  ye 查看余额
  lck 卡池一览
  cz 充值
  wh 仓库
  mka 买出卡片
  *** 敬请期待
  rz 开发日志
  esc 退出
''' #主页面
lck='''
up池:
['可莉(火)五星','诺艾尔(岩)四星','余芝昊(草)三星','牛子(岩)二星','无(无)无']
普通池:
['余芝昊(草)六星','安伯(火)四星','吴铸杰(草)三星','卢克(火)二星','无(无)无']
武器池:
['四风原典(五星)','试作斩岩(四星)','以理服人(二星)','咸鱼大剑(六星)','训练大刀(一星)']
'''
rz='''
21/
8.16(v0.1)
8.17(v1.0)
8.18(v1.4.9)
8.18(v1.5)
8.23(v1.5.1)
8.24(v1.5.2)
8.24(v1.5.3)
8.24(v1.5.4)
'''
md='''
    制作人名单
   作者 奈奈子
   指导 Rrction
   赞助 无(悲)
'''
upkac = ['可莉(火)五星','诺艾尔(岩)四星','余芝昊(草)三星','牛子(岩)二星','无(无)无']
ptkac = ['余芝昊(草)六星','安伯(火)四星','吴铸杰(草)三星','卢克(火)二星','无(无)无']
wpkac = ['四风原典(五星)','试作斩岩(四星)','以理服人(二星)','咸鱼大剑(六星)','训练大刀(一星)']
abab = ['sodayo～😯','是这样的旋律呢～🤔','嗯嗯😊','宁写错了😅','🔊⬆️⬇','️今天又是美好的一天呢～😙']
yuanshi=1600
print(zbt)#显示
cdkey = False
while True:  
  def upxz():#up抽卡
    a = random.choices(upkac,weights=[2,3,4,5,5])
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',a,'一个') 
  def upxz1():#up抽卡
    a = random.choices(upkac,weights=[0.5,4,5,6,7])    
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',a,'一个')   
  def ptxz():#穷b抽卡
    b = random.choices(ptkac,weights=[0.5,3,5,10,1])    
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',b,'一个')
  def ptxz1():#穷b抽卡
    b = random.choices(ptkac,weights=[0.1,3,5,10,1])    
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',b,'一个')
  def wpxz():#武器卡池
    c = random.choices(wpkac,weights=[1.5,2,3,1,4])
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',c,'一个')
  def wpxz1():#武器卡池
    c = random.choices(wpkac,weights=[0.5,1,4,0.1,5])
    print('抽取中.')
    time.sleep(0.5)
    print('抽取中..')
    time.sleep(0.5)
    print('抽取中...')
    time.sleep(0.5)
    print('宁中了:',c,'一个')  
  def waitnm():
    print('正在连接至服务器.')
    time.sleep(3)
    print('正在连接至服务器..')
    time.sleep(3)
    print('正在连接至服务器...')
    time.sleep(3)
    print('正在连接至服务器.')
    time.sleep(3)
    print('正在连接至服务器..')
    time.sleep(3)
    print('正在连接至服务器...')
    time.sleep(3)    
  def czxt():
    global yuanshi
    print('宁还有:',yuanshi)
    print('宁要冲多少？')
    czxz = input('>>')
    d = int(czxz)
    yuanshi = yuanshi + d 
    print('冲值完毕,请前往ye查看，1秒后未到账，请到tg向作者反馈')

  def yext():
    global yuanshi
    print('宁还有:',yuanshi)
  def xz():#显示标题用的
    global xz1
    xz1=input('>>')
  xz()
  if xz1 == 'up':
    e=int(yuanshi)
    if yuanshi<160:
      print('yuanshi不足，无法抽卡，请充值')
    else:
      yuanshi = yuanshi - 160
      upxz()
  elif xz1 == 'upc':
    e=int(yuanshi)
    if yuanshi<1600:
      print('yuanshi不足，无法抽卡，请充值')
    else:
      yuanshi = yuanshi - 1600
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
      upxz1()
  elif xz1 == 'pt':
    e=int(yuanshi)
    if yuanshi<150:
      print('yuanshi不足，无法抽卡，请充值')
    else:
      yuanshi = yuanshi - 150
      ptxz()
  elif xz1 == 'ptc':
    e=int(yuanshi)
    if yuanshi<1500:
      print('yuanshi不足，无法抽卡，请充值')
    else:
      yuanshi = yuanshi - 1500
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
      ptxz1()
  elif xz1 == 'wp':
    e=int(yuanshi)
    if yuanshi<160:
      print('yuanshi不足,无法抽卡,请充值')
    else:
      yuanshi = yuanshi - 160
      wpxz()
  elif xz1 == 'wpc':
    e=int(yuanshi)
    if yuanshi<1600:
      print('yuanshi不足,无法抽卡,请充值')
    else:
      yuanshi = yuanshi - 1600
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
      wpxz1()
  elif xz1 == 'lck':
    print(lck)
  elif xz1 == 'get':
    if not cdkey:
      key_y = randint(160,2000)      
      yuanshi = yuanshi + key_y
      print('签到成功～{0}原石～'.format(key_y))
      cdkey = True
    elif cdkey:
      print('今晚不做宁生意阿')
  elif xz1 == 'ye':
    yext()  
  elif xz1 == 'rz':
    print(rz)
  elif xz1 == 'cz':
    print('去tg向作者充值')
  elif xz1 == 'help':
    print(fbt)
  elif xz1 == '***':
    print('宁**宁马呢？')
  elif xz1 == 'wh':
    waitnm()
    waitnm()
    waitnm()
    waitnm()
    print('无法登陆账号，请稍后再试')
  elif xz1 == 'mka':
    waitnm()
    waitnm()
    waitnm()
    waitnm()
    print('无法连接至服务器，请稍后再试')    
  elif xz1 == 'esc':
    exit()
  elif xz1 == '114514':
    print('宁好臭啊')
    time.sleep(5)
    print('算了，宁自己加钱吧')
    czxt()
  elif xz1 == 'md':
    print(md)    
  else: 
    c = random.choice(abab)
    print(c)
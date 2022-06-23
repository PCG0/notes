#bt是标题ao要记住
#其他的自己理解
#阿吴啊，你又在通宵写py哦？休息一下吧，去打会原神好不好，抽一下卡吧
#记得按时去植发
#在？练一下伪音？
#rnm退钱！
#蚌埠住了
#xp是什么？是Windows系统么？（装傻）
import time
import random
upbt='''  
   选择
  uy 单发
  us 十发
'''       #抽卡选择页面
ptbt='''
   选择
  py 单发
  ps 十发
'''
zbt='''
欢迎使用nt抽卡系统  
  upc up卡池
  ptc 普通卡池
  ye 查看余额
  cz 充值
  *** 敬请期待
  rz 开发日志
''' #主页面
rz='''
21/
8.16添加余额查看,加了卡池.每人赠送一个草系连星都没有的角色（陈浩）外加昊子哥绝版本子一本
8.17添加了烦人的抽卡等待机制,减少了角色“陈浩”和“七七”的抽中概率，增加了亿些角色
'''
upkac = ['可莉(火)五星','菲谢尔(雷)四星','行秋(忘了)忘了','诺艾尔(岩)四星','以理服人','弓藏','陈浩(草)无星','陈浩(草)无星','陈浩(草)无星','陈睿(红)LV6']
ptkac = ['余芝昊(草)六星','安伯(火)四星','丘丘人(无)一星','吴铸杰(草)-五星','迪卢克(火)五星','学者的书','椰羊的本子','七七(水)五星','七七(水)五星','七七(水)五星']
yuan=200
print(zbt)#显示
while True:  
  def upxz():#up抽卡
    a = random.choice(upkac)
    print('抽取中.')
    time.sleep(1)
    print('抽取中..')
    time.sleep(1)
    print('抽取中...')
    time.sleep(1)
    print('宁中了:',a)    
  def ptxz():#穷b抽卡
    b = random.choice(ptkac) 
    print('抽取中.')
    time.sleep(1)
    print('抽取中..')
    time.sleep(1)
    print('抽取中...')
    time.sleep(1)
    print('宁中了:',b)
  def yext():
    global yuan
    print('宁还有:',yuan)
    print('金钱系统现在还没有实装')
  def xz():#显示标题用的
    global xz1
    xz1=input('>>')
  xz()
  if xz1 == 'upc':
    upxz()
  elif xz1 == 'ptc':
    ptxz()
  elif xz1 == 'ye':
    yext()  
  elif xz1 == 'rz':
    print(rz)
  elif xz1 == 'cz':
    print('宁在想屁吃')
  else:
    print('sodayo~')
    
  

  



  










  
  
  
  
  















#jg = random.choice(upkac)
    #print('中了:',jg)
#资料库
#random.choice (随机)

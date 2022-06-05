import random
import time

rmb=100
sd1=['杰哥','Steve','啊伟']
player=[]
help='''
    help    显示帮助（本列表）
    rmb     显示我的余额
    freecj  进入免费抽奖
    cj      进入高级抽奖
    my      查看我的物品
    sell    卖出我的物品
    log     登录
    cj 10   10连抽（付费）
    '''


print(help)
while True:
    a=input(">>>")
    if a=='help':
        print(help)
    elif a=='rmb':
        print('你的余额为{0}'.format(rmb))
    elif a=='freecj':
        print('欢迎进入免费抽奖,分为三个奖励： 一等奖（1000）  二等奖（50元）  三等奖（8元）')
        input("按下转行键来进行抽奖，你只有三次机会")
        l = 0
        while (l < 3):
            l = l + 1
            print(".......到底有没有中奖呢?........")
            time.sleep(1.8)
            a = random.randint(1, 20)
            if a == 20:
                print("恭喜中大奖--1000")
                rmb = rmb + 1000
            if a == 19:
                print("恭喜中二等奖--50元")
                rmb = rmb + 50
            if 16 < a < 19:
                print("恭喜中三等奖--8元")
                rmb = rmb + 8
            if a < 17:
                print("很遗憾，您没有中奖")
                input("按下转行键来再次进行抽奖")
            if a > 16:
                print("MD，你运气居然那么好，不敢跟你玩了，我怕还吃亏")
                break
    elif a=='cw':
        print('恭喜你发现了开发者模式')
        a=input('请输入你要添加的余额数')
        b=int(a)
        rmb=rmb+b
        print('添加成功，已经为您添加{0}元到余额,可输入’rmb‘查看'.format(b))
    elif a=='cw2':
        print('恭喜你发现了开发者模式2')
        a = input('请输入你要添加的人物(一个)')
        player.append(a)
        print('添加成功，已经为您添加{0},可输入”my“查看'.format(a))
    elif a=='my':
        print('你拥有的物品')
        print(player)
    elif a=='cj':
        b=input('每次抽奖都将花费10元，是否继续？（输入1继续）')
        c=int(b)
        if c==1:
            if rmb<10:
                print("你的余额不足，请到免费抽奖获取")
            else:
                rmb=rmb-10
                print("抽奖奖品有")
                print(sd1)
                print(".......到底会抽中什么奖品呢?........")
                time.sleep(1.8)
                a = random.randint(1, 10)
                if a==1:#1
                    player.append('杰哥')
                    print('恭喜你，你抽中了”杰哥“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 1<a<5:#3
                    player.append('Steve')
                    print('恭喜你，你抽中了”Steve“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
                if 4<a<10:#5
                    player.append('啊伟')
                    print('恭喜你，你抽中了”啊伟“')
                    print('物品已经放置到你的仓库，可输入’my‘前去查看')
    elif a=='sell':
        if player==[]:
            print('检测到你的背吧没有物品，不能卖出')
        if player!=[]:
            print('你现在拥有的物品')
            print(player)
            print('注意：无论卖出什么，余额都只增加5')
            a=input('请选择你要卖出的物品序号,一次只能卖出一个（从左到右依次为0，1，2，3.....）')
            b=int(a)
            c=player.pop(b)
            print('你已经卖出{0}'.format(c))
            rmb=rmb+5
            print("余额已经增加5，可以输入”rmb“查看")
    elif a=='cj 10':
        az=0
        b=input('本次抽奖都将花费100元，是否继续？（输入1继续）')
        c=int(b)
        if c==1:
            if rmb<100:
                print("你的余额不足，请到免费抽奖获取")
            else:
                rmb=rmb-100
                while (az<10):
                    time.sleep(1.3)
                    az = az + 1
                    a = random.randint(1, 10)
                    if a == 1:  # 1
                        player.append('杰哥')
                        print('恭喜你，你抽中了”杰哥“')
                    if 1 < a < 5:  # 3
                        player.append('Steve')
                        print('恭喜你，你抽中了”Steve“')
                    if 4 < a < 10:  # 5
                        player.append('啊伟')
                        print('恭喜你，你抽中了”啊伟“')
                print('物品已经放置到你的仓库，可输入’my‘前去查看')
    else:
        print('请输入正确的指令，可输入”help“寻求帮助')


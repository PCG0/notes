#模块
import random
import time

#各参数面板
p=0
qwe=0
rmb=0
hp=2
tl=20
player=[]
help='''
_____________________________帮 助_____________________________
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 余额      显示自身软妹币      背包      查看物品数量       
 物品      查看自身常见物品    拾荒      扣除HP获取物品     
 系统      查看隐藏的常用代码  答题      答题来赚取软妹币
 背包      查看背包所有物品
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
抵制不良游戏，拒绝盗版游戏，请支持正版。
---------------------------------------------------------------
游戏版本：v1.0   版本号：00000000
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
hope='''____系 统____
>>>>>>>>>>>>>
物品使用说明
抽奖几率说明
答题赚钱说明
>>>>>>>>>>>>>
'''
hope4=''''''

hope1='''
>>>>>>>>>>>>>>>>
软妹币剩余：
____________
(    {0}    )
￣￣￣￣￣￣
>>>>>>>>>>>>>>>>
'''.format(rmb)
hope2='''
'''
hope3='''
'''

#指令组开头
print(help)
while True:
    a=input("你:")
    if a=='帮助':
        print(help)
    if a=='余额':
        print(hope1)
    if a=='关闭':
        b=input(hope2)
        c=int(b)
        break
    elif a=='背包':
        print('你拥有的物品')
        print(player)
    if a=='系统':
        print(hope)
    elif a=='使用医疗包':#
        az=player.count("医疗包")
        ax=int(az)
        b=input('''医疗包剩余({0})，发送[ 2 ]确定使用
'''.format(ax))
        if b=='2':
            if ax<1:
                print("当前医疗包不足，不能使用")
            else:
                ax=ax-1
                hp=hp+5
                print('HP增加成功，HP剩余({0}%),({1}%)'.format(hp,ax))
    elif a=='使用饮料':#
        za=player.count('饮料')
        zf=int(za)
        b=input('''饮料剩余({0})，发送[ 2 ]确定使用
'''.format(zf))
        if b=='2':
            if zf<1:
                print("饮料不足，不能使用")
            else:
                zf=zf-1
                tl=tl+2
                print('体力增加成功，剩余({0}%)'.format(tl))
    elif a=="充值":
        zs=input('''您的余额为{0},请问您要充值多少？
'''.format(rmb))
        za=int(zs)
        if 0<za<1000:
            a=random.randint(1,10)
            if a==1:
                print("恭喜您，充值成功")
                print("已到账{0}元，可输入“rmb”查看".format(za))
                rmb=rmb+za
            else:
                print("充值失败，请联系管理员或者作者并把错误代码提供")
                print("错误代码：404  滞留金额：{0}".format(za))
        else:
            print("充值失败，请联系管理员或者作者并把错误代码提供")
            print("错误代码：404  滞留金额：{0}".format(za))
    elif a=='版本':
        print('''
♢版本号：v1.0
♢开发者：[梦之魇]
♢版权：此游戏版权归[梦之魇]所有
♢特别鸣谢：[ResuRrction],[C:\ _]和[CrosWuft]，感谢大佬们相助
''')
    elif a=='物品':
        za=player.count('饮料')
        zf=int(za)
        az=player.count("医疗包")
        ax=int(az)
        sd=player.count("面包")
        cx=int(sd)
        sw=player.count("熟食")
        sq=int(sw)
        cv=player.count("蜂蜜")
        cb=int(cv)
        xv=player.count('酒精')
        xd=int(xv)
        cj=player.count('木板')
        co=int(cj)
        ch=player.count('碎石')
        cv=int(ch)
        lm=player.count('木棍')
        cd=int(lm)
        print("你有 {0} 个饮料".format(zf))
        print("你有 {0} 个医疗包".format(ax))
        print("你有 {0} 个面包".format(cx))
        print("你有 {0} 个熟食".format(sq))
        print("你有 {0} 个蜂蜜".format(cb))
        print("你有 {0} 个酒精".format(xd))
        print("你有 {0} 个木板".format(co))
        print("你有 {0} 个碎石".format(cv))
        print("你有 {0} 个木棍".format(cd))
        alp=zf+ax+cx+sq+cb+xd+co+cv+cd
        print("你一共拥有 {0} 件物品".format(alp))
        print('''''')
    elif a=='背包':#
        print('你拥有的物品')
        print(player)
    elif a=='猜数':
        secret = random.randint(1, 20)
        print(".........猜数游戏.........")
        temp = input("不妨猜一下我心里想的是哪个数字，你只有五次机会,第一次就猜中有惊喜")
        guess = int(temp)
        az = 0
        while az < 5:
            az = az + 1
            if guess != secret:
                temp = input("哎呀，猜错了，请重新输入吧")
                guess = int(temp)
                if guess == secret:
                    print("卧槽，这你都知道")
                    break
                else:
                    if guess > secret:
                        print(" 哥，大了大了")
                    else:
                        if guess < secret:
                            print("哥，小了小了")
            else:
                print("wow，你居然一下子就猜中了，奖励你50吧")
                rmb = rmb + 50
                break
    elif a=='计算':
        x=0
        n=0
        m=0
        print(".................计算答题..................")
        ab=input('请输入你想要答的题数,答五题得一元(不足五题不送钱),无论对错都获得:而且如果你答题超过14题且准确率高的话还会额外再送钱')
        ac=int(ab)
        if ac>4:
            rmb=rmb+(ac/2)
            print('已经赠送您{0}元，可输入“rmb”查看余额'.format(ac/2))
        else:
            print("你所答的题目数量不够5，无法获得rmb,但是你仍然可以答题")
        while (x < ac):
            x = x + 1
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print("请问 {0}+{1} 等于多少".format(a,b))
            c = input("请输入等于几：")
            d = int(c)
            e = a + b
            if e == d:
                print("真棒，你答对了，继续答题吧")
                n = n + 1
            else:
                print("糟糕，你答错了，正确答案是 {0}".format(e))
                m = m + 1
            print("现在你做的题目数为 {0} ,还要做的题目数为 {1}".format(x, ac - x))
            print("....................................................................")
            time.sleep(1)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if 20 >= n >= 0.8 * ac:
            print("你的评分为：     A")
            if ac>14:
                print("看你那么厉害，就奖励你30元吧")
                rmb = rmb + 30
        if 0.8 * ac > n >= 0.6 * ac:
            print("你的评分为：     B")
            if ac > 14:
                print("看你那么厉害，就奖励你10元吧")
                rmb = rmb + 10
        if 0.6 * ac> n >= 0.4 * ac:
            print("你的评分为：     C")
            if ac > 14:
                print("看你那么厉害，就奖励你5元吧")
                rmb = rmb + 5
        if 0.4 * ac > n >= 0.2 * ac:
            print("你的评分为：     D")
        if 0.2 * ac > n >= 0:
            print("你的评分为：     E")
    elif a=='拾荒':#
        ac=input('''
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
拾荒：每次拾荒需要1体力
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[饮料]            ^
[医疗包]          ^
[木板]            ^
[碎石]            ^
[木棍]            ^
[面包]            ^
[熟食]            ^
[酒精]            ^
[蜂蜜]            ^
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
请发送去拾荒的次数，再发送[ 1 ]出发
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
---------------------------------------------------------------
''')
        ab=int(ac)
        if ab<1:
            print("数字{0}出现错误,请重新尝试".format(ac))
        else:
            moy=1*ab
            b=input('''---------------------------------------------------------------
你确定使用 [{0}] 体力拾 [{1}] 次荒吗？


发送[ 1 ]确定
---------------------------------------------------------------
'''.format(moy,ab))
            if not b.isdigit():
                print("请输入数字！")
            else:
                c=int(b)
                if c==1:
                    if tl<moy:
                        print("你的体力不足，请到使用饮料恢复")
                    else:
                        az=0
                        tl=tl-moy
                        while (az < ab):
                            time.sleep(2)
                            az = az + 1
                            a = random.randint(1, 200)
                            if a == 1:  # 1
                                player.append('医疗包')
                                print('恭喜你，你找到了”医疗包“')
                            if 1 < a < 5:  # 3
                                player.append('酒精')
                                print('恭喜你，你找到了”酒精“')
                            if 4 < a < 8:  # 3
                                player.append('熟食')
                                print('恭喜你，你找到了"熟食“')
                            if 7 < a < 15:  # 7
                                player.append('蜂蜜')
                                print('恭喜你，你找到了”蜂蜜“')
                            if 14 < a < 25:  # 10
                                player.append('木板')
                                print('恭喜你，你找到了”木板“')
                            if 24 < a < 35:  # 10
                                player.append('碎石')
                                print('恭喜你，你找到了”碎石“')
                            if 34 < a < 51:  # 16
                                player.append('木棍')
                                print('恭喜你，你找到了”木棍“')
                            if 50 < a < 201: # 150
                                player.append('饮料')
                                print('恭喜你，你找到了”饮料“')
                        print('物品已经放置到你的仓库，可输入（背包）或者（物品）前去查看')
                        print('''你的体力剩余({0}%)'''.format(tl))
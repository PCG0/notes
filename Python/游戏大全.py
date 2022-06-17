import random
import time

print("随便输一下预设代码吧")
print ('输入‘help()’来获得帮助')
def mpk() :
    print (".................速算答题..................")
    x=0
    n=0
    m=0
    difficult1=input("请输入你想要的模式，输入除1外任意数直接开始，输入1进入高级选项")
    difficult2=int(difficult1)
    if difficult2 ==1:
        z=input("请输入你想答的题数(输入0为随机题数)")
        y=int(z)
        w=input('请输入最小加数')
        t=int(w)
        h=input("请输入最大加数")
        u=int(h)
        if y==0:
            y=random.randint(1,45)
        while (x<y):
            x=x+1
            a=random.randint (t,u)
            b=random.randint (t,u)
            print ("请问")
            print (a)
            print ("加")
            print (b)
            print("答案是：")
            c=input("请输入等于几：")
            d=int(c)
            e=a+b
            if e==d:
                print ("真棒，你答对了，继续答题吧")
                print("现在你做的题目数 以及 还要做的题目数为;")
                n=n+1
            else:
                print ("糟糕，你答错了，正确答案是......")
                print (e)
                m=m+1
                print('现在你做的题目数 以及 还要做的题目数为;')
            print (x,y-x)
            print("....................................................................")
            time.sleep(0.8)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if y>=n>=0.8*y:
            print("你的评分为：     A")
        if 0.8*y>n>=0.6*y:
            print("你的评分为：     B")
        if 0.6*y>n>=0.4*y:
            print("你的评分为：     C")
        if 0.4*y>n>=0.2*y:
            print("你的评分为：     D")
        if 0.2*y>n>=0:
            print("你的评分为：     E")
    if difficult2!=1:
        while (x<20):
            x=x+1
            a=random.randint (1,10)
            b=random.randint (1,10)
            print ("请问")
            print (a)
            print ("加")
            print (b)
            print("答案是：")
            c=input("请输入等于几：")
            d=int(c)
            e=a+b
            if e==d:
                 print ("真棒，你答对了，继续答题吧")
                 print("现在你做的题目数 以及 还要做的题目数为;")
                 n=n+1
            else:
                 print ("糟糕，你答错了，正确答案是......")
                 print (e)
                 m=m+1
                 print('现在你做的题目数 以及 还要做的题目数为;')
            print (x,20-x)
            print("....................................................................")
            time.sleep(0.8)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if 20>=n>=0.8*20:
            print("你的评分为：     A")
        if 0.8*20>n>=0.6*20:
            print("你的评分为：     B")
        if 0.6*20>n>=0.4*20:
            print("你的评分为：     C")
        if 0.4*20>n>=0.2*20:
           print("你的评分为：     D")
        if 0.2*20>n>=0:
            print("你的评分为：     E")
    print('                             ')
    print("随便输一下预设代码吧")
    print('输入‘help()’来获得帮助')
def mpkyyds():
    print(".................速算答题..................")
    x = 0
    n = 0
    m = 0
    difficult1 = input("请输入你想要的模式，输入除1外任意数直接开始，输入1进入高级选项")
    difficult2 = int(difficult1)
    if difficult2 == 1:
        z = input("请输入你想答的题数(输入0为随机题数)")
        y = int(z)
        w = input('请输入最小加数')
        t = int(w)
        h = input("请输入最大加数")
        u = int(h)
        if y == 0:
            y = random.randint(1, 45)
        while (x < y):
            x = x + 1
            a = random.randint(t, u)
            b = random.randint(t, u)
            print("请问")
            print(a)
            print("加")
            print(b)
            print("答案是：")
            print(a + b)
            c = input("请输入等于几：")
            d = int(c)
            e = a + b
            if e == d:
                print("真棒，你答对了，继续答题吧")
                print("现在你做的题目数 以及 还要做的题目数为;")
                n = n + 1
            else:
                print("糟糕，你答错了，正确答案是......")
                print(e)
                m = m + 1
                print('现在你做的题目数 以及 还要做的题目数为;')
            print(x, y - x)
            print("....................................................................")
            time.sleep(0.8)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if y >= n >= 0.8 * y:
            print("你的评分为：     A")
        if 0.8 * y > n >= 0.6 * y:
            print("你的评分为：     B")
        if 0.6 * y > n >= 0.4 * y:
            print("你的评分为：     C")
        if 0.4 * y > n >= 0.2 * y:
            print("你的评分为：     D")
        if 0.2 * y > n >= 0:
            print("你的评分为：     E")
    if difficult2 != 1:
        while (x < 20):
            x = x + 1
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            print("请问")
            print(a)
            print("加")
            print(b)
            print("答案是：")
            print(a + b)
            c = input("请输入等于几：")
            d = int(c)
            e = a + b
            if e == d:
                print("真棒，你答对了，继续答题吧")
                print("现在你做的题目数 以及 还要做的题目数为;")
                n = n + 1
            else:
                print("糟糕，你答错了，正确答案是......")
                print(e)
                m = m + 1
                print('现在你做的题目数 以及 还要做的题目数为;')
            print(x, 20 - x)
            print("....................................................................")
            time.sleep(0.8)
        print("你做对的题数为")
        print(n)
        print("你做错的题数为")
        print(m)
        if 20 >= n >= 0.8 * 20:
            print("你的评分为：     A")
        if 0.8 * 20 > n >= 0.6 * 20:
            print("你的评分为：     B")
        if 0.6 * 20 > n >= 0.4 * 20:
            print("你的评分为：     C")
        if 0.4 * 20 > n >= 0.2 * 20:
            print("你的评分为：     D")
        if 0.2 * 20 > n >= 0:
            print("你的评分为：     E")
    print('                           ')
    print("随便输一下预设代码吧")
    print('输入‘help()’来获得帮助')


def help():
    print('输入‘mpk（）’为进入计数比赛')
    print('输入‘mpkyyds（）’为进入计数比赛外挂版')
    print('输入‘help（）’为显示此表')
    print('输入‘cj()’为进入抽奖')
    print('输入‘cs（）’来进行猜数')
    print('输入‘pjf（）’来计算平均分')
    print("随便输一下预设代码吧")

def cj():
    sud=0
    print("幸运大抽奖，分为三个奖励： 一等奖（一百万）  二等奖（一百元）  三等奖（十元） ")
    input("按下转行键来进行抽奖")
    while sud<6:
        print(".......到底有没有中奖呢?........")
        time.sleep(1.9)
        a = random.randint(1, 20)
        if a == 20:
            print("恭喜中大奖--100万")
        if a == 19:
            print("恭喜中二等奖--100元")
        if 16 < a < 19:
            print("恭喜中三等奖--10元")
            print("我居然亏了")
        if a < 17:
            print("很遗憾，您没有中奖")
            sud=sud+1
            if sud<6:
                input('再次按下转行键来进行抽奖')
            else:
                print('不玩了，你运气那么差')
                break
        if a > 16:
            print("MD，你运气居然那么好，不敢跟你玩了，我怕还吃亏")
            break
    print("随便输一下预设代码吧")
    print('输入‘help()’来获得帮助')
def cs():
    a=0
    secret = random.randint(1, 15)
    temp = input("不妨猜一下我心里想的是哪个数字,你只有5次机会哦")
    guess = int(temp)
    while a<6:
        if guess != secret:
            temp = input("哎呀，猜错了，请重新输入吧")
            a=a+1
            guess = int(temp)
        if guess == secret:
            print("卧槽，这你都知道")
            print("恭喜猜中，但游戏结束啦，不玩啦")
            break
        else:
            if guess > secret:
                print(" 哥，大了大了")
            else:
                if guess < secret:
                    print("哥，小了小了")
    if a>=6:
        print('这都猜不中，不玩了')
    print('                                    ')
    print("随便输一下预设代码吧")
    print('输入‘help()’来获得帮助')
def pjf():
    print('请分别输入四次成绩，系统将自动为您统计')
    q = 1
    while q == 1:
        a = int(input('请输入第一次成绩'))
        b = int(input('请输入第二次成绩'))
        c = int(input('请输入第三次成绩'))
        d = int(input('请输入第四次成绩'))
        e = (a + b + c + d) / 4
        print('你的平均成绩为：')
        print(e)
        break
    print('                           ')
    print("随便输一下预设代码吧")
    print('输入‘help()’来获得帮助')

from random import randint,choice
from collections import deque
from time import sleep as sp
from sys import exit

history = deque([],100)#deque容器
DrawHistory = deque([],500)#历史抽卡数容器
#★
Card = ['博丽灵梦','雾雨魔理沙','八云蓝','八云紫','西行寺幽幽子']#卡池
DrawTime = 0#抽卡次数容器

SC = "少女抽卡中......\n"

class roll:#随机数
    def __init__(self,Roll):
        self.Roll = Roll
    def InputRoll(self):
        print("Roll:",self.Roll)
def OnePoll():#单次抽卡
    global DrawTime
    DrawTime += 1
    CnName = choice(Card)
    print(SC)
    DrawHistory.append(CnName)
    sp(0.5)
    print(CnName)
def TenPoll():#十连抽
    global DrawTime
    DrawTime += 10
    TenName = [choice(Card) for _ in range(10)]
    print(SC)
    sp(0.5)
    DrawHistory.append(TenName)
    print(TenName)
def RollPower():#随机数附加语句
    if randroll <= 25:
        print("大失败")
    elif randroll <= 50:
         print("失败")
    elif randroll <= 75:
        print("成功")
    elif randroll <= 99:
        print("大成功")
    else:
        print("欧皇，去抽卡吧！")
def InputHelp():#帮助界面
    help = '''
    r 生成一个随机数
    help 帮助
    poll 抽卡
    poll 10 抽十次卡
    deque poll 显示历史抽出的卡
    deque 历史50条输入记录
    deque clr 删除全部历史输入记录
    '''
    print(help)



while True:#命令检测并执行
    index = input(">>")
    history.append(index)
    if index == "r":#生成一个随机数
        randroll = randint(0,100) 
        Roll = roll(randroll)
        Roll.InputRoll()
        RollPower()
    elif index == "help":#列出命令名单
        InputHelp()
    elif index == "deque":#历史键入记录
        print(list(history))
        history.pop()#弹出deque最右侧的元素
    elif index == "deque clr":#清除deque记录
        history.clear()
        print('已清除')
    elif index == "poll":#抽卡
        OnePoll()
    elif index == "deque poll":#历史卡牌数
        print(list(DrawHistory))
        print("共抽取{}张卡".format(DrawTime))
    elif index == "poll 10":#抽卡——十连
        TenPoll()
    elif index == "exit":#关闭程序
        exit(0)
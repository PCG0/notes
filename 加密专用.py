import random

print("吴涛加密系统1.0》加密文件")
while True:
    wen1 = random.randint(1, 100000)
    a=input("请输入明文,系统将会将其转化为密文")
    if not a.isdigit():#报错
        print("请输入数字!!!")
        print("        ")
    else:
        b=int(a)
        miwen2=input("请输入密钥,(输入0为随机)")
        if not miwen2.isdigit():
            print("错误!!!")#报错
            print("        ")
        else:
            miwen1=int(miwen2)
            if miwen1==0:
                print("你的密钥为{0}".format(wen1))
            else:
                wen1=wen1-wen1+miwen1
                print("你的密钥为{0}".format(wen1))
            scret=((b*wen1)/2)*wen1*600
            print('你的密文为{:.0f}'.format(scret))

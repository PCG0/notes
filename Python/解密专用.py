print("吴涛加密系统1.0》解密文件")
while True:
    a = input("请输入密文,系统将会将其转化为明文")
    if not a.isdigit():#报错
        print("请输入数字!!!")
        print("        ")
    else:
        miyao2=input("请输入密钥")
        if not miyao2.isdigit():  # 报错
            print("错误!!!")
            print("          ")
        else:
            b=int(a)
            miyao=int(miyao2)
            miwen=(b/600)/miyao*2/miyao
            print("明文为{:.0f}".format(miwen))
            print("                 ")
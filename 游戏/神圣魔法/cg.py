import tkinter,codecs
from tkinter import simpledialog
    #大窗口事宜
root = tkinter.Tk()
root.minsize(300,300)
#la1 = tkinter.Label(root,text='',font=70)
#la1.pack()
#la2 = tkinter.Label(root,text='')
#la2.pack()
    #对话文本显示
i = -1#数值修正
def windows_text():
    w_text = tkinter.simpledialog.SimpleDialog(root,text=t,buttons=['知道了'])
    print(w_text.go())
while True:
    i += 1
    int(i)
    with codecs.open('C:\\Users\\resum\\OneDrive - rrr6\\桌面\\新建文件夹 (2)\\游戏\\神圣魔法\\zx.txt',"r",'utf-8') as file:
        sl = file.readlines()
        t = sl[i].strip('\n')
    file.close()
    windows_text()
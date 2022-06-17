import time
import random
import pickle
import tkinter.messagebox
from random import choices,randint
from sys import exit
import tkinter as tk
from tkinter.constants import COMMAND, Y


time.sleep(2)
def log():
    time.sleep(3)
    logt=tk.Tk
    logt.geometry('350x100')
    logt.title('Error')

    tk.Label(logt, text='错误代码:002',font=('Arial',15)).place(x=0, y=10)
    tk.Label(logt, text='请查看网络是否连接',font=('Arial',15)).place(x=0, y=50)
def up():
    def seve():

    
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        # 這裡是開啟我們記錄資料的檔案，將註冊資訊讀出
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        # 這裡就是判斷，如果兩次密碼輸入不一致，則提示Error, Password and confirm password must be the same!
        if np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')

        # 如果使用者名稱已經在我們的資料檔案中，則提示Error, The user has already signed up!
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'The user has already signed up!')

        # 最後如果輸入無以上錯誤，則將註冊輸入的資訊記錄到檔案當中，並提示註冊成功Welcome！,You have successfully signed up!，然後銷燬視窗。
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            # 然後銷燬視窗。
            up.destroy()
    up=tk.Tk()
    up.geometry('350x200')
    up.title('注册')

    new_name = tk.StringVar()  
    new_name.set('example@python.com') 
    tk.Label(up, text='账号: ').place(x=10, y=10) 
    entry_new_name = tk.Entry(up, textvariable=new_name) 
    entry_new_name.place(x=130, y=10)  

    new_pwd = tk.StringVar()
    tk.Label(up, text='密码: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=130, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(up, text='再次输入密码: ').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=130, y=90)


    
def by():
    by=tk.Tk
    by.geometry('350x100')
    by.title('我横科爱，请亏我全:D（')

    tk.Label(by, text='联系方式:',font=('Arial',15)).place(x=0, y=0)
    tk.Label(by, text='telegram:@NNzyo',font=('Arial',15)).place(x=0, y=30)
    tk.Label(by, text='QQ:2771470255',font=('Arial',15)).place(x=0, y=60)
def hi():
    hi=tk.Tk()
    hi.geometry('350x100')
    hi.title('密码找回')

    tk.Label(hi, text='解决方法:',font=('Arial',15)).place(x=0, y=0)
    tk.Label(hi, text='请到后台查看或修改文件以找回密码',font=('Arial',15)).place(x=0, y=30)


def main():
    window=tk.Tk()
    window.title('登录')
    window.geometry('300x400')

    tk.Label(window,text='答题系统',font=('wtf',40),width=20, height=3).place(x=-120,y=10)  
    tk.Label(window,text='账号: ',font=('Arial',15)).place(x=40, y= 150)
    tk.Label(window,text='密码: ',font=('Arial',15)).place(x=40, y= 190)
    tk.Label(window,text='好好学习 天天向上',font=('Arial',14)).place(x=65,y=120)
    tk.Label(window,text='       by NNzyo').place(x=20,y=370)


    usr_name = tk.StringVar()
    ausr_name = tk.Entry(window, textvariable=usr_name)
    ausr_name.place(x=100, y=155)
    usr_pwd = tk.StringVar()
    ausr_pwd = tk.Entry(window, textvariable=usr_pwd,show='*')
    ausr_pwd.place(x=100, y=195)

    tn_login = tk.Button(window, text='登录',font=('Arial',15),width=9,height=1,command=log)
    tn_login.place(x=45, y=230)
    btn_sign_up = tk.Button(window, text='注册',font=('Arial',15),width=9,height=1,command=up)
    btn_sign_up.place(x=160, y=230)
    ms = tk.Button(window,text='联系作者',width=12,height=1,command=by)
    ms.place(x=170,y=365)
    hl = tk.Button(window,text='找回密码',width=8,height=1,command=hi)
    hl.place(x=190,y=275)

    window.mainloop()
main()

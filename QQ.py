import tkinter as tk

window = tk.Tk()
window.title('QQ邮箱（py版）')
window.geometry('450x300')

l = tk.Label(window, 
    text='欢迎使用QQ邮箱',    # 标签的文字
    font=('Arial', 40),     # 字体和字体大小
    width=15, height=2)  # 标签长宽
l.pack()    # 固定窗口位置

# user information
tk.Label(window, text='账号: ').place(x=50, y= 150)
tk.Label(window, text='密码: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    pass
def usr_sign_up():
    window_sign_up=tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', )
    btn_confirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='登录', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='注册', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
import tkinter as tk

window=tk.Tk()
window.title('RBG game')
window.geometry('300x100')

var=tk.StringVar()
l=tk.Label(window,textvariable=var,font=('Arial',12),width=25,
           height=2)
l.pack()

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('休息一下吧，看会书好不好 -阿妈')
    else:
        on_hit=False
        var.set('')

b=tk.Button(window,text='开始游戏',width=15,
            height=2,command=hit_me)
b.pack()
    
window.mainloop()
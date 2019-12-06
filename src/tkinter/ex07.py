from tkinter import *

win = Tk()
str = 'label基本属性测试'

label = Label(win)
label.config(text=str, justify=CENTER, width=20, height=4, bd=2,
             relief=SOLID, wraplength=160, anchor=W, font=('宋体', 18))
label.pack(side=TOP)

win.geometry('300x200')
win.mainloop()

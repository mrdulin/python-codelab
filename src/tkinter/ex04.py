from tkinter import *

win = Tk()

label1 = Label(win, text='请选择下列操作', fg='green')
label1.grid(row=0, column=0, columnspan=4)

btn1 = Button(text='copy')
btn2 = Button(text='cut')
btn3 = Button(text='paste')
btn4 = Button(text='delete')

btn1.grid(row=2, column=0, padx=2)
btn2.grid(row=2, column=1, padx=2)
btn3.grid(row=2, column=2, padx=2)
btn4.grid(row=2, column=3, padx=2)

win.title('example 4')
win.geometry('300x150')
win.mainloop()

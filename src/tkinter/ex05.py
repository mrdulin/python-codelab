from tkinter import *

win = Tk()

label1 = Label(win, text='place()方法测试', fg='black')
label1.place(x=140, y=50, anchor=N)

btn1 = Button(text='place()按钮')
btn2 = Button(text='grid()')
btn1.place(x=140, y=80, anchor=N)  # N = north, NW = northwest
btn2.grid(row=2, column=1)

win.title('example 5')
win.geometry('300x200')
win.mainloop()

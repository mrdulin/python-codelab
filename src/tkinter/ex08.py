from tkinter import *

win = Tk()
win.title('Button Test')
win.geometry('300x200')

label = Label(win, text='此处显示计算结果', font=('宋体', 12))
label.pack()


def compute():
    sum = 0
    for i in range(1, 101):
        sum += i
    result = '累加结果是: ' + str(sum)
    label.config(text=result)


button = Button(win, text='计算1到100累加值', justify=CENTER,
                width=20, height=3, bd=3, relief=RAISED, anchor=CENTER, font=('隶书', 12, 'underline'), command=compute, activebackground='yellow', activeforeground='red')
button.pack()

win.mainloop()

from tkinter import *

win = Tk()
win.title('Entry Test')
win.geometry('300x200')

label_for_entry = Label(win, text='请输入计算数据：', width=16,
                        height=3, font=('宋体', 12))
label_for_entry.grid(row=0, column=0)

number = StringVar()
entry = Entry(win, textvariable=number, width=16)
entry.grid(row=0, column=1)

label_for_confirm = Label(win, text='请单击确认：', width=14,
                          height=3, font=('宋体', 12))
label_for_confirm.grid(row=1, column=0)


def computing():
    sum = 0
    n = int(number.get())
    for i in range(n+1):
        sum += i
    result = '累加结果是：' + str(sum)
    label_show_result.config(text=result)


button = Button(win, text='计算', justify=CENTER,
                width=14, height=2, bd=3, relief=RAISED, anchor=CENTER, font=('隶书', 12), command=computing)
button.grid(row=1, column=1)

label_show_result = Label(win, text='显示结果', width=16,
                          height=3, font=('宋体', 12))
label_show_result.place(x=50, y=130)
win.mainloop()

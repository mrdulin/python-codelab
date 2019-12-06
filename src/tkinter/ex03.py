from tkinter import *

win = Tk()
label1 = Label(win, text='标签标题', fg='white', bg='blue')
label1.pack(anchor=NW, padx=5)

label2 = Label(win)
label2.config(text='标签内容', fg='white', bg='grey')
label2.pack(expand=YES, fill=BOTH, padx=5)

btn = Button()
btn['text'] = 'click'
btn.pack()

win.title('Example 3')
win.geometry('300x200')
win.mainloop()

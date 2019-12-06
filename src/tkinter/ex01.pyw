import tkinter

win = tkinter.Tk()

label1 = tkinter.Label(win, text='Hello, Python')
btn1 = tkinter.Button(win, text='click')

label1.pack()
btn1.pack()
win.mainloop()

import tkinter

win = tkinter.Tk()

label = tkinter.Label(win)
label.config(text='Hello Python')
label.config(fg='white', bg="blue")
label.pack()

label1 = tkinter.Label(win, text='Hello, Python')
label1.pack()

btn1 = tkinter.Button(win, text='click')
btn1.pack()

win.title('tkinter example')
win.geometry('300x200')
win.mainloop()

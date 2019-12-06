from tkinter import *

win = Tk()

frame_a = Frame()
frame_b = Frame()

frame_a.pack()
frame_b.pack()

label_username = Label(frame_a, text='Username', width=10, fg='black')
entry_username = Entry(frame_a, width=20)
label_username.grid(row=1, column=1)
entry_username.grid(row=1, column=2)

label_password = Label(frame_a, text='Password', width=10, fg='black')
entry_password = Entry(frame_a, width=20)
label_password.grid(row=2, column=1)
entry_password.grid(row=2, column=2)

btn_reset = Button(frame_b, text='Reset', width=10)
btn_submit = Button(frame_b, text='Submit', width=10)
btn_reset.grid(row=1, column=1)
btn_submit.grid(row=1, column=2)

win.title('example 6')
win.geometry('300x200')
win.mainloop()

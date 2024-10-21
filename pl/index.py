from tkinter import *
from be.Register_User import Register

win = Tk()

# Setting Screen

win.geometry('800x600')
win.title("Register")
win.resizable(width=False, height=False)

class App:
    def __init__(self):
        pass

# Text Screen

win.config(bg='blue')
txtnamee = StringVar()
txtname = Entry(win, width=25, background="white", foreground="#000000", bd=3, justify='center', textvariable=self.name)
txtname.place(x=200, y=100)


txtnamee.set("Name")

win.mainloop()

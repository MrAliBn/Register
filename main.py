from pl import index
from tkinter import *

if __name__ == "__main__":
    screen = Tk()
    screen.geometry("%dx%d+%d+%d" % (800, 400, 200, 200))
    screen.title("Register")
    screen.resizable(False, False)
    paheme = index.App(screen)
    screen.mainloop()

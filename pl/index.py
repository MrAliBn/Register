from be.Register_User import Register_User
from tkinter import messagebox, ttk
from tkinter import *


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.text_screen()

    # function
    def OneClickedRegister(self):
        user = Register_User(self.txtname.get(), self.txtfamily.get(), self.txtfilde.get(), self.txtage.get())
        user.add_user()

# screen text
    def text_screen(self):
        self.name = StringVar()
        self.txtname = Entry(self.screen, textvariable=self.name)
        self.txtname.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtname.place(x=300, y=50)
        self.name.set("Username")

        self.family = StringVar()
        self.txtfamily = Entry(self.screen, textvariable=self.family)
        self.txtfamily.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfamily.place(x=300, y=100)
        self.family.set("Family")

        self.filde = StringVar()
        self.txtfilde= Entry(self.screen, textvariable=self.filde)
        self.txtfilde.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfilde.place(x=300, y=150)
        self.filde.set("Filde")

        self.age = StringVar()
        self.txtage = Entry(self.screen, textvariable=self.age)
        self.txtage.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtage.place(x=300, y=200)
        self.age.set("Age")

        # Button Screen

        btnscreen = Button(self.screen, text="Register", width=15, command=self.OneClickedRegister)
        btnscreen.configure(bg="green", fg="black", bd=3, justify="center")
        btnscreen.place(x=310, y=250)



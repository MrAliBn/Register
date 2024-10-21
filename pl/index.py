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
        if self.name.get() == "Username" or self.txtname.get() == '' or not self.txtname.get().isalpha():
            messagebox.showerror("Error", "Please enter your name is alpha")
            self.txtname.focus()
        elif self.family.get() == "Family" or self.txtfamily.get() == '' or not self.txtfamily.get().isalpha():
            messagebox.showerror("Error", "Please enter your family name is alpha")
            self.txtfamily.focus()
        elif self.filde.get() == "Filed" or self.txtfilde.get() == '' or not self.txtfilde.get().isalpha():
            messagebox.showerror("Error", "Please enter your filed is alpha")
            self.txtfilde.focus()
        elif self.age.get() == "Year" or self.txtage.get() == '' or not self.txtage.get().isdigit():
            messagebox.showerror("Error", "Please enter your age is digit")
            self.txtage.focus()
        else:
            user = Register_User(self.txtname.get(), self.txtfamily.get(), self.txtfilde.get(), self.txtage.get())
            user.add_user()
            messagebox.showinfo("Registered", "Registered")

        # clear
    def clear_name(self, e):
        self.name.set('')

    def clear_family(self, e):
        self.family.set('')

    def clear_filed(self, e):
        self.filde.set('')

    def clear_age(self, e):
        self.age.set('')
# screen text
    def text_screen(self):
        self.name = StringVar()
        self.txtname = Entry(self.screen, textvariable=self.name)
        self.txtname.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtname.place(x=300, y=50)
        self.name.set("Username")
        self.txtname.bind("<Button-1>", self.clear_name)

        self.family = StringVar()
        self.txtfamily = Entry(self.screen, textvariable=self.family)
        self.txtfamily.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfamily.place(x=300, y=100)
        self.family.set("Family")
        self.txtfamily.bind("<Button-1>", self.clear_family)

        self.filde = StringVar()
        self.txtfilde= Entry(self.screen, textvariable=self.filde)
        self.txtfilde.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfilde.place(x=300, y=150)
        self.filde.set("Filed")
        self.txtfilde.bind("<Button-1>", self.clear_filed)

        self.age = StringVar()
        self.txtage = Entry(self.screen, textvariable=self.age)
        self.txtage.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtage.place(x=300, y=200)
        self.age.set("Year")
        self.txtage.bind("<Button-1>", self.clear_age)

        # Button Screen

        btnscreen = Button(self.screen, text="Register", width=15, command=self.OneClickedRegister)
        btnscreen.configure(bg="green", fg="black", bd=3, justify="center")
        btnscreen.place(x=310, y=250)



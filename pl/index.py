from be.Register_User import Register_User
from tkinter import messagebox, ttk
from tkinter import *


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.text_screen()
        self.insert_table()

    # function

    # Register
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
            self.clear_table()
            self.insert_table()

        # clear

    def clear_name(self, e):
        if self.name.get() == "Username":
            self.name.set('')

    def clear_family(self, e):
        if self.family.get() == "Family":
            self.family.set('')

    def clear_filed(self, e):
        if self.filde.get() == "Filed":
            self.filde.set('')

    def clear_age(self, e):
        if self.age.get() == "Year":
            self.age.set('')

    # insert table

    def insert_table(self):
        r = Register_User(self.name.get(), self.family.get(), self.filde.get(), self.txtage.get())
        result = r.all_users()
        for item in result:
            self.table.insert("", "end", values=item)

    def clear_table(self):
        result = self.table.get_children()
        for item in result:
            sel = (str(item),)
            self.table.delete(sel)

    # screen text
    def text_screen(self):
        self.name = StringVar()
        self.txtname = Entry(self.screen, textvariable=self.name)
        self.txtname.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtname.place(x=100, y=70)
        self.name.set("Username")
        self.txtname.bind("<Button-1>", self.clear_name)

        self.family = StringVar()
        self.txtfamily = Entry(self.screen, textvariable=self.family)
        self.txtfamily.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfamily.place(x=100, y=120)
        self.family.set("Family")
        self.txtfamily.bind("<Button-1>", self.clear_family)

        self.filde = StringVar()
        self.txtfilde= Entry(self.screen, textvariable=self.filde)
        self.txtfilde.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtfilde.place(x=100, y=170)
        self.filde.set("Filed")
        self.txtfilde.bind("<Button-1>", self.clear_filed)

        self.age = StringVar()
        self.txtage = Entry(self.screen, textvariable=self.age)
        self.txtage.configure(bg="white", fg="black", bd=3, justify="center")
        self.txtage.place(x=100, y=220)
        self.age.set("Year")
        self.txtage.bind("<Button-1>", self.clear_age)

        # Button Screen

        # Register Button

        self.btnscreen = Button(self.screen, text="Register", width=15, command=self.OneClickedRegister)
        self.btnscreen.configure(bg="green", fg="black", bd=3, justify="center")
        self.btnscreen.place(x=110, y=270)


        # table

        self.table = ttk.Treeview(self.screen, columns=("Row", "Name", "Family", "Filed", "Age"), show="headings")

        self.table.heading("Name", text="Name")
        self.table.heading("Row", text="Row")
        self.table.heading("Family", text="Family")
        self.table.heading("Filed", text="Filed")
        self.table.heading("Age", text="Age")

        self.table.column("Row", anchor="center", width="50")
        self.table.column("Name", anchor="center", width="100")
        self.table.column("Family", anchor="center", width="100")
        self.table.column("Filed", anchor="center", width="100")
        self.table.column("Age", anchor="center", width="100")

        self.table.place(x=320, y=70)



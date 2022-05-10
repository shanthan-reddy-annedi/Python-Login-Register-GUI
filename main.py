import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ttkbootstrap as strap


class main(tk.Tk):

    def __init__(self):
        super(main, self).__init__()

        self.resizable(False, False)
        self.title("password Manager")
        # self.geometry("400x400")
        self.columnconfigure(0, weight=1)
        strap.Style()

        self.register_frame = Register(self)
        self.register_frame.grid(row=0, column=0, sticky="ewns")

        self.login_frame = Login(self)
        self.login_frame.grid(row=0, column=0, sticky="ewns")

        self.switch(Login)

    def switch(self, container):
        if container == Register:
            self.login_frame.grid_forget()
            self.register_frame.grid(row=0, column=0, sticky="ewns")

        else:
            self.register_frame.grid_forget()
            self.login_frame.grid(row=0, column=0, sticky="ewns")


class Login(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.user_name = tk.StringVar()
        self.user_password = tk.StringVar()

        self.img = ImageTk.PhotoImage(Image.open("user.png").resize((100, 100)))
        ttk.Label(self, image=self.img).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        username = ttk.Label(self, text="User Name:")
        password = ttk.Label(self, text="Password:")

        username_entry = ttk.Entry(self, textvariable=self.user_name, width=30)
        password_entry = ttk.Entry(self, textvariable=self.user_password, width=30)

        login_button = ttk.Button(self, text="Login", style="warning.TButton")
        register_button = ttk.Button(self, text="create account", style="success.TButton",
                                     command=lambda: master.switch(Register))

        # grid
        username.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        username_entry.grid(row=1, column=1, pady=20, padx=20)

        password.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        password_entry.grid(row=2, column=1, pady=20, padx=20)

        login_button.grid(row=3, column=1, pady=20, padx=20, sticky="e")
        register_button.grid(row=3, column=0, pady=20, padx=20)


class Register(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.img = ImageTk.PhotoImage(Image.open("user.png").resize((100, 100)))
        ttk.Button(self, text="back", command=lambda: master.switch(Login)).grid(row=0, column=0, sticky="w")
        ttk.Label(self, image=self.img).grid(row=1, column=0, columnspan=2)

        self.email = tk.StringVar()
        self.name = tk.StringVar()
        self.user_name = tk.StringVar()
        self.user_password = tk.StringVar()

        full_name = ttk.Label(self, text="Name:")
        email_id = ttk.Label(self, text="Email-Id:")
        username = ttk.Label(self, text="User Name:")
        password = ttk.Label(self, text="Password:")

        full_name_entry = ttk.Entry(self, textvariable=self.name, width=30)
        email_id_entry = ttk.Entry(self, textvariable=self.email, width=30)
        username_entry = ttk.Entry(self, textvariable=self.user_name, width=30)
        password_entry = ttk.Entry(self, textvariable=self.user_password, width=30)

        register_button = ttk.Button(self, text="create account", style="success.TButton")
        # grid
        full_name.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        full_name_entry.grid(row=2, column=1)

        email_id.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        email_id_entry.grid(row=3, column=1)

        username.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        username_entry.grid(row=4, column=1, pady=10, padx=20)

        password.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        password_entry.grid(row=5, column=1, pady=10, padx=20)

        register_button.grid(row=6, column=0, pady=10, padx=20, columnspan=2)


root = main()
root.mainloop()

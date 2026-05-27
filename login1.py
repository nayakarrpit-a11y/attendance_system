from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# =========================
# DATABASE CONNECTION
# =========================

def connect_database():

    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="1511",
        database="face"
    )

    return conn


# =========================
# REGISTER CLASS
# =========================

class Register:

    def __init__(self, root):

        self.root = root
        self.root.title("REGISTER SYSTEM")
        self.root.geometry("700x650+350+50")
        self.root.config(bg="#0f172a")

        # VARIABLES

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_confirmpass = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()

        # TITLE

        title = Label(
            self.root,
            text="NEW USER REGISTRATION",
            font=("Poppins", 24, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(pady=20)

        # MAIN FRAME

        frame = Frame(
            self.root,
            bg="#1e293b",
            bd=3,
            relief=RIDGE
        )

        frame.place(x=80, y=90, width=540, height=500)

        # FULL NAME

        Label(
            frame,
            text="FULL NAME",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=40)

        ttk.Entry(
            frame,
            textvariable=self.var_name,
            font=("Poppins", 12),
            width=28
        ).place(x=220, y=40)

        # EMAIL

        Label(
            frame,
            text="EMAIL",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=90)

        ttk.Entry(
            frame,
            textvariable=self.var_email,
            font=("Poppins", 12),
            width=28
        ).place(x=220, y=90)

        # USERNAME

        Label(
            frame,
            text="USERNAME",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=140)

        ttk.Entry(
            frame,
            textvariable=self.var_username,
            font=("Poppins", 12),
            width=28
        ).place(x=220, y=140)

        # PASSWORD

        Label(
            frame,
            text="PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=190)

        self.pass_entry = ttk.Entry(
            frame,
            textvariable=self.var_password,
            font=("Poppins", 12),
            show="*",
            width=28
        )

        self.pass_entry.place(x=220, y=190)

        # CONFIRM PASSWORD

        Label(
            frame,
            text="CONFIRM PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=240)

        self.confirm_entry = ttk.Entry(
            frame,
            textvariable=self.var_confirmpass,
            font=("Poppins", 12),
            show="*",
            width=28
        )

        self.confirm_entry.place(x=220, y=240)

        # SHOW PASSWORD

        self.show_pass = IntVar()

        Checkbutton(
            frame,
            text="Show Password",
            variable=self.show_pass,
            command=self.show_password,
            bg="#1e293b",
            fg="white",
            activebackground="#1e293b",
            activeforeground="white",
            selectcolor="#1e293b"
        ).place(x=220, y=270)

        # SECURITY QUESTION

        Label(
            frame,
            text="SECURITY QUESTION",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=310)

        self.combo_security_Q = ttk.Combobox(
            frame,
            textvariable=self.var_securityQ,
            font=("Poppins", 12),
            state="readonly",
            width=26
        )

        self.combo_security_Q["values"] = (
            "SELECT",
            "YOUR FAVOURITE COLOR?",
            "YOUR PET NAME?",
            "YOUR BIRTH PLACE?"
        )

        self.combo_security_Q.current(0)

        self.combo_security_Q.place(x=220, y=310)

        # SECURITY ANSWER

        Label(
            frame,
            text="SECURITY ANSWER",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).place(x=40, y=360)

        ttk.Entry(
            frame,
            textvariable=self.var_securityA,
            font=("Poppins", 12),
            width=28
        ).place(x=220, y=360)

        # TERMS CHECKBOX

        self.var_check = IntVar()

        Checkbutton(
            frame,
            text="I Agree Terms & Conditions",
            variable=self.var_check,
            bg="#1e293b",
            fg="#38bdf8",
            activebackground="#1e293b",
            activeforeground="#38bdf8",
            selectcolor="#1e293b"
        ).place(x=150, y=410)

        # REGISTER BUTTON

        Button(
            frame,
            text="REGISTER",
            command=self.register_data,
            font=("Poppins", 12, "bold"),
            bg="#38bdf8",
            fg="black",
            width=15,
            cursor="hand2"
        ).place(x=80, y=445)

        # RESET BUTTON

        Button(
            frame,
            text="RESET",
            command=self.reset_data,
            font=("Poppins", 12, "bold"),
            bg="#ef4444",
            fg="white",
            width=15,
            cursor="hand2"
        ).place(x=280, y=445)

    # =========================
    # SHOW PASSWORD
    # =========================

    def show_password(self):

        if self.show_pass.get() == 1:
            self.pass_entry.config(show="")
            self.confirm_entry.config(show="")
        else:
            self.pass_entry.config(show="*")
            self.confirm_entry.config(show="*")

    # =========================
    # REGISTER FUNCTION
    # =========================

    def register_data(self):

        if self.var_name.get() == "" or self.var_email.get() == "":

            messagebox.showerror(
                "ERROR",
                "ALL FIELDS ARE REQUIRED"
            )

        elif self.var_password.get() != self.var_confirmpass.get():

            messagebox.showerror(
                "ERROR",
                "PASSWORD NOT MATCH"
            )

        elif self.combo_security_Q.get() == "SELECT":

            messagebox.showerror(
                "ERROR",
                "PLEASE SELECT SECURITY QUESTION"
            )

        elif self.var_check.get() == 0:

            messagebox.showerror(
                "ERROR",
                "PLEASE AGREE TERMS & CONDITIONS"
            )

        else:

            try:

                conn = connect_database()

                my_cursor = conn.cursor()

                # CREATE TABLE

                my_cursor.execute("""
                CREATE TABLE IF NOT EXISTS register1(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    NAME VARCHAR(100),
                    EMAIL VARCHAR(100),
                    USERNAME VARCHAR(100),
                    PASSWORD VARCHAR(100),
                    SECURITYQ VARCHAR(200),
                    SECURITYA VARCHAR(200)
                )
                """)

                # CHECK USERNAME

                query = """
                SELECT * FROM register1
                WHERE USERNAME=%s
                """

                value = (
                    self.var_username.get(),
                )

                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row != None:

                    messagebox.showerror(
                        "ERROR",
                        "USERNAME ALREADY EXISTS"
                    )

                else:

                    query = """
                    INSERT INTO register1
                    (NAME, EMAIL, USERNAME, PASSWORD, SECURITYQ, SECURITYA)

                    VALUES (%s,%s,%s,%s,%s,%s)
                    """

                    value = (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_username.get(),
                        self.var_password.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get()
                    )

                    my_cursor.execute(query, value)

                    conn.commit()

                    conn.close()

                    messagebox.showinfo(
                        "SUCCESS",
                        "REGISTER SUCCESSFULLY"
                    )

                    self.root.destroy()

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # RESET FUNCTION
    # =========================

    def reset_data(self):

        self.var_name.set("")
        self.var_email.set("")
        self.var_username.set("")
        self.var_password.set("")
        self.var_confirmpass.set("")
        self.var_securityQ.set("SELECT")
        self.var_securityA.set("")
        self.var_check.set(0)


# =========================
# LOGIN CLASS
# =========================

class Login:

    def __init__(self, root):

        self.root = root
        self.root.title("FACE RECOGNITION LOGIN SYSTEM")
        self.root.geometry("900x500+250+100")
        self.root.config(bg="#0f172a")

        # TITLE

        title = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Poppins", 24, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(pady=20)

        # MAIN FRAME

        frame = Frame(
            self.root,
            bg="#1e293b",
            bd=3,
            relief=RIDGE
        )

        frame.place(x=220, y=120, width=450, height=350)

        # LOGIN TITLE

        Label(
            frame,
            text="LOGIN",
            font=("Poppins", 20, "bold"),
            bg="#1e293b",
            fg="white"
        ).pack(pady=10)

        # USERNAME

        Label(
            frame,
            text="USERNAME",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        ).pack()

        self.txtuser = ttk.Entry(
            frame,
            font=("Poppins", 12)
        )

        self.txtuser.pack(pady=10, ipadx=50)

        # PASSWORD

        Label(
            frame,
            text="PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        ).pack()

        self.txtpass = ttk.Entry(
            frame,
            font=("Poppins", 12),
            show="*"
        )

        self.txtpass.pack(pady=10, ipadx=50)

        # SHOW PASSWORD

        self.show_pass = IntVar()

        Checkbutton(
            frame,
            text="Show Password",
            variable=self.show_pass,
            command=self.show_password,
            bg="#1e293b",
            fg="white",
            activebackground="#1e293b",
            activeforeground="white",
            selectcolor="#1e293b"
        ).pack()

        # BUTTON FRAME

        btn_frame = Frame(
            frame,
            bg="#1e293b"
        )

        btn_frame.pack(pady=10)

        # LOGIN BUTTON

        Button(
            btn_frame,
            text="LOGIN",
            command=self.login,
            font=("Poppins", 12, "bold"),
            bg="#38bdf8",
            fg="black",
            width=12,
            cursor="hand2"
        ).grid(row=0, column=0, padx=10)

        # RESET BUTTON

        Button(
            btn_frame,
            text="RESET",
            command=self.reset_fields,
            font=("Poppins", 12, "bold"),
            bg="#ef4444",
            fg="white",
            width=12,
            cursor="hand2"
        ).grid(row=0, column=1, padx=10)

        # FORGOT PASSWORD BUTTON

        Button(
            frame,
            text="FORGOT PASSWORD?",
            command=self.forgot_password_window,
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=0,
            cursor="hand2"
        ).pack(pady=5)

        # REGISTER BUTTON

        Button(
            frame,
            text="NEW USER REGISTER",
            command=self.register_window,
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=0,
            cursor="hand2"
        ).pack()

    # =========================
    # SHOW PASSWORD
    # =========================

    def show_password(self):

        if self.show_pass.get() == 1:
            self.txtpass.config(show="")
        else:
            self.txtpass.config(show="*")

    # =========================
    # LOGIN FUNCTION
    # =========================

    def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":

            messagebox.showerror(
                "ERROR",
                "ALL FIELDS ARE REQUIRED"
            )

        else:

            try:

                conn = connect_database()

                my_cursor = conn.cursor()

                query = """
                SELECT * FROM register1
                WHERE USERNAME=%s AND PASSWORD=%s
                """

                value = (
                    self.txtuser.get(),
                    self.txtpass.get()
                )

                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row == None:

                    messagebox.showerror(
                        "ERROR",
                        "INVALID USERNAME OR PASSWORD"
                    )

                else:

                    messagebox.showinfo(
                        "SUCCESS",
                        "LOGIN SUCCESSFULLY"
                    )

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # RESET FUNCTION
    # =========================

    def reset_fields(self):

        self.txtuser.delete(0, END)
        self.txtpass.delete(0, END)

    # =========================
    # REGISTER WINDOW
    # =========================

    def register_window(self):

        self.new_window = Toplevel(self.root)

        Register(self.new_window)

    # =========================
    # FORGOT PASSWORD WINDOW
    # =========================

    def forgot_password_window(self):

        if self.txtuser.get() == "":

            messagebox.showerror(
                "ERROR",
                "PLEASE ENTER USERNAME"
            )

            return

        self.root2 = Toplevel()

        self.root2.title("FORGOT PASSWORD")

        self.root2.geometry("450x450+500+150")

        self.root2.config(bg="#0f172a")

        title = Label(
            self.root2,
            text="RESET PASSWORD",
            font=("Poppins", 20, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(pady=20)

        # SECURITY QUESTION

        Label(
            self.root2,
            text="SECURITY QUESTION",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        self.combo_security_Q = ttk.Combobox(
            self.root2,
            font=("Poppins", 12),
            state="readonly",
            width=30
        )

        self.combo_security_Q["values"] = (
            "SELECT",
            "YOUR FAVOURITE COLOR?",
            "YOUR PET NAME?",
            "YOUR BIRTH PLACE?"
        )

        self.combo_security_Q.current(0)

        self.combo_security_Q.pack(pady=10)

        # SECURITY ANSWER

        Label(
            self.root2,
            text="SECURITY ANSWER",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        self.txt_security = ttk.Entry(
            self.root2,
            font=("Poppins", 12),
            width=32
        )

        self.txt_security.pack(pady=10)

        # NEW PASSWORD

        Label(
            self.root2,
            text="NEW PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack()

        self.txt_newpass = ttk.Entry(
            self.root2,
            font=("Poppins", 12),
            width=32,
            show="*"
        )

        self.txt_newpass.pack(pady=10)

        # SHOW PASSWORD

        self.show_new_pass = IntVar()

        Checkbutton(
            self.root2,
            text="Show Password",
            variable=self.show_new_pass,
            command=self.show_new_password,
            bg="#0f172a",
            fg="white",
            activebackground="#0f172a",
            activeforeground="white",
            selectcolor="#0f172a"
        ).pack()

        # RESET BUTTON

        Button(
            self.root2,
            text="RESET PASSWORD",
            command=self.reset_pass,
            font=("Poppins", 12, "bold"),
            bg="#38bdf8",
            fg="black",
            cursor="hand2"
        ).pack(pady=20)

    # =========================
    # SHOW NEW PASSWORD
    # =========================

    def show_new_password(self):

        if self.show_new_pass.get() == 1:
            self.txt_newpass.config(show="")
        else:
            self.txt_newpass.config(show="*")

    # =========================
    # RESET PASSWORD FUNCTION
    # =========================

    def reset_pass(self):

        if self.combo_security_Q.get() == "SELECT":

            messagebox.showerror(
                "ERROR",
                "SELECT SECURITY QUESTION",
                parent=self.root2
            )

        elif self.txt_security.get() == "":

            messagebox.showerror(
                "ERROR",
                "ENTER SECURITY ANSWER",
                parent=self.root2
            )

        elif self.txt_newpass.get() == "":

            messagebox.showerror(
                "ERROR",
                "ENTER NEW PASSWORD",
                parent=self.root2
            )

        else:

            try:

                conn = connect_database()

                my_cursor = conn.cursor()

                query = """
                SELECT * FROM register1
                WHERE USERNAME=%s
                AND SECURITYQ=%s
                AND SECURITYA=%s
                """

                value = (
                    self.txtuser.get(),
                    self.combo_security_Q.get(),
                    self.txt_security.get()
                )

                my_cursor.execute(query, value)

                row = my_cursor.fetchone()

                if row == None:

                    messagebox.showerror(
                        "ERROR",
                        "INVALID SECURITY ANSWER",
                        parent=self.root2
                    )

                else:

                    query = """
                    UPDATE register1
                    SET PASSWORD=%s
                    WHERE USERNAME=%s
                    """

                    value = (
                        self.txt_newpass.get(),
                        self.txtuser.get()
                    )

                    my_cursor.execute(query, value)

                    conn.commit()

                    messagebox.showinfo(
                        "SUCCESS",
                        "PASSWORD RESET SUCCESSFULLY",
                        parent=self.root2
                    )

                    self.root2.destroy()

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Login(root)

    root.mainloop()
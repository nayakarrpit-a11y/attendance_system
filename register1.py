from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# =========================
# REGISTER CLASS
# =========================

class Register:

    def __init__(self, root):

        self.root = root

        self.root.title("REGISTER SYSTEM")

        self.root.geometry("950x650+200+50")

        self.root.config(bg="#0f172a")

        # =========================
        # VARIABLES
        # =========================

        self.var_name = StringVar()

        self.var_email = StringVar()

        self.var_username = StringVar()

        self.var_password = StringVar()

        self.var_confirmpass = StringVar()

        self.var_securityQ = StringVar()

        self.var_securityA = StringVar()

        # =========================
        # TITLE
        # =========================

        title = Label(
            self.root,
            text="NEW USER REGISTRATION",
            font=("Poppins", 26, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(pady=20)

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = Frame(
            self.root,
            bg="#1e293b",
            bd=3,
            relief=RIDGE
        )

        main_frame.place(x=350, y=130, width=600, height=480)

        # =========================
        # NAME
        # =========================

        name_lbl = Label(
            main_frame,
            text="FULL NAME",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        name_lbl.place(x=40, y=40)

        name_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_name,
            font=("Poppins", 12),
            width=28
        )

        name_entry.place(x=250, y=40)

        # =========================
        # EMAIL
        # =========================

        email_lbl = Label(
            main_frame,
            text="EMAIL",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        email_lbl.place(x=40, y=90)

        email_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_email,
            font=("Poppins", 12),
            width=28
        )

        email_entry.place(x=250, y=90)

        # =========================
        # USERNAME
        # =========================

        user_lbl = Label(
            main_frame,
            text="USERNAME",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        user_lbl.place(x=40, y=140)

        user_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_username,
            font=("Poppins", 12),
            width=28
        )

        user_entry.place(x=250, y=140)

        # =========================
        # PASSWORD
        # =========================

        pass_lbl = Label(
            main_frame,
            text="PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        pass_lbl.place(x=40, y=190)

        pass_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_password,
            font=("Poppins", 12),
            show="*",
            width=28
        )

        pass_entry.place(x=250, y=190)

        # =========================
        # CONFIRM PASSWORD
        # =========================

        conf_lbl = Label(
            main_frame,
            text="CONFIRM PASSWORD",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        conf_lbl.place(x=40, y=240)

        conf_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_confirmpass,
            font=("Poppins", 12),
            show="*",
            width=28
        )

        conf_entry.place(x=250, y=240)

        # =========================
        # SECURITY QUESTION
        # =========================

        sec_lbl = Label(
            main_frame,
            text="SECURITY QUESTION",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        sec_lbl.place(x=40, y=290)

        self.combo_security_Q = ttk.Combobox(
            main_frame,
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

        self.combo_security_Q.place(x=250, y=290)

        # =========================
        # SECURITY ANSWER
        # =========================

        answer_lbl = Label(
            main_frame,
            text="SECURITY ANSWER",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        answer_lbl.place(x=40, y=340)

        answer_entry = ttk.Entry(
            main_frame,
            textvariable=self.var_securityA,
            font=("Poppins", 12),
            width=28
        )

        answer_entry.place(x=250, y=340)

        # =========================
        # TERMS CHECKBOX
        # =========================

        self.var_check = IntVar()

        checkbtn = Checkbutton(
            main_frame,
            text="I AGREE THE TERMS & CONDITIONS",
            variable=self.var_check,
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            activebackground="#1e293b",
            activeforeground="#38bdf8",
            selectcolor="#1e293b"
        )

        checkbtn.place(x=150, y=390)

        # =========================
        # BUTTON FRAME
        # =========================

        btn_frame = Frame(
            main_frame,
            bg="#1e293b"
        )

        btn_frame.place(x=120, y=430)

        # REGISTER BUTTON

        register_btn = Button(
            btn_frame,
            text="REGISTER",
            command=self.register_data,
            font=("Poppins", 12, "bold"),
            bg="#38bdf8",
            fg="black",
            width=15,
            cursor="hand2"
        )

        register_btn.grid(row=0, column=0, padx=10)

        # RESET BUTTON

        reset_btn = Button(
            btn_frame,
            text="RESET",
            command=self.reset_data,
            font=("Poppins", 12, "bold"),
            bg="#ef4444",
            fg="white",
            width=15,
            cursor="hand2"
        )

        reset_btn.grid(row=0, column=1, padx=10)

    # =========================
    # REGISTER FUNCTION
    # =========================

    def register_data(self):

        if self.var_name.get() == "" or self.var_email.get() == "":

            messagebox.showerror(
                "ERROR",
                "ALL FIELDS ARE REQUIRED",
                parent=self.root
            )

        elif self.var_password.get() != self.var_confirmpass.get():

            messagebox.showerror(
                "ERROR",
                "PASSWORD & CONFIRM PASSWORD MUST BE SAME",
                parent=self.root
            )

        elif self.combo_security_Q.get() == "SELECT":

            messagebox.showerror(
                "ERROR",
                "PLEASE SELECT SECURITY QUESTION",
                parent=self.root
            )

        elif self.var_check.get() == 0:

            messagebox.showerror(
                "ERROR",
                "PLEASE AGREE TERMS & CONDITIONS",
                parent=self.root
            )

        else:

            try:

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="1511",
                    database="face"
                )

                my_cursor = conn.cursor()

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
                        "USERNAME ALREADY EXISTS",
                        parent=self.root
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
                        "REGISTER SUCCESSFULLY",
                        parent=self.root
                    )

                    self.reset_data()

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"DUE TO : {str(es)}",
                    parent=self.root
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
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Register(root)

    root.mainloop()
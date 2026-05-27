from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
from datetime import datetime
import os
from student1 import Student

# =========================
# MAIN DASHBOARD CLASS
# =========================

class Face_Recognition_System:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1530x790+0+0")

        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

        self.root.config(bg="#0f172a")

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Poppins", 30, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title_lbl.pack(side=TOP, fill=X)

        # =========================
        # DATE & TIME
        # =========================

        self.time_lbl = Label(
            self.root,
            font=("Poppins", 14, "bold"),
            bg="#1e293b",
            fg="white"
        )

        self.time_lbl.pack(fill=X)

        self.update_time()

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = Frame(
            self.root,
            bg="#0f172a"
        )

        main_frame.place(x=0, y=80, width=1230, height=710)

        # =========================
        # DASHBOARD TITLE
        # =========================

        dashboard_lbl = Label(
            main_frame,
            text="MAIN DASHBOARD",
            font=("Poppins", 24, "bold"),
            bg="#0f172a",
            fg="white"
        )

        dashboard_lbl.pack(pady=20)

        # =========================
        # BUTTONS
        # =========================

        button_data = [

            ("STUDENT DETAILS", self.student_details),

            ("TRAIN DATA", self.train_data),

            ("FACE RECOGNITION", self.face_recognition),

            ("ATTENDANCE", self.attendance_data),

            ("ATTENDANCE REPORT", self.attendancereport_data),

            ("PHOTOS", self.open_photos),

            ("DEVELOPER", self.developer_data),

            ("CHATBOT", self.chatbot_data),

            ("EXIT", self.iExit)

        ]

        # =========================
        # BUTTON FRAME
        # =========================

        btn_frame = Frame(
            main_frame,
            bg="#0f172a"
        )

        btn_frame.pack(pady=30)

        row = 0
        col = 0

        for text, command in button_data:

            btn = Button(
                btn_frame,
                text=text,
                command=command,
                cursor="hand2",
                font=("Poppins", 14, "bold"),
                bg="#1e293b",
                fg="white",
                activebackground="#38bdf8",
                activeforeground="black",
                width=22,
                height=4,
                bd=3,
                relief=RIDGE
            )

            btn.grid(row=row, column=col, padx=20, pady=20)

            col += 1

            if col > 2:
                col = 0
                row += 1

        # =========================
        # FOOTER
        # =========================

        footer_lbl = Label(
            self.root,
            text="BCA SEMESTER 6 PROJECT | FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8"
        )

        footer_lbl.pack(side=BOTTOM, fill=X)

    # =========================
    # LIVE TIME FUNCTION
    # =========================

    def update_time(self):

        current_time = time.strftime("%H:%M:%S")

        current_date = datetime.now().strftime("%d-%m-%Y")

        self.time_lbl.config(
            text=f"DATE : {current_date}        TIME : {current_time}"
        )

        self.time_lbl.after(1000, self.update_time)

    # =========================
    # STUDENT DETAILS
    # =========================

    def student_details(self):

        try:

            from student1 import Student

            self.new_window = Toplevel(self.root)

            self.app = Student(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # TRAIN DATA
    # =========================

    def train_data(self):

        try:

            from train1 import Train

            self.new_window = Toplevel(self.root)

            self.app = Train(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # FACE RECOGNITION
    # =========================

    def face_recognition(self):

        try:

            from face_recognition1 import Face_Recognition

            self.new_window = Toplevel(self.root)

            self.app = Face_Recognition(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # ATTENDANCE
    # =========================

    def attendance_data(self):

        try:

            from attendance1 import Attendance

            self.new_window = Toplevel(self.root)

            self.app = Attendance(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )
    
    # =========================
    # ATTENDANCE REPORT
    # =========================

    def attendancereport_data(self):

        try:

            from report import Attendance

            self.new_window = Toplevel(self.root)

            self.app = Attendance(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # OPEN PHOTOS
    # =========================

    def open_photos(self):

        folder_path = "gallery1"

        # Create folder automatically

        if not os.path.exists(folder_path):

            os.makedirs(folder_path)

            messagebox.showinfo(
                "FOLDER CREATED",
                "gallery1 folder created successfully"
            )

        try:

            os.startfile(folder_path)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"Cannot Open Folder\n\n{str(es)}"
            )
    # =========================
    # DEVELOPER
    # =========================

    def developer_data(self):

        try:

            from developer1 import Developer

            self.new_window = Toplevel(self.root)

            self.app = Developer(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # CHATBOT
    # =========================

    def chatbot_data(self):

        try:

            from chatbot1 import ChatBot

            self.new_window = Toplevel(self.root)

            self.app = ChatBot(self.new_window)

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # EXIT SYSTEM
    # =========================

    def iExit(self):

        self.iExit = messagebox.askyesno(
            "FACE RECOGNITION",
            "ARE YOU SURE YOU WANT TO EXIT?",
            parent=self.root
        )

        if self.iExit > 0:

            self.root.destroy()

        else:

            return

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Face_Recognition_System(root)

    root.mainloop()
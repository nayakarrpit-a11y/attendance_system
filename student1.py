from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
import numpy as np
from datetime import datetime
import threading

# =========================
# STUDENT CLASS
# =========================

class Student:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1530x790+0+0")

        self.root.title("STUDENT MANAGEMENT SYSTEM")

        self.root.config(bg="#0f172a")

        # =========================
        # VARIABLES
        # =========================

        self.var_DEP = StringVar()
        self.var_COURSE = StringVar()
        self.var_YEAR = StringVar()
        self.var_SEMESTER = StringVar()

        self.var_STD_ID = StringVar()
        self.var_STD_NAME = StringVar()
        self.var_DIV = StringVar()
        self.var_ROLL = StringVar()
        self.var_GENDER = StringVar()
        self.var_DOB = StringVar()
        self.var_EMAIL = StringVar()
        self.var_PHONE = StringVar()
        self.var_ADDRESS = StringVar()
        self.var_TEACHER = StringVar()

        self.var_radio1 = StringVar()

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("Poppins", 28, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title_lbl.pack(fill=X)

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = Frame(
            self.root,
            bg="#1e293b",
            bd=3,
            relief=RIDGE
        )

        main_frame.place(x=10, y=60, width=1270, height=580)

        # =========================
        # LEFT FRAME
        # =========================

        left_frame = LabelFrame(
            main_frame,
            text="STUDENT DETAILS",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=3,
            relief=RIDGE
        )

        left_frame.place(x=10, y=10, width=620, height=560)

        # =========================
        # CURRENT COURSE
        # =========================

        current_course_frame = LabelFrame(
            left_frame,
            text="CURRENT COURSE INFORMATION",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        current_course_frame.place(x=10, y=10, width=590, height=120)

        # Department

        dep_label = Label(
            current_course_frame,
            text="Department",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        )

        dep_label.grid(row=0, column=0, padx=10, pady=10)

        dep_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_DEP,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        dep_combo["values"] = (
            "SELECT DEPARTMENT",
            "IT",
            "COMPUTER SCIENCE",
            "BCA",
            "MCA",
            "BBA"
        )

        dep_combo.current(0)

        dep_combo.grid(row=0, column=1)

        # Course

        course_label = Label(
            current_course_frame,
            text="Course",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        )

        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_COURSE,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        course_combo["values"] = (
            "SELECT COURSE",
            "FYBCA",
            "SYBCA",
            "TYBCA"
        )

        course_combo.current(0)

        course_combo.grid(row=0, column=3)

        # Year

        year_label = Label(
            current_course_frame,
            text="Year",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        )

        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_YEAR,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        year_combo["values"] = (
            "SELECT YEAR",
            "2023-24",
            "2024-25",
            "2025-26"
        )

        year_combo.current(0)

        year_combo.grid(row=1, column=1)

        # Semester

        sem_label = Label(
            current_course_frame,
            text="Semester",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        )

        sem_label.grid(row=1, column=2)

        sem_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_SEMESTER,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        sem_combo["values"] = (
            "SELECT SEMESTER",
            "SEM-1",
            "SEM-2",
            "SEM-3",
            "SEM-4",
            "SEM-5",
            "SEM-6"
        )

        sem_combo.current(0)

        sem_combo.grid(row=1, column=3)

        # =========================
        # STUDENT INFORMATION
        # =========================

        class_frame = LabelFrame(
            left_frame,
            text="CLASS STUDENT INFORMATION",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        class_frame.place(x=10, y=140, width=590, height=380)

        # Student ID

        Label(
            class_frame,
            text="Student ID",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=8, sticky=W)

        ttk.Entry(
            class_frame,
            textvariable=self.var_STD_ID,
            width=20,
            font=("Poppins", 10)
        ).grid(row=0, column=1)

        # Student Name

        Label(
            class_frame,
            text="Student Name",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=2)

        ttk.Entry(
            class_frame,
            textvariable=self.var_STD_NAME,
            width=20,
            font=("Poppins", 10)
        ).grid(row=0, column=3)

        # Division

        Label(
            class_frame,
            text="Division",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=1, column=0, padx=10, pady=8)

        div_combo = ttk.Combobox(
            class_frame,
            textvariable=self.var_DIV,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        div_combo["values"] = (
            "SELECT DIVISION",
            "A",
            "B",
            "C"
        )

        div_combo.current(0)

        div_combo.grid(row=1, column=1)

        # Roll

        Label(
            class_frame,
            text="Roll No",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=1, column=2)

        ttk.Entry(
            class_frame,
            textvariable=self.var_ROLL,
            width=20,
            font=("Poppins", 10)
        ).grid(row=1, column=3)

        # Gender

        Label(
            class_frame,
            text="Gender",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=2, column=0, padx=10, pady=8)

        gender_combo = ttk.Combobox(
            class_frame,
            textvariable=self.var_GENDER,
            font=("Poppins", 10),
            state="readonly",
            width=18
        )

        gender_combo["values"] = (
            "SELECT GENDER",
            "MALE",
            "FEMALE",
            "OTHER"
        )

        gender_combo.current(0)

        gender_combo.grid(row=2, column=1)

        # DOB

        Label(
            class_frame,
            text="DOB",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=2, column=2)

        ttk.Entry(
            class_frame,
            textvariable=self.var_DOB,
            width=20,
            font=("Poppins", 10)
        ).grid(row=2, column=3)

        # Email

        Label(
            class_frame,
            text="Email",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=3, column=0, padx=10, pady=8)

        ttk.Entry(
            class_frame,
            textvariable=self.var_EMAIL,
            width=20,
            font=("Poppins", 10)
        ).grid(row=3, column=1)

        # Phone

        Label(
            class_frame,
            text="Phone",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=3, column=2)

        ttk.Entry(
            class_frame,
            textvariable=self.var_PHONE,
            width=20,
            font=("Poppins", 10)
        ).grid(row=3, column=3)

        # Address

        Label(
            class_frame,
            text="Address",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=4, column=0, padx=10, pady=8)

        ttk.Entry(
            class_frame,
            textvariable=self.var_ADDRESS,
            width=20,
            font=("Poppins", 10)
        ).grid(row=4, column=1)

        # Teacher

        Label(
            class_frame,
            text="Teacher",
            font=("Poppins", 10, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=4, column=2)

        ttk.Entry(
            class_frame,
            textvariable=self.var_TEACHER,
            width=20,
            font=("Poppins", 10)
        ).grid(row=4, column=3)

        # RADIO BUTTONS

        ttk.Radiobutton(
            class_frame,
            text="Take Photo Sample",
            variable=self.var_radio1,
            value="Yes"
        ).grid(row=5, column=0, pady=15)

        ttk.Radiobutton(
            class_frame,
            text="No Photo Sample",
            variable=self.var_radio1,
            value="No"
        ).grid(row=5, column=1)

        # =========================
        # BUTTON FRAME
        # =========================

        btn_frame = Frame(
            class_frame,
            bg="#1e293b"
        )

        btn_frame.place(x=10, y=250, width=570, height=100)

        Button(
            btn_frame,
            text="SAVE",
            command=self.add_data,
            font=("Poppins", 10, "bold"),
            bg="#38bdf8",
            fg="black",
            width=15
        ).grid(row=0, column=0, padx=5, pady=10)

        Button(
            btn_frame,
            text="UPDATE",
            command=self.update_data,
            font=("Poppins", 10, "bold"),
            bg="#22c55e",
            fg="black",
            width=15
        ).grid(row=0, column=1, padx=5)

        Button(
            btn_frame,
            text="DELETE",
            command=self.delete_data,
            font=("Poppins", 10, "bold"),
            bg="#ef4444",
            fg="white",
            width=15
        ).grid(row=0, column=2, padx=5)

        Button(
            btn_frame,
            text="RESET",
            command=self.reset_data,
            font=("Poppins", 10, "bold"),
            bg="#f59e0b",
            fg="black",
            width=15
        ).grid(row=0, column=3, padx=5)

        Button(
            btn_frame,
            text="TAKE PHOTO SAMPLE",
            command=self.generate_dataset,
            font=("Poppins", 10, "bold"),
            bg="#8b5cf6",
            fg="white",
            width=30
        ).grid(row=1, column=0, columnspan=2, pady=10)

        Button(
            btn_frame,
            text="UPDATE PHOTO SAMPLE",
            command=self.generate_dataset,
            font=("Poppins", 10, "bold"),
            bg="#06b6d4",
            fg="black",
            width=30
        ).grid(row=1, column=2, columnspan=2)

        # =========================
        # RIGHT FRAME
        # =========================

        right_frame = LabelFrame(
            main_frame,
            text="STUDENT DATABASE",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=3,
            relief=RIDGE
        )

        right_frame.place(x=640, y=10, width=610, height=560)

        # SEARCH FRAME

        search_frame = LabelFrame(
            right_frame,
            text="SEARCH SYSTEM",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )

        search_frame.place(x=10, y=10, width=580, height=80)

        Label(
            search_frame,
            text="Search By",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        self.search_combo = ttk.Combobox(
            search_frame,
            font=("Poppins", 10),
            state="readonly",
            width=15
        )

        self.search_combo["values"] = (
            "SELECT",
            "ROLL",
            "PHONE"
        )

        self.search_combo.current(0)

        self.search_combo.grid(row=0, column=1)

        self.search_entry = ttk.Entry(
            search_frame,
            width=15,
            font=("Poppins", 10)
        )

        self.search_entry.grid(row=0, column=2, padx=10)

        Button(
            search_frame,
            text="SEARCH",
            command=self.search_data,
            font=("Poppins", 10, "bold"),
            bg="#38bdf8",
            fg="black",
            width=11
        ).grid(row=0, column=3, padx=5)

        Button(
            search_frame,
            text="SHOW ALL",
            command=self.fetch_data,
            font=("Poppins", 10, "bold"),
            bg="#22c55e",
            fg="black",
            width=11
        ).grid(row=0, column=4)

        # =========================
        # TABLE FRAME
        # =========================

        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE
        )

        table_frame.place(x=10, y=100, width=580, height=430)

        scroll_x = ttk.Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        scroll_y = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        headings = [

            ("dep", "Department"),
            ("course", "Course"),
            ("year", "Year"),
            ("sem", "Semester"),
            ("id", "Student ID"),
            ("name", "Name"),
            ("div", "Division"),
            ("roll", "Roll"),
            ("gender", "Gender"),
            ("dob", "DOB"),
            ("email", "Email"),
            ("phone", "Phone"),
            ("address", "Address"),
            ("teacher", "Teacher"),
            ("photo", "Photo")

        ]

        for col, text in headings:

            self.student_table.heading(col, text=text)

            self.student_table.column(col, width=120)

        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind(
            "<ButtonRelease>",
            self.get_cursor
        )

        self.fetch_data()

    # =========================
    # DATABASE CONNECTION
    # =========================

    def connect_db(self):

        return mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

    # =========================
    # ADD DATA
    # =========================

    def add_data(self):

        if self.var_DEP.get() == "SELECT DEPARTMENT" or self.var_STD_NAME.get() == "":

            messagebox.showerror(
                "ERROR",
                "ALL FIELDS ARE REQUIRED"
            )

        else:

            try:

                conn = self.connect_db()

                my_cursor = conn.cursor()

                my_cursor.execute(
                    """
                    INSERT INTO student1
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        self.var_DEP.get(),
                        self.var_COURSE.get(),
                        self.var_YEAR.get(),
                        self.var_SEMESTER.get(),
                        self.var_STD_ID.get(),
                        self.var_STD_NAME.get(),
                        self.var_DIV.get(),
                        self.var_ROLL.get(),
                        self.var_GENDER.get(),
                        self.var_DOB.get(),
                        self.var_EMAIL.get(),
                        self.var_PHONE.get(),
                        self.var_ADDRESS.get(),
                        self.var_TEACHER.get(),
                        self.var_radio1.get()
                    )
                )

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "SUCCESS",
                    "STUDENT DETAILS ADDED SUCCESSFULLY"
                )

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # FETCH DATA
    # =========================

    def fetch_data(self):

        conn = self.connect_db()

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM student1")

        data = my_cursor.fetchall()

        if len(data) != 0:

            self.student_table.delete(
                *self.student_table.get_children()
            )

            for i in data:

                self.student_table.insert(
                    "",
                    END,
                    values=i
                )

            conn.commit()

        conn.close()

    # =========================
    # GET CURSOR
    # =========================

    def get_cursor(self, event=""):

        cursor_focus = self.student_table.focus()

        content = self.student_table.item(cursor_focus)

        data = content["values"]

        if len(data) == 0:
            return

        self.var_DEP.set(data[0])
        self.var_COURSE.set(data[1])
        self.var_YEAR.set(data[2])
        self.var_SEMESTER.set(data[3])
        self.var_STD_ID.set(data[4])
        self.var_STD_NAME.set(data[5])
        self.var_DIV.set(data[6])
        self.var_ROLL.set(data[7])
        self.var_GENDER.set(data[8])
        self.var_DOB.set(data[9])
        self.var_EMAIL.set(data[10])
        self.var_PHONE.set(data[11])
        self.var_ADDRESS.set(data[12])
        self.var_TEACHER.set(data[13])
        self.var_radio1.set(data[14])

    # =========================
    # UPDATE DATA
    # =========================

    def update_data(self):

        if self.var_STD_ID.get() == "":

            messagebox.showerror(
                "ERROR",
                "STUDENT ID REQUIRED"
            )

        else:

            try:

                conn = self.connect_db()

                my_cursor = conn.cursor()

                my_cursor.execute(
                    """
                    UPDATE student1 SET
                    DEP=%s,
                    COURSE=%s,
                    YEAR=%s,
                    SEMESTER=%s,
                    NAME=%s,
                    DIVISION=%s,
                    ROLL=%s,
                    GENDER=%s,
                    DOB=%s,
                    EMAIL=%s,
                    PHONE=%s,
                    ADDRESS=%s,
                    TEACHER=%s,
                    PHOTOSAMPLE=%s
                    WHERE STD_ID=%s
                    """,
                    (
                        self.var_DEP.get(),
                        self.var_COURSE.get(),
                        self.var_YEAR.get(),
                        self.var_SEMESTER.get(),
                        self.var_STD_NAME.get(),
                        self.var_DIV.get(),
                        self.var_ROLL.get(),
                        self.var_GENDER.get(),
                        self.var_DOB.get(),
                        self.var_EMAIL.get(),
                        self.var_PHONE.get(),
                        self.var_ADDRESS.get(),
                        self.var_TEACHER.get(),
                        self.var_radio1.get(),
                        self.var_STD_ID.get()
                    )
                )

                conn.commit()

                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "SUCCESS",
                    "STUDENT UPDATED SUCCESSFULLY"
                )

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # DELETE DATA
    # =========================

    def delete_data(self):

        if self.var_STD_ID.get() == "":

            messagebox.showerror(
                "ERROR",
                "STUDENT ID REQUIRED"
            )

        else:

            try:

                delete = messagebox.askyesno(
                    "DELETE",
                    "DO YOU WANT TO DELETE?"
                )

                if delete > 0:

                    conn = self.connect_db()

                    my_cursor = conn.cursor()

                    sql = "DELETE FROM student1 WHERE STD_ID=%s"

                    val = (self.var_STD_ID.get(),)

                    my_cursor.execute(sql, val)

                    conn.commit()

                    self.fetch_data()

                    conn.close()

                    messagebox.showinfo(
                        "DELETE",
                        "STUDENT DELETED SUCCESSFULLY"
                    )

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # RESET DATA
    # =========================

    def reset_data(self):

        self.var_DEP.set("SELECT DEPARTMENT")
        self.var_COURSE.set("SELECT COURSE")
        self.var_YEAR.set("SELECT YEAR")
        self.var_SEMESTER.set("SELECT SEMESTER")

        self.var_STD_ID.set("")
        self.var_STD_NAME.set("")
        self.var_DIV.set("SELECT DIVISION")
        self.var_ROLL.set("")
        self.var_GENDER.set("SELECT GENDER")
        self.var_DOB.set("")
        self.var_EMAIL.set("")
        self.var_PHONE.set("")
        self.var_ADDRESS.set("")
        self.var_TEACHER.set("")
        self.var_radio1.set("")

    # =========================
    # SEARCH DATA
    # =========================

    def search_data(self):

        if self.search_combo.get() == "SELECT":

            messagebox.showerror(
                "ERROR",
                "SELECT SEARCH OPTION"
            )

        else:

            try:

                conn = self.connect_db()

                my_cursor = conn.cursor()

                query = f"""
                SELECT * FROM student1
                WHERE {self.search_combo.get()} LIKE '%{self.search_entry.get()}%'
                """

                my_cursor.execute(query)

                rows = my_cursor.fetchall()

                if len(rows) != 0:

                    self.student_table.delete(
                        *self.student_table.get_children()
                    )

                    for i in rows:

                        self.student_table.insert(
                            "",
                            END,
                            values=i
                        )

                else:

                    messagebox.showerror(
                        "ERROR",
                        "NO DATA FOUND"
                    )

                conn.commit()

                conn.close()

            except Exception as es:

                messagebox.showerror(
                    "ERROR",
                    f"{str(es)}"
                )

    # =========================
    # GENERATE DATASET
    # =========================

    def generate_dataset(self):

        if self.var_STD_ID.get() == "" or self.var_STD_NAME.get() == "":

            messagebox.showerror(
                "ERROR",
                "STUDENT DETAILS REQUIRED"
            )

            return

        if self.var_radio1.get() != "Yes":

            messagebox.showerror(
                "ERROR",
                "PLEASE SELECT TAKE PHOTO SAMPLE"
            )

            return

        try:
            

            face_classifier = cv2.CascadeClassifier(
                cv2.data.haarcascades +
                "haarcascade_frontalface_default.xml"
            )

            def face_cropped(img):

                gray = cv2.cvtColor(
                    img,
                    cv2.COLOR_BGR2GRAY
                )

                faces = face_classifier.detectMultiScale(
                    gray,
                    1.3,
                    5
                )

                for (x, y, w, h) in faces:

                    face_cropped = img[y:y+h, x:x+w]

                    return face_cropped

            cap = cv2.VideoCapture(0)

            img_id = 0

            if not os.path.exists("gallery1"):

                os.makedirs("gallery1")

            while True:

                ret, my_frame = cap.read()

                if face_cropped(my_frame) is not None:

                    img_id += 1

                    face = cv2.resize(
                        face_cropped(my_frame),
                        (450, 450)
                    )

                    face = cv2.cvtColor(
                        face,
                        cv2.COLOR_BGR2GRAY
                    )

                    file_name_path = (
                        "gallery1/user."
                        + str(self.var_STD_ID.get())
                        + "."
                        + str(img_id)
                        + ".jpg"
                    )

                    cv2.imwrite(
                        file_name_path,
                        face
                    )

                    cv2.putText(
                        face,
                        f"IMAGE {img_id}/20",
                        (50, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

                    cv2.imshow(
                        "FACE CROP",
                        face
                    )

                if cv2.waitKey(1) == 13 or int(img_id) == 20:

                    break

            cap.release()

            cv2.destroyAllWindows()

            self.fetch_data()

            messagebox.showinfo(
                "RESULT",
                "DATASET GENERATED SUCCESSFULLY"
            )

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

    obj = Student(root)

    root.mainloop()
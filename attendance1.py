from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import csv
import os
from datetime import datetime
import mysql.connector

# =========================
# ATTENDANCE CLASS
# =========================

class Attendance:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1530x790+0+0")

        self.root.title("ATTENDANCE MANAGEMENT SYSTEM")

        self.root.config(bg="#0f172a")

        # =========================
        # DATABASE CONNECTION
        # =========================

        try:

            self.conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="1511",
                database="face"
            )

            self.my_cursor = self.conn.cursor()

            # =========================
            # CREATE TABLE
            # =========================

            self.my_cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance1(

                Attendance_ID VARCHAR(50) PRIMARY KEY,
                Roll VARCHAR(50),
                Name VARCHAR(100),
                Department VARCHAR(100),
                Time VARCHAR(50),
                Date VARCHAR(50),
                Attendance VARCHAR(50)

            )
            """)

            self.conn.commit()

        except Exception as es:

            messagebox.showerror(
                "DATABASE ERROR",
                f"{str(es)}"
            )

        # =========================
        # VARIABLES
        # =========================

        self.var_attend_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()

        # =========================
        # AUTO DATE & TIME
        # =========================

        self.update_time()
        self.update_date()

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="ATTENDANCE MANAGEMENT SYSTEM",
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

        main_frame.place(x=20, y=70, width=1300, height=570)

        # =========================
        # LEFT FRAME
        # =========================

        left_frame = LabelFrame(
            main_frame,
            text="STUDENT ATTENDANCE DETAILS",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=3,
            relief=RIDGE
        )

        left_frame.place(x=10, y=10, width=550, height=550)

        # =========================
        # LABELS & ENTRIES
        # =========================

        labels = [

            ("Attendance ID", self.var_attend_id),
            ("Roll No", self.var_roll),
            ("Student Name", self.var_name),
            ("Department", self.var_dep),
            ("Time", self.var_time),
            ("Date", self.var_date)

        ]

        row_num = 0

        for text, variable in labels:

            Label(
                left_frame,
                text=text,
                font=("Poppins", 11, "bold"),
                bg="#1e293b",
                fg="white"
            ).grid(row=row_num, column=0, padx=20, pady=15, sticky=W)

            entry = ttk.Entry(
                left_frame,
                textvariable=variable,
                width=25,
                font=("Poppins", 11)
            )

            entry.grid(row=row_num, column=1, padx=10, pady=15)

            if text == "Time" or text == "Date":
                entry.config(state="readonly")

            row_num += 1

        # =========================
        # ATTENDANCE STATUS
        # =========================

        Label(
            left_frame,
            text="Attendance Status",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=6, column=0, padx=20, pady=15, sticky=W)

        attendance_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_attendance,
            font=("Poppins", 11),
            state="readonly",
            width=22
        )

        attendance_combo["values"] = (
            "Status",
            "Present",
            "Absent"
        )

        attendance_combo.current(0)

        attendance_combo.grid(row=6, column=1)

        # =========================
        # BUTTON FRAME
        # =========================

        btn_frame = Frame(
            left_frame,
            bg="#1e293b"
        )

        btn_frame.place(x=10, y=380, width=520, height=130)

        # IMPORT BUTTON

        Button(
            btn_frame,
            text="IMPORT CSV",
            command=self.importCsv,
            font=("Poppins", 9, "bold"),
            bg="#38bdf8",
            fg="black",
            width=15
        ).grid(row=0, column=0, padx=10, pady=15)

        # EXPORT BUTTON

        Button(
            btn_frame,
            text="EXPORT CSV",
            command=self.exportCsv,
            font=("Poppins", 9, "bold"),
            bg="#22c55e",
            fg="black",
            width=15
        ).grid(row=0, column=1, padx=10)

        # SAVE BUTTON

        Button(
            btn_frame,
            text="SAVE",
            command=self.save_data,
            font=("Poppins", 9, "bold"),
            bg="#8b5cf6",
            fg="white",
            width=15
        ).grid(row=1, column=0, padx=10, pady=15)

        # UPDATE BUTTON

        Button(
            btn_frame,
            text="UPDATE",
            command=self.update_data,
            font=("Poppins", 9, "bold"),
            bg="#f59e0b",
            fg="black",
            width=15
        ).grid(row=1, column=1, padx=10)

        # DELETE BUTTON

        Button(
            btn_frame,
            text="DELETE",
            command=self.delete_data,
            font=("Poppins", 9, "bold"),
            bg="#ef4444",
            fg="white",
            width=15
        ).grid(row=1, column=2, padx=10)

        # RESET BUTTON

        Button(
            btn_frame,
            text="RESET",
            command=self.reset_data,
            font=("Poppins", 9, "bold"),
            bg="#06b6d4",
            fg="black",
            width=15
        ).grid(row=1, column=3, padx=10)

        # =========================
        # RIGHT FRAME
        # =========================

        right_frame = LabelFrame(
            main_frame,
            text="ATTENDANCE DETAILS",
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="#38bdf8",
            bd=3,
            relief=RIDGE
        )

        right_frame.place(x=600, y=10, width=640, height=550)

        # =========================
        # SEARCH FRAME
        # =========================

        search_frame = Frame(
            right_frame,
            bg="#1e293b"
        )

        search_frame.place(x=10, y=10, width=600, height=60)

        Label(
            search_frame,
            text="Search",
            font=("Poppins", 11, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        self.search_var = StringVar()

        ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=30,
            font=("Poppins", 11)
        ).grid(row=0, column=1, padx=10)

        Button(
            search_frame,
            text="SEARCH",
            command=self.search_data,
            font=("Poppins", 10, "bold"),
            bg="#38bdf8",
            fg="black",
            width=12
        ).grid(row=0, column=2, padx=10)

        Button(
            search_frame,
            text="SHOW ALL",
            command=self.fetch_database_data,
            font=("Poppins", 10, "bold"),
            bg="#22c55e",
            fg="black",
            width=12
        ).grid(row=0, column=3)

        # =========================
        # TABLE FRAME
        # =========================

        table_frame = Frame(
            right_frame,
            bd=2,
            relief=RIDGE
        )

        table_frame.place(x=10, y=60, width=620, height=460)

        scroll_x = ttk.Scrollbar(
            table_frame,
            orient=HORIZONTAL
        )

        scroll_y = ttk.Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "roll",
                "name",
                "department",
                "time",
                "date",
                "attendance"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(
            command=self.AttendanceReportTable.xview
        )

        scroll_y.config(
            command=self.AttendanceReportTable.yview
        )

        headings = [

            ("id", "Attendance ID"),
            ("roll", "Roll No"),
            ("name", "Student Name"),
            ("department", "Department"),
            ("time", "Time"),
            ("date", "Date"),
            ("attendance", "Attendance")

        ]

        for col, text in headings:

            self.AttendanceReportTable.heading(
                col,
                text=text
            )

            self.AttendanceReportTable.column(
                col,
                width=120
            )

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.pack(
            fill=BOTH,
            expand=1
        )

        self.AttendanceReportTable.bind(
            "<ButtonRelease>",
            self.get_cursor
        )

        self.fetch_database_data()

    # =========================
    # AUTO TIME
    # =========================

    def update_time(self):

        current_time = datetime.now().strftime("%H:%M:%S")

        self.var_time.set(current_time)

        self.root.after(1000, self.update_time)

    # =========================
    # AUTO DATE
    # =========================

    def update_date(self):

        current_date = datetime.now().strftime("%d/%m/%Y")

        self.var_date.set(current_date)

    # =========================
    # SAVE DATA
    # =========================

    def save_data(self):

        if self.var_attend_id.get() == "":

            messagebox.showerror(
                "ERROR",
                "ATTENDANCE ID REQUIRED"
            )

            return

        try:

            self.my_cursor.execute("""
            INSERT INTO attendance1
            VALUES(%s,%s,%s,%s,%s,%s,%s)
            """, (

                self.var_attend_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance.get()

            ))

            self.conn.commit()

            self.fetch_database_data()

            messagebox.showinfo(
                "SUCCESS",
                "DATA STORED SUCCESSFULLY"
            )

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # FETCH DATABASE DATA
    # =========================

    def fetch_database_data(self):

        self.my_cursor.execute(
            "SELECT * FROM attendance1"
        )

        data = self.my_cursor.fetchall()

        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children()
        )

        for row in data:

            self.AttendanceReportTable.insert(
                "",
                END,
                values=row
            )

    # =========================
    # IMPORT CSV
    # =========================

    def importCsv(self):

        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(
                ("CSV File", "*.csv"),
                ("All File", "*.*")
            ),
            parent=self.root
        )

        if fln == "":
            return

        try:

            with open(fln) as myfile:

                csvread = csv.reader(myfile)

                next(csvread)

                for i in csvread:

                    self.my_cursor.execute("""
                    INSERT INTO attendance1
                    VALUES(%s,%s,%s,%s,%s,%s,%s)
                    """, (

                        i[0],
                        i[1],
                        i[2],
                        i[3],
                        i[4],
                        i[5],
                        i[6]

                    ))

            self.conn.commit()

            self.fetch_database_data()

            messagebox.showinfo(
                "SUCCESS",
                "CSV IMPORTED SUCCESSFULLY"
            )

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # EXPORT CSV
    # =========================

    def exportCsv(self):

        try:

            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(
                    ("CSV File", "*.csv"),
                    ("All File", "*.*")
                ),
                parent=self.root
            )

            if fln == "":
                return

            self.my_cursor.execute(
                "SELECT * FROM attendance1"
            )

            data = self.my_cursor.fetchall()

            with open(fln, mode="w", newline="") as myfile:

                exp_write = csv.writer(myfile)

                exp_write.writerow([
                    "ID",
                    "ROLL",
                    "NAME",
                    "DEPARTMENT",
                    "TIME",
                    "DATE",
                    "STATUS"
                ])

                for i in data:

                    exp_write.writerow(i)

            messagebox.showinfo(
                "SUCCESS",
                "CSV FILE EXPORTED SUCCESSFULLY"
            )

        except Exception as es:

            messagebox.showerror(
                "ERROR",
                f"{str(es)}"
            )

    # =========================
    # GET CURSOR
    # =========================

    def get_cursor(self, event=""):

        cursor_row = self.AttendanceReportTable.focus()

        content = self.AttendanceReportTable.item(cursor_row)

        rows = content["values"]

        if len(rows) == 0:
            return

        self.var_attend_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    # =========================
    # UPDATE DATA
    # =========================

    def update_data(self):

        if self.var_attend_id.get() == "":

            messagebox.showerror(
                "ERROR",
                "SELECT RECORD"
            )

            return

        try:

            self.my_cursor.execute("""
            UPDATE attendance1 SET

            Roll=%s,
            Name=%s,
            Department=%s,
            Time=%s,
            Date=%s,
            Attendance=%s

            WHERE Attendance_ID=%s
            """, (

                self.var_roll.get(),
                self.var_name.get(),
                self.var_dep.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attendance.get(),
                self.var_attend_id.get()

            ))

            self.conn.commit()

            self.fetch_database_data()

            messagebox.showinfo(
                "SUCCESS",
                "DATA UPDATED SUCCESSFULLY"
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

        if self.var_attend_id.get() == "":

            messagebox.showerror(
                "ERROR",
                "SELECT RECORD"
            )

            return

        try:

            delete = messagebox.askyesno(
                "DELETE",
                "DO YOU WANT TO DELETE?"
            )

            if delete > 0:

                self.my_cursor.execute("""
                DELETE FROM attendance1
                WHERE Attendance_ID=%s
                """, (

                    self.var_attend_id.get(),

                ))

                self.conn.commit()

                self.fetch_database_data()

                messagebox.showinfo(
                    "SUCCESS",
                    "DATA DELETED SUCCESSFULLY"
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

        self.var_attend_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_attendance.set("Status")

        self.update_time()
        self.update_date()

    # =========================
    # SEARCH DATA
    # =========================

    def search_data(self):

        keyword = self.search_var.get().lower()

        self.my_cursor.execute(
            "SELECT * FROM attendance1"
        )

        data = self.my_cursor.fetchall()

        filtered_data = []

        for row in data:

            row_text = " ".join(map(str, row)).lower()

            if keyword in row_text:

                filtered_data.append(row)

        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children()
        )

        for row in filtered_data:

            self.AttendanceReportTable.insert(
                "",
                END,
                values=row
            )

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Attendance(root)

    root.mainloop()
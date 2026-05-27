from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pandas as pd
from datetime import datetime, timedelta

class Attendance:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1200x650+100+50")

        self.root.title("Attendance Report System")

        self.root.config(bg="#0f172a")

        title = Label(
            self.root,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            font=("Poppins", 24, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(fill=X)

        # ================= BUTTON FRAME =================

        btn_frame = Frame(self.root, bg="#0f172a")

        btn_frame.pack(pady=20)

        Button(
            btn_frame,
            text="DAILY REPORT",
            command=self.daily_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            text="WEEKLY REPORT",
            command=self.weekly_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=1, padx=10)

        Button(
            btn_frame,
            text="MONTHLY REPORT",
            command=self.monthly_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white"
        ).grid(row=0, column=2, padx=10)

        Button(
            btn_frame,
            text="EXPORT EXCEL",
            command=self.export_excel,
            font=("Poppins", 12, "bold"),
            bg="green",
            fg="white"
        ).grid(row=0, column=3, padx=10)

        # ================= TABLE =================

        table_frame = Frame(self.root)

        table_frame.pack(fill=BOTH, expand=1)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)

        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(
            table_frame,
            columns=(
                "id",
                "name",
                "department",
                "time",
                "date",
                "status"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_table.xview)

        scroll_y.config(command=self.attendance_table.yview)

        headings = [
            ("id", "Student ID"),
            ("name", "Name"),
            ("department", "Department"),
            ("time", "Time"),
            ("date", "Date"),
            ("status", "Status")
        ]

        for col, text in headings:

            self.attendance_table.heading(col, text=text)

            self.attendance_table.column(col, width=150)

        self.attendance_table["show"] = "headings"

        self.attendance_table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    # ================= FETCH DATA =================

    def fetch_data(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

        if len(data) != 0:

            self.attendance_table.delete(
                *self.attendance_table.get_children()
            )

            for i in data:

                self.attendance_table.insert("", END, values=i)

        conn.close()

    # ================= DAILY REPORT =================

    def daily_report(self):

        today = datetime.now().strftime("%d/%m/%Y")

        self.filter_report(today)

    # ================= WEEKLY REPORT =================

    def weekly_report(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        today = datetime.now()

        for row in data:

            row_date = datetime.strptime(row[5], "%d/%m/%Y")

            if (today - row_date).days <= 7:

                self.attendance_table.insert("", END, values=row)

        conn.close()

    # ================= MONTHLY REPORT =================

    def monthly_report(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        today = datetime.now()

        for row in data:

            row_date = datetime.strptime(row[5], "%d/%m/%Y")

            if (today - row_date).days <= 30:

                self.attendance_table.insert("", END, values=row)

        conn.close()

    # ================= FILTER REPORT =================

    def filter_report(self, filter_date):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        my_cursor = conn.cursor()

        my_cursor.execute(
            "SELECT * FROM attendance1 WHERE DATE=%s",
            (filter_date,)
        )

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        for i in data:

            self.attendance_table.insert("", END, values=i)

        conn.close()

    # ================= EXPORT EXCEL =================

    def export_excel(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        query = "SELECT * FROM attendance1"

        df = pd.read_sql(query, conn)

        df.to_excel("attendance_report.xlsx", index=False)

        conn.close()

        messagebox.showinfo(
            "SUCCESS",
            "Attendance Exported Successfully"
        )

# ================= MAIN =================

if __name__ == "__main__":

    root = Tk()

    obj = Attendance(root)

    root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import pandas as pd
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Attendance:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1450x800+30+10")

        self.root.title("AI Attendance Analytics Dashboard")

        self.root.config(bg="#0f172a")

        # ================= TITLE =================

        title = Label(
            self.root,
            text="AI ATTENDANCE ANALYTICS SYSTEM",
            font=("Poppins", 26, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title.pack(fill=X, pady=10)

        # ================= BUTTON FRAME =================

        btn_frame = Frame(self.root, bg="#0f172a")

        btn_frame.pack(pady=10)

        Button(
            btn_frame,
            text="DAILY REPORT",
            command=self.daily_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white",
            width=18
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            text="WEEKLY REPORT",
            command=self.weekly_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white",
            width=18
        ).grid(row=0, column=1, padx=10)

        Button(
            btn_frame,
            text="MONTHLY REPORT",
            command=self.monthly_report,
            font=("Poppins", 12, "bold"),
            bg="#1e293b",
            fg="white",
            width=18
        ).grid(row=0, column=2, padx=10)

        Button(
            btn_frame,
            text="PRESENT / ABSENT GRAPH",
            command=self.show_attendance_graph,
            font=("Poppins", 12, "bold"),
            bg="#2563eb",
            fg="white",
            width=22
        ).grid(row=0, column=3, padx=10)

        Button(
            btn_frame,
            text="MONTHLY ANALYTICS",
            command=self.monthly_analytics_graph,
            font=("Poppins", 12, "bold"),
            bg="#7c3aed",
            fg="white",
            width=22
        ).grid(row=0, column=4, padx=10)

        Button(
            btn_frame,
            text="EXPORT EXCEL",
            command=self.export_excel,
            font=("Poppins", 12, "bold"),
            bg="green",
            fg="white",
            width=18
        ).grid(row=0, column=5, padx=10)

        # ================= TABLE =================

        table_frame = Frame(self.root)

        table_frame.pack(fill=BOTH, expand=1, padx=20, pady=10)

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

        # ================= ANALYTICS LABEL =================

        self.analytics_label = Label(
            self.root,
            text="",
            font=("Poppins", 14, "bold"),
            bg="#0f172a",
            fg="#facc15"
        )

        self.analytics_label.pack(pady=10)

        # ================= GRAPH FRAME =================

        self.graph_frame = Frame(self.root, bg="#0f172a")

        self.graph_frame.pack(fill=BOTH, expand=1)

        self.fetch_data()

    # ================= DATABASE CONNECTION =================

    def database_connection(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="1511",
            database="face"
        )

        return conn

    # ================= FETCH DATA =================

    def fetch_data(self):

        conn = self.database_connection()

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

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

        conn = self.database_connection()

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        today = datetime.now()

        count = 0

        for row in data:

            row_date = datetime.strptime(row[5], "%d/%m/%Y")

            if (today - row_date).days <= 7:

                self.attendance_table.insert("", END, values=row)

                count += 1

        self.analytics_label.config(
            text=f"Weekly Attendance Records: {count}"
        )

        conn.close()

    # ================= MONTHLY REPORT =================

    def monthly_report(self):

        conn = self.database_connection()

        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM attendance1")

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        today = datetime.now()

        count = 0

        for row in data:

            row_date = datetime.strptime(row[5], "%d/%m/%Y")

            if (today - row_date).days <= 30:

                self.attendance_table.insert("", END, values=row)

                count += 1

        self.analytics_label.config(
            text=f"Monthly Attendance Records: {count}"
        )

        conn.close()

    # ================= FILTER REPORT =================

    def filter_report(self, filter_date):

        conn = self.database_connection()

        my_cursor = conn.cursor()

        my_cursor.execute(
            "SELECT * FROM attendance1 WHERE date=%s",
            (filter_date,)
        )

        data = my_cursor.fetchall()

        self.attendance_table.delete(
            *self.attendance_table.get_children()
        )

        for i in data:

            self.attendance_table.insert("", END, values=i)

        self.analytics_label.config(
            text=f"Daily Attendance Report: {filter_date}"
        )

        conn.close()

    # ================= PRESENT / ABSENT GRAPH =================

    def show_attendance_graph(self):

        conn = self.database_connection()

        query = """
        SELECT status, COUNT(*) as total
        FROM attendance1
        GROUP BY status
        """

        df = pd.read_sql(query, conn)

        conn.close()

        for widget in self.graph_frame.winfo_children():

            widget.destroy()

        fig = plt.Figure(figsize=(7, 4), dpi=100)

        ax = fig.add_subplot(111)

        ax.bar(df["status"], df["total"])

        ax.set_title("Present vs Absent")

        ax.set_xlabel("Attendance Status")

        ax.set_ylabel("Total Students")

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)

        canvas.draw()

        canvas.get_tk_widget().pack()

    # ================= MONTHLY ANALYTICS GRAPH =================

    def monthly_analytics_graph(self):

        conn = self.database_connection()

        query = """
        SELECT date, COUNT(*) as total
        FROM attendance1
        GROUP BY date
        """

        df = pd.read_sql(query, conn)

        conn.close()

        for widget in self.graph_frame.winfo_children():

            widget.destroy()

        fig = plt.Figure(figsize=(8, 4), dpi=100)

        ax = fig.add_subplot(111)

        ax.plot(df["date"], df["total"], marker='o')

        ax.set_title("Monthly Attendance Analytics")

        ax.set_xlabel("Date")

        ax.set_ylabel("Attendance Count")

        plt.xticks(rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)

        canvas.draw()

        canvas.get_tk_widget().pack()

    # ================= EXPORT EXCEL =================

    def export_excel(self):

        conn = self.database_connection()

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
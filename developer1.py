from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

# =========================
# DEVELOPER CLASS
# =========================

class Developer:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1530x790+0+0")

        self.root.title("DEVELOPER INFORMATION")

        self.root.config(bg="#0f172a")

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="DEVELOPER INFORMATION",
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

        main_frame.place(x=20, y=60, width=1230, height=580)

        # =========================
        # LEFT FRAME
        # =========================

        left_frame = Frame(
            main_frame,
            bg="#0f172a",
            bd=3,
            relief=RIDGE
        )

        left_frame.place(x=20, y=20, width=450, height=550)

        # =========================
        # DEVELOPER IMAGE
        # =========================

        try:

            img = Image.open(r"D:\face\image1/dev.jpg")

            img = img.resize((250, 250), Image.LANCZOS)

            self.photoimg = ImageTk.PhotoImage(img)

            img_lbl = Label(
                left_frame,
                image=self.photoimg,
                bg="#0f172a"
            )

            img_lbl.pack(pady=20)

        except:

            no_img = Label(
                left_frame,
                text="DEVELOPER PHOTO",
                font=("Poppins", 18, "bold"),
                bg="#334155",
                fg="white"
            )

            no_img.place(x=70, y=50, width=300, height=250)

        # =========================
        # NAME
        # =========================

        name_lbl = Label(
            left_frame,
            text="Arpit Nayak",
            font=("Poppins", 20, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        name_lbl.pack(pady=10)

        # =========================
        # COURSE
        # =========================

        course_lbl = Label(
            left_frame,
            text="BCA Semester 6 Student",
            font=("Poppins", 14),
            bg="#0f172a",
            fg="white"
        )

        course_lbl.pack()

        # =========================
        # CONTACT SECTION
        # =========================

        contact_frame = LabelFrame(
            left_frame,
            text="CONTACT INFORMATION",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="#38bdf8",
            bd=2,
            relief=RIDGE
        )

        contact_frame.place(x=20, y=390, width=400, height=130)

        Label(
            contact_frame,
            text="Email : yourmail@gmail.com",
            font=("Poppins", 11),
            bg="#0f172a",
            fg="white"
        ).pack(anchor=W, padx=10, pady=10)

        Label(
            contact_frame,
            text="Phone : +91 XXXXX XXXXX",
            font=("Poppins", 11),
            bg="#0f172a",
            fg="white"
        ).pack(anchor=W, padx=10)

        Label(
            contact_frame,
            text="Location : Ahmedabad, Gujarat",
            font=("Poppins", 11),
            bg="#0f172a",
            fg="white"
        ).pack(anchor=W, padx=10, pady=10)

        # =========================
        # RIGHT FRAME
        # =========================

        right_frame = Frame(
            main_frame,
            bg="#0f172a",
            bd=3,
            relief=RIDGE
        )

        right_frame.place(x=480, y=20, width=730, height=550)

        # =========================
        # ABOUT PROJECT
        # =========================

        about_lbl = Label(
            right_frame,
            text="ABOUT PROJECT",
            font=("Poppins", 17, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        about_lbl.pack(pady=5)

        project_text = """

Face Recognition Attendance System is an AI based smart attendance project.

This project is developed using:

• Python Programming
• OpenCV
• Tkinter GUI
• MySQL Database
• Face Recognition Technology


        """

        text_lbl = Label(
            right_frame,
            text=project_text,
            justify=LEFT,
            font=("Poppins", 14),
            bg="#0f172a",
            fg="white"
        )

        text_lbl.pack(padx=5,pady=5,anchor="n")

        # =========================
        # SKILLS SECTION
        # =========================

        skills_frame = LabelFrame(
            right_frame,
            text="TECHNICAL SKILLS",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="#38bdf8",
            bd=2,
            relief=RIDGE
        )

        skills_frame.place(x=30, y=330, width=300, height=160)

        skills = [

            "Python Programming",
            "Tkinter GUI",
            "OpenCV",
            "MySQL Database",
            "Face Recognition",
            "AI Chatbot"

        ]

        for skill in skills:

            Label(
                skills_frame,
                text=f"✓ {skill}",
                font=("Poppins", 11),
                bg="#0f172a",
                fg="white"
            ).pack(anchor=W, padx=20, pady=3)

        # =========================
        # TECHNOLOGY SECTION
        # =========================

        tech_frame = LabelFrame(
            right_frame,
            text="TECHNOLOGIES USED",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="#38bdf8",
            bd=2,
            relief=RIDGE
        )

        tech_frame.place(x=380, y=330, width=300, height=160)

        techs = [

            "Python 3.12",
            "OpenCV",
            "NumPy",
            "Pillow",
            "MySQL",
            "Tkinter"

        ]

        for tech in techs:

            Label(
                tech_frame,
                text=f"✓ {tech}",
                font=("Poppins", 11),
                bg="#0f172a",
                fg="white"
            ).pack(anchor=W, padx=20, pady=3)

        # =========================
        # SOCIAL BUTTONS
        # =========================

        social_frame = Frame(
            right_frame,
            bg="#0f172a"
        )

        social_frame.place(x=200, y=500, width=450, height=40)

        github_btn = Button(
            social_frame,
            text="GitHub",
            command=lambda: self.open_link("https://github.com"),
            font=("Poppins", 11, "bold"),
            bg="#38bdf8",
            fg="black",
            width=10,
            cursor="hand2"
        )

        github_btn.grid(row=0, column=0, padx=10)

        linkedin_btn = Button(
            social_frame,
            text="LinkedIn",
            command=lambda: self.open_link("https://linkedin.com"),
            font=("Poppins", 11, "bold"),
            bg="#22c55e",
            fg="black",
            width=10,
            cursor="hand2"
        )

        linkedin_btn.grid(row=0, column=1, padx=10)

        gmail_btn = Button(
            social_frame,
            text="Gmail",
            command=lambda: self.open_link("https://mail.google.com"),
            font=("Poppins", 11, "bold"),
            bg="#f59e0b",
            fg="black",
            width=10,
            cursor="hand2"
        )

        gmail_btn.grid(row=0, column=2, padx=10)

    # =========================
    # OPEN LINKS
    # =========================

    def open_link(self, url):

        webbrowser.open(url)

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Developer(root)

    root.mainloop()
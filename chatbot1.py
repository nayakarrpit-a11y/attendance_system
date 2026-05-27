from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

import datetime
import pyttsx3
import threading

# =========================
# CHATBOT CLASS
# =========================

class ChatBot:

    def __init__(self, root):

        self.root = root

        self.root.geometry("900x700+250+50")

        self.root.title("AI CHATBOT")

        self.root.config(bg="#0f172a")

        # =========================
        # TEXT TO SPEECH
        # =========================

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="AI CHATBOT SYSTEM",
            font=("Poppins", 26, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title_lbl.pack(fill=X)

        # =========================
        # DATE & TIME
        # =========================

        self.time_lbl = Label(
            self.root,
            text="",
            font=("Poppins", 11, "bold"),
            bg="#0f172a",
            fg="white"
        )

        self.time_lbl.pack(pady=5)

        self.update_time()

        # =========================
        # CHAT FRAME
        # =========================

        chat_frame = Frame(
            self.root,
            bg="#1e293b",
            bd=3,
            relief=RIDGE
        )

        chat_frame.place(x=20, y=80, width=1250, height=500)

        # =========================
        # CHAT AREA
        # =========================

        self.chat_area = ScrolledText(
            chat_frame,
            font=("Poppins", 12),
            bg="#111827",
            fg="white",
            wrap=WORD
        )

        self.chat_area.place(x=10, y=10, width=1220, height=475)

        self.chat_area.insert(
            END,
            "🤖 Bot: Hello! Welcome to Face Recognition System Chatbot.\n\n"
        )

        self.chat_area.config(state=DISABLED)

        # =========================
        # INPUT FRAME
        # =========================

        input_frame = Frame(
            self.root,
            bg="#0f172a"
        )

        input_frame.place(x=250, y=600, width=860, height=70)

        self.user_input = StringVar()

        self.entry = Entry(
            input_frame,
            textvariable=self.user_input,
            font=("Poppins", 13),
            bg="#1e293b",
            fg="white",
            insertbackground="white"
        )

        self.entry.place(x=10, y=10, width=520, height=45)

        self.entry.bind("<Return>", self.send_message)

        # =========================
        # SEND BUTTON
        # =========================

        send_btn = Button(
            input_frame,
            text="SEND",
            command=self.send_message,
            font=("Poppins", 12, "bold"),
            bg="#38bdf8",
            fg="black",
            width=10,
            cursor="hand2"
        )

        send_btn.place(x=550, y=10, width=120, height=45)

        # =========================
        # CLEAR BUTTON
        # =========================

        clear_btn = Button(
            input_frame,
            text="CLEAR",
            command=self.clear_chat,
            font=("Poppins", 12, "bold"),
            bg="#ef4444",
            fg="white",
            width=10,
            cursor="hand2"
        )

        clear_btn.place(x=700, y=10, width=120, height=45)

        # =========================
        # VOICE GREETING
        # =========================

        threading.Thread(
            target=self.speak,
            args=("Hello Welcome to AI Chatbot System",),
            daemon=True
        ).start()

    # =========================
    # UPDATE TIME
    # =========================

    def update_time(self):

        current_time = datetime.datetime.now().strftime(
            "%d-%m-%Y   %I:%M:%S %p"
        )

        self.time_lbl.config(
            text=f"Date & Time : {current_time}"
        )

        self.root.after(1000, self.update_time)

    # =========================
    # SPEAK FUNCTION
    # =========================

    def speak(self, text):

        self.engine.say(text)

        self.engine.runAndWait()

    # =========================
    # SEND MESSAGE
    # =========================

    def send_message(self, event=None):

        user_msg = self.user_input.get().strip()

        if user_msg == "":
            return

        self.chat_area.config(state=NORMAL)

        self.chat_area.insert(
            END,
            f"🧑 You: {user_msg}\n\n"
        )

        bot_reply = self.get_response(user_msg)

        self.chat_area.insert(
            END,
            f"🤖 Bot: {bot_reply}\n\n"
        )

        self.chat_area.config(state=DISABLED)

        self.chat_area.see(END)

        self.user_input.set("")

        threading.Thread(
            target=self.speak,
            args=(bot_reply,),
            daemon=True
        ).start()

    # =========================
    # CHATBOT RESPONSES
    # =========================

    def get_response(self, msg):

        msg = msg.lower()

        # =========================
        # GREETINGS
        # =========================

        if "hello" in msg or "hi" in msg:

            return "Hello! How can I help you today?"

        elif "how are you" in msg:

            return "I am fine. Thank you for asking."

        elif "your name" in msg:

            return "I am AI Chatbot for Face Recognition System."

        # =========================
        # PROJECT QUESTIONS
        # =========================

        elif "project" in msg:

            return (
                "This is a Face Recognition Attendance System "
                "developed using Python, OpenCV, Tkinter and MySQL."
            )

        elif "attendance" in msg:

            return (
                "Attendance is automatically marked "
                "when face recognition detects a student."
            )

        elif "face recognition" in msg:

            return (
                "Face Recognition identifies a person "
                "using facial features through webcam."
            )

        elif "student" in msg:

            return (
                "Student module manages student details, "
                "database records and photo samples."
            )

        elif "train data" in msg:

            return (
                "Train Data converts captured face images "
                "into trained classifier data."
            )

        elif "developer" in msg:

            return (
                "Developer module shows project "
                "developer information and technologies used."
            )

        elif "chatbot" in msg:

            return (
                "I am an AI chatbot that answers "
                "questions related to your project."
            )

        elif "database" in msg:

            return (
                "The project uses MySQL database "
                "to store student and attendance details."
            )

        elif "python" in msg:

            return (
                "Python is the main programming language "
                "used in this project."
            )

        elif "opencv" in msg:

            return (
                "OpenCV is used for face detection "
                "and face recognition."
            )

        elif "tkinter" in msg:

            return (
                "Tkinter is used to create GUI interface."
            )

        # =========================
        # TIME & DATE
        # =========================

        elif "time" in msg:

            current_time = datetime.datetime.now().strftime(
                "%I:%M:%S %p"
            )

            return f"Current time is {current_time}"

        elif "date" in msg:

            current_date = datetime.datetime.now().strftime(
                "%d-%m-%Y"
            )

            return f"Today's date is {current_date}"

        # =========================
        # EXIT
        # =========================

        elif "bye" in msg or "exit" in msg:

            return "Goodbye! Have a nice day."

        # =========================
        # DEFAULT RESPONSE
        # =========================

        else:

            return (
                "Sorry, I did not understand. "
                "Please ask project related questions."
            )

    # =========================
    # CLEAR CHAT
    # =========================

    def clear_chat(self):

        self.chat_area.config(state=NORMAL)

        self.chat_area.delete(1.0, END)

        self.chat_area.insert(
            END,
            "🤖 Bot: Chat Cleared Successfully.\n\n"
        )

        self.chat_area.config(state=DISABLED)

# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = ChatBot(root)

    root.mainloop()
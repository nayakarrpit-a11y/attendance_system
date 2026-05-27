from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import cv2
import os
import mysql.connector
import numpy as np
from time import strftime
from datetime import datetime

# =========================
# FACE RECOGNITION CLASS
# =========================

class Face_Recognition:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1530x790+0+0")

        self.root.title("FACE RECOGNITION SYSTEM")

        self.root.config(bg="#0f172a")


        # =========================
        # CAMERA VARIABLES
        # =========================

        self.video_cap = None
        self.running = False

        # =========================
        # WINDOW CLOSE EVENT
        # =========================

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_closing
        )

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
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

        main_frame.place(x=20, y=70, width=1240, height=570)

        # =========================
        # LEFT IMAGE
        # =========================

        try:

            img = Image.open(r"D:\face\image1/face.avif")

            img = img.resize((600, 500), Image.LANCZOS)

            self.photoimg = ImageTk.PhotoImage(img)

            f_lbl = Label(
                main_frame,
                image=self.photoimg,
                bg="#1e293b"
            )

            f_lbl.place(x=50, y=30, width=550, height=500)

        except:

            no_img = Label(
                main_frame,
                text="FACE RECOGNITION",
                font=("Poppins", 25, "bold"),
                bg="#334155",
                fg="white"
            )

            no_img.place(x=30, y=50, width=600, height=500)

        # =========================
        # RIGHT FRAME
        # =========================

        right_frame = Frame(
            main_frame,
            bg="#0f172a",
            bd=3,
            relief=RIDGE
        )

        right_frame.place(x=670, y=30, width=520, height=500)

        heading = Label(
            right_frame,
            text="REAL-TIME FACE DETECTION",
            font=("Poppins", 22, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        heading.pack(pady=20)

        info = Label(
            right_frame,
            text=(
                "This module detects student faces\n"
                "using trained dataset images.\n\n"
                "Attendance will automatically\n"
                "be stored in CSV file."
            ),
            font=("Poppins", 13),
            bg="#0f172a",
            fg="white",
            justify=CENTER
        )

        info.pack(pady=20)

        # =========================
        # STATUS LABEL
        # =========================

        self.status_lbl = Label(
            right_frame,
            text="Camera Not Started",
            font=("Poppins", 12, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )

        self.status_lbl.pack(pady=20)

        # =========================
        #  START BUTTON
        # =========================

        detect_btn = Button(
            right_frame,
            text="START FACE RECOGNITION",
            command=self.face_recog,
            font=("Poppins", 15, "bold"),
            bg="#38bdf8",
            fg="black",
            cursor="hand2",
            width=25
        )

        detect_btn.pack(pady=20)


    # =========================
    # ATTENDANCE FUNCTION
    # =========================

    def mark_attendance(self, i, r, n, d):

        file_path = "attendance.csv"

        if not os.path.exists(file_path):

            with open(file_path, "w", newline="\n") as f:

                f.write(
                    "ID,ROLL,NAME,DEPARTMENT,TIME,DATE,STATUS\n"
                )

        with open(file_path, "r+", newline="\n") as f:

            myDataList = f.readlines()

            name_list = []

            for line in myDataList:

                entry = line.split(",")

                name_list.append(entry[0])

            if (
                (i not in name_list)
            ):

                now = datetime.now()

                d1 = now.strftime("%d/%m/%Y")

                dtString = now.strftime("%H:%M:%S")

                f.writelines(
                    f"\n{i},{r},{n},{d},{dtString},{d1},Present"
                )

    # =========================
    # FACE RECOGNITION
    # =========================

    def face_recog(self):

        # =========================
        # DRAW BOUNDARY
        # =========================

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):

            gray_image = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )

            features = classifier.detectMultiScale(
                gray_image,
                scaleFactor,
                minNeighbors
            )

            

            for (x, y, w, h) in features:

                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    color,
                    3
                )

                id, predict = clf.predict(
                    gray_image[y:y+h, x:x+w]
                )

                confidence = int(
                    (100 * (1 - predict / 300))
                )

                # =========================
                # DATABASE CONNECTION
                # =========================

                try:

                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="1511",
                        database="face"
                    )

                    my_cursor = conn.cursor()

                    my_cursor.execute(
                        "SELECT NAME FROM student1 WHERE STD_ID=" + str(id)
                    )

                    n = my_cursor.fetchone()

                    n = "+".join(n)

                    my_cursor.execute(
                        "SELECT ROLL FROM student1 WHERE STD_ID=" + str(id)
                    )

                    r = my_cursor.fetchone()

                    r = "+".join(r)

                    my_cursor.execute(
                        "SELECT DEP FROM student1 WHERE STD_ID=" + str(id)
                    )

                    d = my_cursor.fetchone()

                    d = "+".join(d)

                    my_cursor.execute(
                        "SELECT STD_ID FROM student1 WHERE STD_ID=" + str(id)
                    )

                    i = my_cursor.fetchone()

                    i = "+".join(i)

                    conn.close()

                except:

                    n = "Unknown"
                    r = "Unknown"
                    d = "Unknown"
                    i = "Unknown"

                # =========================
                # FACE MATCH
                # =========================

                if confidence > 77:

                    cv2.putText(
                        img,
                        f"ID : {i}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    cv2.putText(
                        img,
                        f"Name : {n}",
                        (x, y - 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    cv2.putText(
                        img,
                        f"Roll : {r}",
                        (x, y - 25),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    cv2.putText(
                        img,
                        f"Department : {d}",
                        (x, y),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        2
                    )

                    self.mark_attendance(
                        i,
                        r,
                        n,
                        d
                    )

                    self.status_lbl.config(
                        text=f"Detected : {n}"
                    )

                else:

                    cv2.rectangle(
                        img,
                        (x, y),
                        (x + w, y + h),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        img,
                        "UNKNOWN FACE",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (255, 255, 255),
                        2
                    )

                    self.status_lbl.config(
                        text="Unknown Face Detected"
                    )

            return img

        # =========================
        # LOAD CLASSIFIER
        # =========================

        faceCascade = cv2.CascadeClassifier(
            cv2.data.haarcascades +
            "haarcascade_frontalface_default.xml"
        )

        try:

            clf = cv2.face.LBPHFaceRecognizer_create()

            clf.read("classifier.xml")

        except:

            messagebox.showerror(
                "ERROR",
                "Please Train Data First"
            )

            return

        self.video_cap = cv2.VideoCapture(0)

        if not self.video_cap.isOpened():

            messagebox.showerror(
                "ERROR",
                "Camera Not Found"
            )

            return
        
        self.running=True

        self.status_lbl.config(
            text="Camera Started"
        )

        # =========================
        # START TIMER
        # =========================

        start_time = datetime.now()

        # =========================
        # CAMERA LOOP
        # =========================

        while self.running:

            ret, img = self.video_cap.read()

            if not ret:
                break

            img = draw_boundary(
                img,
                faceCascade,
                1.1,
                10,
                (0, 255, 0),
                "Face",
                clf
            )

            cv2.imshow(
                "FACE RECOGNITION",
                img
            )
            
             # =========================
            # AUTO CLOSE AFTER 30 SECOND
            # =========================

            current_time = datetime.now()

            seconds = (
                current_time - start_time
            ).seconds

            if seconds >= 15:

                messagebox.showinfo(
                    "INFO",
                    "Camera Closed Automatically After 15 Seconds"
                )

                break

            # ENTER KEY TO EXIT

            if cv2.waitKey(1) == 13:

                break
           

    # =========================
    # STOP CAMERA
    # =========================

        self.running = False

        if self.video_cap is not None:

            self.video_cap.release()

        cv2.destroyAllWindows()

        self.status_lbl.config(
            text="Camera Closed"
        )

    # =========================
    # WINDOW CLOSE
    # =========================

    def on_closing(self):

        self.running = False

        if self.video_cap is not None:

            self.video_cap.release()

        cv2.destroyAllWindows()

        self.root.destroy()



# =========================
# MAIN
# =========================

if __name__ == "__main__":

    root = Tk()

    obj = Face_Recognition(root)

    root.mainloop()
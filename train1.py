from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import cv2
import os
import numpy as np

# =========================
# TRAIN CLASS
# =========================

class Train:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1200x700+100+50")
        self.root.title("Train Dataset")
        self.root.config(bg="#0f172a")

        # =========================
        # TITLE
        # =========================

        title_lbl = Label(
            self.root,
            text="FACE DATA TRAINING SYSTEM",
            font=("Arial", 28, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        title_lbl.pack(fill=X, pady=10)

        # =========================
        # MAIN FRAME
        # =========================

        main_frame = Frame(
            self.root,
            bg="#1e293b",
            bd=4,
            relief=RIDGE
        )

        main_frame.place(x=40, y=80, width=1200, height=560)

        # =========================
        # LEFT IMAGE FRAME
        # =========================

        left_frame = Frame(
            main_frame,
            bg="#1e293b"
        )

        left_frame.place(x=20, y=20, width=520, height=500)

        try:

            img = Image.open(r"D:\F2\image\tr.avif")

            img = img.resize((500, 500), Image.LANCZOS)

            self.photoimg = ImageTk.PhotoImage(img)

            img_lbl = Label(
                left_frame,
                image=self.photoimg,
                bg="#1e293b"
            )

            img_lbl.place(x=0, y=0, width=520, height=500)

        except:

            no_img = Label(
                left_frame,
                text="NO IMAGE FOUND",
                font=("Arial", 25, "bold"),
                bg="#334155",
                fg="white"
            )

            no_img.place(x=0, y=0, width=520, height=500)

        # =========================
        # RIGHT FRAME
        # =========================

        right_frame = Frame(
            main_frame,
            bg="#0f172a",
            bd=3,
            relief=RIDGE
        )

        right_frame.place(x=610, y=20, width=550, height=500)

        heading = Label(
            right_frame,
            text="TRAIN FACE DATA",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="#38bdf8"
        )

        heading.pack(pady=20)

        info = Label(
            right_frame,
            text=(
                "Click the button below to train\n"
                "all face images from gallery1 folder.\n\n"
                "Image Name Format:\n"
                "user.1.1.jpg\n"
                "user.2.1.jpg"
            ),
            font=("Arial", 14),
            bg="#0f172a",
            fg="white",
            justify=CENTER
        )

        info.pack(pady=20)

        # =========================
        # PROGRESS BAR
        # =========================

        self.progress = ttk.Progressbar(
            right_frame,
            orient=HORIZONTAL,
            length=350,
            mode="determinate"
        )

        self.progress.pack(pady=30)

        # =========================
        # STATUS LABEL
        # =========================

        self.status_lbl = Label(
            right_frame,
            text="Ready To Train",
            font=("Arial", 14, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )

        self.status_lbl.pack(pady=10)

        # =========================
        # TRAIN BUTTON
        # =========================

        train_btn = Button(
            right_frame,
            text="TRAIN DATA",
            command=self.train_classifier,
            font=("Arial", 16, "bold"),
            bg="#38bdf8",
            fg="black",
            activebackground="#0ea5e9",
            cursor="hand2",
            width=20,
            height=2,
            bd=0
        )

        train_btn.pack(pady=40)

    # =========================
    # TRAIN FUNCTION
    # =========================

    def train_classifier(self):

        data_dir = "gallery1"

        # =========================
        # CREATE FOLDER IF NOT EXISTS
        # =========================

        if not os.path.exists(data_dir):

            os.makedirs(data_dir)

            messagebox.showerror(
                "ERROR",
                "gallery1 folder created.\nPlease add images first."
            )

            return

        # =========================
        # GET IMAGE PATHS
        # =========================

        path = []

        for file in os.listdir(data_dir):

            if file.endswith(".jpg") or file.endswith(".png"):

                path.append(os.path.join(data_dir, file))

        if len(path) == 0:

            messagebox.showerror(
                "ERROR",
                "No Images Found In gallery1 Folder"
            )

            return

        faces = []
        ids = []

        total_images = len(path)

        self.progress["maximum"] = total_images

        image_count = 0

        # =========================
        # READ IMAGES
        # =========================

        for image_path in path:

            try:

                img = Image.open(image_path).convert('L')

                imageNp = np.array(img, 'uint8')

                filename = os.path.split(image_path)[1]

                # Example: user.1.1.jpg
                id = int(filename.split('.')[1])

                faces.append(imageNp)

                ids.append(id)

                cv2.imshow("Training", imageNp)

                cv2.waitKey(1)

                image_count += 1

                self.progress["value"] = image_count

                self.status_lbl.config(
                    text=f"Training {image_count}/{total_images}"
                )

                self.root.update_idletasks()

            except Exception as es:

                print("Image Error:", es)

        # =========================
        # CHECK FACE MODULE
        # =========================

        if not hasattr(cv2, 'face'):

            messagebox.showerror(
                "ERROR",
                "opencv-contrib-python not installed"
            )

            return

        # =========================
        # TRAIN MODEL
        # =========================

        try:

            clf = cv2.face.LBPHFaceRecognizer_create()

            clf.train(faces, np.array(ids))

            clf.write("classifier.xml")

            cv2.destroyAllWindows()

            self.progress["value"] = total_images

            self.status_lbl.config(
                text="Training Completed Successfully"
            )

            messagebox.showinfo(
                "SUCCESS",
                "Dataset Trained Successfully"
            )

        except AttributeError:

            messagebox.showerror(
                "ERROR",
                "Install opencv-contrib-python"
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

    obj = Train(root)

    root.mainloop()
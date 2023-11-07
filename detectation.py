import cv2
import os
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image

root = Tk()
root.geometry("500x500+100+50")
root.config(background="skyblue")
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)
root.title("Prisoner Detection")
high_font = Font(family="Times new Roman", size=18, weight="bold", underline=1 )
med_font = Font(family="Times new Roman", size=14, weight="bold", underline=1)
sml_font = Font(family="Times new Roman", size=10, weight="bold")
root.config(background="skyblue")
def id_get():
    id = enter_set.get()
    dectect = cv2.CascadeClassifier("C:/Users/Devil/AppData/Local/Programs/Python/Python311/Lib/site-packages/"
                                    "cv2/data/haarcascade_frontalface_default.xml")
    video = cv2.VideoCapture(0)

    count = 0
    background = cv2.imread("background.jpg")
    while True:
        ret, frame = video.read()
        video_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = dectect.detectMultiScale(
            video_gray,
            scaleFactor=1.3,
            minNeighbors=5, )
        for (x, y, w, h) in face:
            count = count + 1
            cv2.imwrite('dataset/user. ' + str(id) + "." + str(count) + ".jpg", video_gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        background[150:150 + 480, 55:55 + 640] = frame
        cv2.imshow("Face Detection", background)
        k = cv2.waitKey(1)
        if count >= 1000:
            break
    video.release()
    cv2.destroyAllWindows()
    while True:
        exit()
def exit_code():
    exit()
label = Label(root, text="Prisoner Detection",bg = "skyblue", font=high_font).grid(columnspan=1)
img = ImageTk.PhotoImage(Image.open("front1.png"))
panel = Label(root, image=img, background="skyblue", borderwidth=0)
panel.grid(columnspan=1)
wel = Label(root, text="Welcome", bg="skyblue", font=med_font).grid(columnspan=1)
enter_set = IntVar()
test_text_no = Label(root, text="1: ", font=sml_font, bg="skyblue").place(x=20,y=300)
test_text = Label(root, text="Enter the Id for Stroing Dataset:", font=sml_font, bg="skyblue").place(x=30,y=300)
enter = Entry(root, textvariable=enter_set).place(x=250,y=300)
buton = Button(root, text="Set value", command=id_get).place(x=220,y=330)
buton_exit = Button(root, text="Exit", command=exit_code).place(x=300, y=330)
root.mainloop()

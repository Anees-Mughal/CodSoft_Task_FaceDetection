from tkinter import *
from subprocess import call
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter import messagebox

import os

root = Tk()
root.geometry("500x500+100+50")
root.config(background="skyblue")
img = PhotoImage(file='icon.png')
root.iconphoto(False, img)
root.title("Prisoner Detection")
high_font = Font(family="Times new Roman", size=20, weight="bold", underline=1 )
med_font = Font(family="Times new Roman", size=14, weight="bold", underline=1)
sml_font = Font(family="Times new Roman", size=10, weight="bold")

def open_dectection():
    call(["Python", "detectation.py"])
def open_train():
    call(["Python", "train.py"])
def open_test():
    call(["Python", "test.py"])
label = Label(root, text="Prisoner Detection",bg = "skyblue", font=high_font).grid(columnspan=10)
img = ImageTk.PhotoImage(Image.open("front1.png"))
panel = Label(root, image=img, background="skyblue", borderwidth=0)
panel.grid(columnspan=1)
wel = Label(root, text="Welcome", bg="skyblue", font=med_font).grid(columnspan=1)
dec_text_no = Label(root, text="1: ", font=sml_font, bg="skyblue").place(x=100,y=300)
dec_text = Label(root, text="Detection:", font=sml_font, bg="skyblue").place(x=120,y=300)
buton_detct = Button(root, text="Detection", font=sml_font, command=open_dectection).place(x=230, y=300)
train_text_no = Label(root, text="2: ", font=sml_font, bg="skyblue").place(x=100,y=330)
train_text = Label(root, text="Train the dataset:", font=sml_font, bg="skyblue").place(x=120,y=330)
buton_train = Button(root, text="Train", font=sml_font, command=open_train).place(x=230, y=330)
test_text_no = Label(root, text="3: ", font=sml_font, bg="skyblue").place(x=100,y=360)
test_text = Label(root, text="Test the dataset:", font=sml_font, bg="skyblue").place(x=120,y=360)
buton_test = Button(root, text="Test", font=sml_font, command=open_test).place(x=230, y=360)
button = Button(root, text="Done", font=sml_font, command=exit).place(x=180, y=390)

root.mainloop()
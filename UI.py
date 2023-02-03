import sys
import random
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from subprocess import call

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Feedback Machine")
root.config(bg="black")

Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=1)

title_frame = tk.Frame(root, bg="black")
title_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

left_frame = tk.Frame(root, bg="grey")
left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

left_middle_frame = tk.Frame(root, bg="grey")
left_middle_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

middle_frame = tk.Frame(root, bg="grey")
middle_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

right_middle_frame = tk.Frame(root, bg="grey")
right_middle_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

right_frame = tk.Frame(root, bg="grey")
right_frame.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

bottom_frame = tk.Frame(root, bg="grey")
bottom_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

image_excellent = PhotoImage(file="images/Ecstatic Face.png")
image_good = PhotoImage(file="images/Happy Face.png")
image_okay = PhotoImage(file="images/OK Face.png")
image_bad = PhotoImage(file="images/Not Happy Face.png")
image_very_bad = PhotoImage(file="images/Angry Face.png")
image_hallam_logo = PhotoImage(file="images/Project Logo.png")
image_back_button = PhotoImage(file="images/Back_To_Login.png")

label_top = Label(title_frame, bg="black", image=image_hallam_logo, padx=10, pady=10)
label_top.pack(fill="y", expand=True)

def RegisterResponseExcellent():
    print("Glad to hear it was excellent")

def RegisterResponseGood():
    print("Thanks for the feedback")

def RegisterResponseOkay():
    print("Thanks for the repsonse")

def RegisterResponseBad():
    print("Thanks for the feedback")

def RegisterResponseVeryBad():
    print("Sorry to hear it was bad")

def BackToLogin():
    root.destroy()
    call(["python3", "front_page.py"])

button_excellent = tk.Button(left_frame, text="Excellent", bg="green", activebackground="black", image=image_excellent, command=RegisterResponseExcellent)
button_excellent.pack(fill=tk.BOTH, expand=True)

button_good = tk.Button(left_middle_frame, text="Good", bg="lightgreen", activebackground="black", image=image_good , command=RegisterResponseGood)
button_good.pack(fill=tk.BOTH, expand=True)

button_straight = tk.Button(middle_frame, text="Okay", bg="yellow", activebackground="black", image=image_okay, command=RegisterResponseOkay)
button_straight.pack(fill=tk.BOTH, expand=True)

button_bad = tk.Button(right_middle_frame, text="Bad", bg="orange", activebackground="black", image=image_bad , command=RegisterResponseBad)
button_bad.pack(fill=tk.BOTH, expand=True)

button_very_bad = tk.Button(right_frame, text="Very Bad", bg="red", activebackground="black", image=image_very_bad , command=RegisterResponseBad)
button_very_bad.pack(fill=tk.BOTH, expand=True)

button_back = tk.Button(bottom_frame, bg="black", activebackground="black", image=image_back_button, borderwidth=0, command=BackToLogin)
button_back.pack(fill=tk.BOTH, expand=TRUE)

root.mainloop()
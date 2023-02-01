import sys
import random
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Feedback Machine")
root.config(bg="skyblue")

left_frame = tk.Frame(root, bg="grey")
left_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

left_middle_frame = tk.Frame(root, bg="grey")
left_middle_frame.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

middle_frame = tk.Frame(root, bg="grey")
middle_frame.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

right_middle_frame = tk.Frame(root, bg="grey")
right_middle_frame.grid(row=0, column=4, padx=10, pady=10, sticky=tk.W)

right_frame = tk.Frame(root, bg="grey")
right_frame.grid(row=0, column=5, padx=10, pady=10, sticky=tk.W)

root.columnconfigure(0, weight=1)
root.columnconfigure(6, weight=1)
root.rowconfigure(0, weight=1)

image_excellent = PhotoImage(file="download.png")
# image_good = PhotoImage(file="")
image_okay = PhotoImage(file="straight.png")
# image_bad = PhotoImage(file="")
image_very_bad = PhotoImage(file="Sad.png")

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

button_excellent = tk.Button(left_frame, text="Excellent", image=image_excellent, command=RegisterResponseExcellent)
button_excellent.pack(fill=tk.BOTH, expand=True)

# button_good = tk.button(left_middle_frame, text="Good", image= , command=RegisterResponseGood)
# button_good.pack(fill=tk.BOTH, expand=True)

button_straight = tk.Button(middle_frame, text="Okay", image=image_okay, command=RegisterResponseOkay)
button_straight.pack(fill=tk.BOTH, expand=True)

# button_bad = tk.button(right_middle_frame, text="Bad", image= , command=RegisterResponseBad)
# button_bad.pack(fill=tk.BOTH, expand=True)

button_very_bad = tk.Button(right_frame, text="Very Bad", image=image_very_bad , command=RegisterResponseBad)
button_very_bad.pack(fill=tk.BOTH, expand=True)

root.mainloop()
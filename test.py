import sys
import random
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Feedback Machine")
root.config(bg="skyblue")

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=1)

middle_frame = tk.Frame(root, bg="grey")
middle_frame.pack(fill=tk.BOTH, expand=True)

image_excellent = PhotoImage(file="Ecstatic Face.png")
image_good = PhotoImage(file="Happy Face.png")
image_okay = PhotoImage(file="OK Face.png")
image_bad = PhotoImage(file="Not Happy Face.png")
image_very_bad = PhotoImage(file="Angry Face.png")

def RegisterResponseExcellent():
    print("Glad to hear it was excellent")

def RegisterResponseBad():
    print("Sorry to hear it was bad")

button_excellent = tk.Button(middle_frame, text="Excellent", bg="green", activebackground="black", image=image_excellent)
button_excellent.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

button_good = tk.Button(middle_frame, text="Good", bg="lightgreen", activebackground="black", image=image_good)
button_good.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")

button_straight = tk.Button(middle_frame, text="Okay", bg="yellow", activebackground="black", image=image_okay)
button_straight.grid(row=0, column=2, padx=10, pady=10, sticky="nesw")

button_bad = tk.Button(middle_frame, text="Bad", bg="orange", activebackground="black", image=image_bad)
button_bad.grid(row=0, column=3, padx=10, pady=10, sticky="nesw")

button_very_bad = tk.Button(middle_frame, text="Very Bad", bg="red", activebackground="black", image=image_very_bad)
button_very_bad.grid(row=0, column=4, padx=10, pady=10, sticky="nesw")

root.mainloop()
import sys
import random
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("960x600")
root.title("Feedback Machine")
root.config(bg="skyblue")

left_frame = Frame(root, width=200, height=200, bg="grey")
left_frame.grid(row=0, column=1, padx=10, pady=10)

left_middle_frame = Frame(root, width=200, height=200, bg="grey")
left_middle_frame.grid(row=0, column=2, padx=10, pady=10)

middle_frame = Frame(root, width=200, height=200, bg="grey")
middle_frame.grid(row=0, column=3, padx=10, pady=10)

right_middle_frame = Frame(root, width=200, height=200, bg="grey")
right_middle_frame.grid(row=0, column=4, padx=10, pady=10)

right_frame = Frame(root, width=200, height=200, bg="grey")
right_frame.grid(row=0, column=5, padx=10, pady=10)

image_excellent = PhotoImage(file="download.png")
image_bad = PhotoImage(file="sad.png")

def RegisterResponexpand():
    print("Glad to hear it was excellent")

def RegisterResponseBad():
    print("Sorry to hear it was shit")

# button_qwer = Button(root, text="asdfasdf", image=image_excellent, command=RegisterResponseExcellent)
# button_qwer.pack()

# button_2 = Button(root, text="blah", image=image_bad , command=RegisterResponseBad)
# button_2.pack()

root.mainloop()



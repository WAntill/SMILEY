import sys
import os
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from subprocess import call
from PIL import Image,ImageTk

# makes sure the text box is empty at all times
session_id_text = ""


# def sing_in():
def set_id():
    # for now we check a txt file, change this to check DB
    input_file = open("group_codes.txt")
    Codes = input_file.readlines()

    # get the value of the global variable
    session_id_info = session_id.get()
    for code in Codes:
        if session_id_info in code:
            print(session_id_info)
            # do some shit to send it to DB and open an exec file
            # add fault handling
            portal.destroy()
            # call the other file with the reactions
            call(["python3", "UI.py"])
    messagebox.showerror("Login Error", "Group ID does not exist")

# backspace button logic
def backspace_press():
    global session_id_text
    # if the text box is not empty delete the character that appears on the
    # far right, and assign it to the session ID variable, otherwise do nothing
    if session_id_text != "":
        session_id_text = session_id.get()
        session_id_text = session_id_text[:-1]
        session_id.set(session_id_text)
    else:
        pass


# logic for when a key is pressed
def button_press(the_button):
    global session_id_text
    session_id_text = session_id_text + str(the_button)
    session_id.set(session_id_text)


# main page
portal = Tk()
portal.title("Feedback Machine")
portal.config(bg="black")
portal.attributes('-fullscreen', True)

# loading images for late use on the buttons
image_login = PhotoImage(file="images/Login.png")
image_backspace = PhotoImage(file="images/Backspace.png")
image_zero = PhotoImage(file="images/zero.png")
image_one = PhotoImage(file="images/One.png")
image_two = PhotoImage(file="images/two.png")
image_three = PhotoImage(file="images/three.png")
image_four = PhotoImage(file="images/four.png")
image_five = PhotoImage(file="images/five.png")
image_six = PhotoImage(file="images/six.png")
image_seven = PhotoImage(file="images/seven.png")
image_eight = PhotoImage(file="images/eight.png")
image_nine = PhotoImage(file="images/nine.png")


# set session ID text variable
session_id = StringVar()

Grid.rowconfigure(portal, 0, weight=1)
Grid.rowconfigure(portal, 1, weight=1)
Grid.rowconfigure(portal, 2, weight=1)
Grid.rowconfigure(portal, 3, weight=1)
Grid.rowconfigure(portal, 4, weight=1)
Grid.rowconfigure(portal, 5, weight=1)
Grid.rowconfigure(portal, 6, weight=1)
Grid.rowconfigure(portal, 7, weight=1)

Grid.columnconfigure(portal, 0, weight=1)
Grid.columnconfigure(portal, 1, weight=1)
Grid.columnconfigure(portal, 2, weight=1)
Grid.columnconfigure(portal, 3, weight=1)
Grid.columnconfigure(portal, 4, weight=1)

# Defining frames and their positions in order to map buttons for scaling
empty_left_frame = tk.Frame(portal, bg="black")
empty_left_frame.grid(row=0, rowspan=6, column=0)

empty_right_frame = tk.Frame(portal, bg="black")
empty_right_frame.grid(row=0, rowspan=6, column=4)

empty_bottom_frame = tk.Frame(portal, bg="black")
empty_bottom_frame.grid(row=7, column=0, columnspan=5)

# session_id_textbox_frame = tk.Frame(portal)
# session_id_textbox_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

button_seven_frame = tk.Frame(portal)
button_seven_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

button_eight_frame = tk.Frame(portal)
button_eight_frame.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

button_nine_frame = tk.Frame(portal)
button_nine_frame.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

button_four_frame = tk.Frame(portal)
button_four_frame.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

button_five_frame = tk.Frame(portal)
button_five_frame.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

button_six_frame = tk.Frame(portal)
button_six_frame.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

button_one_frame = tk.Frame(portal)
button_one_frame.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

button_two_frame = tk.Frame(portal)
button_two_frame.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

button_three_frame = tk.Frame(portal)
button_three_frame.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

button_backspace_frame = tk.Frame(portal)
button_backspace_frame.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

button_zero_frame = tk.Frame(portal)
button_zero_frame.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")

login_button_frame = tk.Frame(portal)
login_button_frame.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")

# the textbox for the session ID - this is so broken, needs some more looking into
session_id_textbox = Label(
    textvariable=session_id,
    borderwidth=3,
    relief="groove",
    font=("Amasis MT Std Black", 42),
    bg="black",
    fg="white"
)
session_id_textbox.grid(row=1, rowspan=2, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

# login button - need to replace with some art rather than mess with fonts
login_button = Button(login_button_frame, image=image_login, bg="black", activebackground="black", border=0, width=8, borderwidth=4, height=4, command=set_id)
login_button.pack(fill=tk.BOTH, expand=True)

# backspace button
button_backspace = Button(button_backspace_frame, image=image_backspace, bg="black", activebackground="black", border=0, width=8, borderwidth=4, height=4, command=lambda: backspace_press())
button_backspace.pack(fill=tk.BOTH, expand=True)

# number keys
button_zero = Button(button_zero_frame, image=image_zero, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("0"))
button_zero.pack(fill=tk.BOTH, expand=True)

button_one = Button(button_one_frame, image=image_one, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("1"))
button_one.pack(fill=tk.BOTH, expand=True)

button_two = Button(button_two_frame, image=image_two, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("2"))
button_two.pack(fill=tk.BOTH, expand=True)

button_three = Button(button_three_frame, image=image_three, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("3"))
button_three.pack(fill=tk.BOTH, expand=True)

button_four = Button(button_four_frame, image=image_four, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("4"))
button_four.pack(fill=tk.BOTH, expand=True)

button_five = Button(button_five_frame, image=image_five, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("5"))
button_five.pack(fill=tk.BOTH, expand=True)

button_six = Button(button_six_frame, image=image_six, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("6"))
button_six.pack(fill=tk.BOTH, expand=True)

button_seven = Button(button_seven_frame,image=image_seven, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("7"))
button_seven.pack(fill=tk.BOTH, expand=True)

button_eight = Button(button_eight_frame, image=image_eight, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("8"))
button_eight.pack(fill=tk.BOTH, expand=True)

button_nine = Button(button_nine_frame, image=image_nine, bg="black", activebackground="black", border=0, width=8, height=4, borderwidth=4, command=lambda: button_press("9"))
button_nine.pack(fill=tk.BOTH, expand=True)


portal.mainloop()
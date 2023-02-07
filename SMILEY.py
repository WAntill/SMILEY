import sys
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from subprocess import call

# makes sure the text box is empty at all times
session_id_text = ""

# def sing_in():
def set_id():
    global session_id_text
    # for now we check a txt file, change this to check DB
    input_file = open("group_codes.txt")
    Codes = input_file.readlines()

    # get the value of the global variable
    session_id_info = session_id.get()
    for code in Codes:
        #strip the code of the "\n"
        code = code.strip("\n")
        if session_id_info == code:
            session_id_text = ""
            session_id.set(session_id_text)            
            main_frame.tkraise()

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

# set session ID text variable
session_id = StringVar()

main_frame = tk.Frame(root, bg="black")
main_frame.grid(row=0, rowspan=3, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

front_frame = tk.Frame(root, bg="black")
front_frame.grid(row=0, rowspan=3, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

Grid.rowconfigure(front_frame, 0, weight=1)
Grid.rowconfigure(front_frame, 1, weight=1)
Grid.rowconfigure(front_frame, 2, weight=1)
Grid.rowconfigure(front_frame, 3, weight=1)
Grid.rowconfigure(front_frame, 4, weight=1)
Grid.rowconfigure(front_frame, 5, weight=1)
Grid.rowconfigure(front_frame, 6, weight=1)
Grid.rowconfigure(front_frame, 7, weight=1)

Grid.columnconfigure(front_frame, 0, weight=1)
Grid.columnconfigure(front_frame, 1, weight=1)
Grid.columnconfigure(front_frame, 2, weight=1)
Grid.columnconfigure(front_frame, 3, weight=1)
Grid.columnconfigure(front_frame, 4, weight=1)

Grid.rowconfigure(main_frame, 0, weight=1)
Grid.rowconfigure(main_frame, 1, weight=1)
Grid.rowconfigure(main_frame, 2, weight=1)

Grid.columnconfigure(main_frame, 0, weight=1)
Grid.columnconfigure(main_frame, 1, weight=1)
Grid.columnconfigure(main_frame, 2, weight=1)
Grid.columnconfigure(main_frame, 3, weight=1)
Grid.columnconfigure(main_frame, 4, weight=1)

title_frame = tk.Frame(main_frame, bg="black")
title_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

left_frame = tk.Frame(main_frame, bg="grey")
left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

left_middle_frame = tk.Frame(main_frame, bg="grey")
left_middle_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

middle_frame = tk.Frame(main_frame, bg="grey")
middle_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

right_middle_frame = tk.Frame(main_frame, bg="grey")
right_middle_frame.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

right_frame = tk.Frame(main_frame, bg="grey")
right_frame.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

bottom_frame = tk.Frame(main_frame, bg="grey")
bottom_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# Defining frames and their positions in order to map buttons for scaling
empty_left_frame = tk.Frame(front_frame, bg="black")
empty_left_frame.grid(row=0, rowspan=6, column=0)

empty_right_frame = tk.Frame(front_frame, bg="black")
empty_right_frame.grid(row=0, rowspan=6, column=4)

empty_bottom_frame = tk.Frame(front_frame, bg="black")
empty_bottom_frame.grid(row=7, column=0, columnspan=5)

# session_id_textbox_frame = tk.Frame(front_frame)
# session_id_textbox_frame.grid(row=1, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

button_seven_frame = tk.Frame(front_frame)
button_seven_frame.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

button_eight_frame = tk.Frame(front_frame)
button_eight_frame.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

button_nine_frame = tk.Frame(front_frame)
button_nine_frame.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

button_four_frame = tk.Frame(front_frame)
button_four_frame.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

button_five_frame = tk.Frame(front_frame)
button_five_frame.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

button_six_frame = tk.Frame(front_frame)
button_six_frame.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

button_one_frame = tk.Frame(front_frame)
button_one_frame.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

button_two_frame = tk.Frame(front_frame)
button_two_frame.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

button_three_frame = tk.Frame(front_frame)
button_three_frame.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")

button_backspace_frame = tk.Frame(front_frame)
button_backspace_frame.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

button_zero_frame = tk.Frame(front_frame)
button_zero_frame.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")

login_button_frame = tk.Frame(front_frame)
login_button_frame.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")

image_excellent = PhotoImage(file="images/Ecstatic Face.png")
image_good = PhotoImage(file="images/Happy Face.png")
image_okay = PhotoImage(file="images/OK Face.png")
image_bad = PhotoImage(file="images/Not Happy Face.png")
image_very_bad = PhotoImage(file="images/Angry Face.png")
image_hallam_logo = PhotoImage(file="images/Project Logo.png")
image_back_button = PhotoImage(file="images/Back_To_Login.png")

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
    front_frame.tkraise()

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
button_back.pack(fill=tk.BOTH, expand=TRUE)# the textbox for the session ID - this is so broken, needs some more looking into

session_id_textbox = Label(
    front_frame,
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

root.mainloop()
import sys
import os
import random
from tkinter import *
from tkinter import messagebox
from subprocess import call

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


def backspace_press():
    # backspace button logic
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
portal.config(bg="#b61c54")
portal.geometry("840x600")

# set session ID text variable
session_id = StringVar()

# the textbox for the session ID - this is so broken, needs some more looking into
session_id_textbox = Label(
    textvariable=session_id,
    borderwidth=3,
    relief="groove",
    font=("Arial", 42),
    width=9,
    height=0,
)
session_id_textbox.grid(row=1, column=0, columnspan=4)

# no idea how to center the grid tbch
# login button - need to replace with some art rather than mess with fonts
login_button = Button(
    portal, text="Login", width=8, borderwidth=4, height=4, command=set_id
)
login_button.grid(row=6, column=2)
# backspace button
button_backspace = Button(
    text="<-", width=8, borderwidth=4, height=4, command=lambda: backspace_press()
)
button_backspace.grid(row=6, column=0)

# number keys
button_zero = Button(
    text="0", width=8, height=4, borderwidth=4, command=lambda: button_press("0")
)
button_zero.grid(row=6, column=1)
button_one = Button(
    text="1", width=8, height=4, borderwidth=4, command=lambda: button_press("1")
)
button_one.grid(row=5, column=0)
button_two = Button(
    text="2", width=8, height=4, borderwidth=4, command=lambda: button_press("2")
)
button_two.grid(row=5, column=1)
button_three = Button(
    text="3", width=8, height=4, borderwidth=4, command=lambda: button_press("3")
)
button_three.grid(row=5, column=2)
button_four = Button(
    text="4", width=8, height=4, borderwidth=4, command=lambda: button_press("4")
)
button_four.grid(row=4, column=0)
button_five = Button(
    text="5", width=8, height=4, borderwidth=4, command=lambda: button_press("5")
)
button_five.grid(row=4, column=1)
button_six = Button(
    text="6", width=8, height=4, borderwidth=4, command=lambda: button_press("6")
)
button_six.grid(row=4, column=2)
button_seven = Button(
    text="7", width=8, height=4, borderwidth=4, command=lambda: button_press("7")
)
button_seven.grid(row=3, column=0)
button_eight = Button(
    text="8", width=8, height=4, borderwidth=4, command=lambda: button_press("8")
)
button_eight.grid(row=3, column=1)
button_nine = Button(
    text="9", width=8, height=4, borderwidth=4, command=lambda: button_press("9")
)
button_nine.grid(row=3, column=2)


portal.mainloop()

import sys
import os
import random
from tkinter import *
from subprocess import call


def sing_in():
    def set_id():
        session_id_info = session_id.get()
        print(session_id_info)
        # do some shit to send it to DB and open an exec file
        # add fault handling
        portal.destroy()
        # call the other file with the reactions
        call(["python3", "UI.py"])

    # open a seperate toplevel window
    signin_screen = Toplevel(portal)
    signin_screen.title("Login")
    signin_screen.geometry("300x260")

    # set session ID text variable
    session_id = StringVar()

    # set up user instructions
    instruction = Label(signin_screen, text="Session ID *", bg="pink").pack()
    # set up entry point for the login screen
    username_entry = Entry(signin_screen, textvariable=session_id)
    username_entry.pack()
    # confirm button
    signin_button = Button(
        signin_screen, text="Sign In", width=10, height=1, command=set_id
    ).pack()


# main page
portal = Tk()
portal.title("Feedback Machine")
portal.config(bg="skyblue")
portal.geometry("840x600")
# create Login Button that stays in the center
login_button = Button(
    portal, text="Login", height="5", width="30", font=("Arial", 24), command=sing_in
).place(relx=0.5, rely=0.5, anchor=CENTER)

portal.mainloop()

# Daksh Parikh
# This is a GUI application that will let user to login, create new_account, edit and delete account
# with the help of the Mongodb that provides backend support to this application.
# For this I'm using pymongo library and for GUI tkinter

import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from pymongo import MongoClient
import projectmodule

def edit_db():   # edit button function to edit the record

    user = usename_txt.get()
    pas = password_txt.get()
    projectmodule.edit(user,pas)

    usename_txt.delete(0,"end")
    usename_txt.insert(0,"")
    password_txt.delete(0,"end")
    password_txt.insert(0,"")


def login(): # login button function for login the user

    user = usename_txt.get()
    pas = password_txt.get()
    projectmodule.log_in(user,pas)

    usename_txt.delete(0,"end")
    usename_txt.insert(0,"")
    password_txt.delete(0,"end")
    password_txt.insert(0,"")


def new_account(): # create button function for creat new user
    projectmodule.create()

    usename_txt.delete(0,"end")
    usename_txt.insert(0,"")
    password_txt.delete(0,"end")
    password_txt.insert(0,"")


if __name__ == "__main__":
    # Welcome Screen
    window = tk.Tk()

    window.minsize(450, 300)

    window.title("GUI")

    intro_lbl = tk.Label(window, text = "Welcome to the GUI")
    intro_lbl.grid(row = 0, column = 1)

    usename_lbl = tk.Label(window, text = "Username:")
    usename_lbl.grid(row = 1, column = 0)
    usename_txt = tk.Entry(window)
    usename_txt.grid(row = 1, column = 1)

    password_lbl = tk.Label(window, text = "Password:")
    password_lbl.grid(row = 2, column = 0)
    password_txt = tk.Entry(window)
    password_txt.grid(row = 2, column = 1)

    login_btn = tk.Button(window, text="login", command=login)
    login_btn.grid(column=1, row=3)


    new_btn = tk.Button(window, text="creat account", command=new_account)
    new_btn.grid(column=1, row=4)

    edit_btn = tk.Button(window, text="Edit", command=edit_db)
    edit_btn.grid(column=1, row=5)

    window.mainloop()

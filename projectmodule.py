# They can be created and destroyed dynamically, passed to other functions, returned as values, etc.
# Python supports the concept of a "nested function" or "inner function",
# which is simply a function defined inside another function.

# I'm using because it simples the code. In tkinter if we want to deal with multiple screens and
# if each screen has different task so it's bothe easy and smart thing to use nested function.
# It will save both your energy and time. Otherwise we have to write code that will had too long and
# both hard to do and understand so, it's important to use function within a functions

# I'm using in two functions,
# the first function will be create function that will use to insert new data in database and
# the second function is edit, in that function I'm using two other function
# 1) that will edit database 2) delete from the database


import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
from pymongo import MongoClient


def log_in(user,pas):
    client = MongoClient()

    client = MongoClient('mongodb://localhost:27017') # connecting to database

    db = client.pyprojecttest

    posts = db.posts
    info = posts.find_one({"username": user})
    if info is None: # validating user's credential
        tk.messagebox.showinfo(message='Username does not exist')
    else:
        if pas == info['password']:
            # login window
            window = tk.Tk()

            window.minsize(450, 300)

            window.title("Info GUI")

            lbl_text = "Welcome " + info['username']
            Welcome_lbl = tk.Label(window, text = lbl_text) # if username and password is correct than it will go in new screen
            Welcome_lbl.grid(row = 0, column = 1)

            window.mainloop()

        else:
            tk.messagebox.showinfo(message='Wrong password')


def create(): # function that will create records

    window = tk.Tk()

    window.minsize(450, 300)

    window.title("Create GUI")

    intro_lbl1 = tk.Label(window, text = "Create an acount")
    intro_lbl1.grid(row = 0, column = 1)

    firstname_lbl1 = tk.Label(window, text = "First Name:")
    firstname_lbl1.grid(row = 1, column = 0)
    firstname_txt1 = tk.Entry(window)
    firstname_txt1.grid(row = 1, column = 1)

    lastname_lbl1 = tk.Label(window, text = "Last Name:")
    lastname_lbl1.grid(row = 2, column = 0)
    lastname_txt1 = tk.Entry(window)
    lastname_txt1.grid(row = 2, column = 1)

    email_lbl1 = tk.Label(window, text = "Email Id:")
    email_lbl1.grid(row = 3, column = 0)
    email_txt1 = tk.Entry(window)
    email_txt1.grid(row = 3, column = 1)

    usename_lbl1 = tk.Label(window, text = "Username:")
    usename_lbl1.grid(row = 4, column = 0)
    usename_txt1 = tk.Entry(window)
    usename_txt1.grid(row = 4, column = 1)

    password_lbl1 = tk.Label(window, text = "Password:")
    password_lbl1.grid(row = 5, column = 0)
    password_txt1 = tk.Entry(window)
    password_txt1.grid(row = 5, column = 1)

    def clicked(): # function within a function to insert an new data

        client = MongoClient()

        client = MongoClient('mongodb://localhost:27017') # connecting to database

        db = client.pyprojecttest

        posts = db.posts
        post_data = {
            'username': usename_txt1.get(),
            'password': password_txt1.get(),
            'first_name': firstname_txt1.get(),
            'last_name': lastname_txt1.get(),
            'email': email_txt1.get()
            }
        result = posts.insert_one(post_data) #insering record in database
        print('One post: {0}'.format(result.inserted_id))
        window.destroy()

    submit_btn = tk.Button(window, text="Submit", command=clicked)
    submit_btn.grid(column=1, row=6)
    window.mainloop()



def edit(user,pas): #take username and password in parameter and update record in databas
    client = MongoClient()

    client = MongoClient('mongodb://localhost:27017') # connecting to database

    db = client.pyprojecttest

    posts = db.posts
    info = posts.find_one({"username": user})
    if info is None:
        tk.messagebox.showinfo(message='Username does not exist')
    else:
        if pas == info['password']:
            # edit window
            window = tk.Tk()

            window.minsize(450, 300)

            window.title("Edit GUI")

            intro_lbl2 = tk.Label(window, text = "Your Information")
            intro_lbl2.grid(row = 0, column = 1)

            firstname_lbl2 = tk.Label(window, text = "First Name:")
            firstname_lbl2.grid(row = 1, column = 0)
            firstname_txt2 = tk.Entry(window)
            firstname_txt2.grid(row = 1, column = 1)

            lastname_lbl2 = tk.Label(window, text = "Last Name:")
            lastname_lbl2.grid(row = 2, column = 0)
            lastname_txt2 = tk.Entry(window)
            lastname_txt2.grid(row = 2, column = 1)

            email_lbl2 = tk.Label(window, text = "Email Id:")
            email_lbl2.grid(row = 3, column = 0)
            email_txt2 = tk.Entry(window)
            email_txt2.grid(row = 3, column = 1)

            usename_lbl2 = tk.Label(window, text = "Username:")
            usename_lbl2.grid(row = 4, column = 0)
            usename_txt2 = tk.Entry(window)
            usename_txt2.grid(row = 4, column = 1)

            password_lbl2 = tk.Label(window, text = "Password:")
            password_lbl2.grid(row = 5, column = 0)
            password_txt2 = tk.Entry(window)
            password_txt2.grid(row = 5, column = 1)

            usename_txt2.delete(0,"end")
            usename_txt2.insert(0,info['username'])
            password_txt2.delete(0,"end")
            password_txt2.insert(0,info['password'])
            firstname_txt2.delete(0,"end")
            firstname_txt2.insert(0,info['first_name'])
            lastname_txt2.delete(0,"end")
            lastname_txt2.insert(0,info['last_name'])
            email_txt2.delete(0,"end")
            email_txt2.insert(0,info['email'])

            def ubdate_db(): # function within function to Update button to update record in database

                myquery = {
                            'username': info['username'],
                            'password': info['password'],
                            'first_name': info['first_name'],
                            'last_name': info['last_name'],
                            'email': info['email']
                            }
                newvalues = { "$set": {
                                        'username': usename_txt2.get(),
                                        'password': password_txt2.get(),
                                        'first_name': firstname_txt2.get(),
                                        'last_name': lastname_txt2.get(),
                                        'email': email_txt2.get()
                                        } }

                posts.update_one(myquery, newvalues) # update query
                print("done")
                window.destroy()

            def delete_db(): # function within a function to Delete button to delete record in database
                myquery = { 'username': info['username'] }
                posts.delete_one(myquery) # deleting a query
                print("delete")
                window.destroy()

            update_btn = tk.Button(window, text="Update", command=ubdate_db)
            update_btn.grid(column=1, row=6)

            delete_btn = tk.Button(window, text="Delete", command=delete_db)
            delete_btn.grid(column=1, row=7)

            window.mainloop()

        else:
            tk.messagebox.showinfo(message='Wrong password')

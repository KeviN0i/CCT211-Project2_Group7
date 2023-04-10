import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import sys, math
from tkinter import ttk
import csv
import tkinter.messagebox as messagebox 
import pandas as pd
from Clients import create_hotel_mgm_csv_reader_frame
from Mainpage import Main_page

"""
CCT211 Group Project 2 Group 7
Group Members:
Junkai Zhang
Runqi Yang
Yutong Zhang
Xingzhe Zhao

Start from Login Page 
"""


# Basics
loginroot = tk.Tk()
loginroot.title("Login form")
loginroot.geometry('1200x600+650+300')
loginroot.resizable(False, False)

# Login functoin
def login():
    # Account and password
    username = "12345"
    password = "12345"

    # Check conditions 
    if usernameEntry.get()==username and passwordEntry.get()==password:
        messagebox.showinfo(title="Login Success", message="Welcome")

        #Destroy the old page 
        loginroot.destroy()

        #The new page replace the current login page
        Main_page()
        
    # Display error message
    else:
        messagebox.showerror(title="Login Failed", message="Invalid login.")

# Show password Function
def showPassword():
    if showPassword_var.get() ==1:
        passwordEntry.config(show = "")
    else:
        passwordEntry.config(show = "*")

loginframe = tk.Frame()
# widgets
#Images
canvas = tk.Canvas(loginroot, width=500, height=350)
canvas.pack (side = "right", padx = 75, pady = 50)
photo = tk.PhotoImage(file="hotel.png")  
canvas.create_image(10, 10, image=photo)

# Login label
loginLabel = tk.Label(loginframe, text="Hotel Management",fg="#000",font=("Helvetica",34))
loginLabel.grid(row=0,column=0,columnspan=2,sticky="news",pady=40,padx = 100)

loginLabel2 = tk.Label(loginframe, text="Admin Login",fg="#000",font=("Verdana",12))
loginLabel2.grid(row=1,column=0,pady=10,padx=30)

# Username Label
usernameLabel = tk.Label(loginframe, text="Username",fg="#000",font=("Verdana",14))
usernameLabel.grid(row=1,column=0,padx=30)

# Password label
passwordLabel = tk.Label(loginframe, text="Password",fg="#000",font=("Verdana",14))
passwordLabel.grid(row=2,column=0,padx=30)

# Username Entry label
usernameEntry = tk.Entry(loginframe, font=("Verdana",16))
usernameEntry.grid(row=1,column=1,pady=20)

# Password label
passwordEntry = tk.Entry(loginframe, show="*", font=("Verdana",16))
passwordEntry.grid(row=2,column=1,pady=20)

# Showpassword Button
showPassword_var = IntVar()
show_password_checkbox = Checkbutton(loginframe,text="Show password",variable=showPassword_var,command=showPassword,font=("Verdana", 8))
show_password_checkbox.grid(row=3,column=1,columnspan=2)

# Login Button
loginButton = tk.Button(loginframe, text="Login",fg="#000",font=("Verdana", 16),command=login)
loginButton.grid(row=4,column=0,columnspan=2,pady=30)

# The login frame will be placed on the left, while the image is displayed on the right
loginframe.pack(side = "left")

# Background color
# root.configure(bg='#000')
loginroot.mainloop()

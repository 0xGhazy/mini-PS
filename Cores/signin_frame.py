
# Coded by: 
# Tested by: hossam hamdy
# coding style: PEP-008

import os
import sqlite3
from tkinter import *
from getpass import getuser
from tkinter import messagebox
from functions import read_json, calc_hash, backup, logger

# reading pathes from
os.chdir(os.path.dirname(__file__))
pathes = read_json(r"Profile.json")
DATABASE_PATH = pathes["DATABASE_PATH"]

def close():
    """Closing the frame"""
    logger("Info", "signin_frame.py has been closed.")
    exit()


def clear():
	messagebox.showinfo(title='delete', message='Do you want to clear?')
	username_text.delete(0, END)
	password_text.delete(0, END)


def login():
	if username_text.get() == "" or password_text.get() == "":
		messagebox.showerror("[-] Error" , "All Fields Are Required" , parent = signin_window)
		logger("Info", "signin_frame.py All Fields Are Required error.")
	else:
		try:
            # connect to database.
			con = sqlite3.connect(DATABASE_PATH)
			c = con.cursor()
			# c = fname, lname, username, email_address, password
			for row in c.execute("Select * from users_info"):
				uname = row[2] # = username
				upass = row[4] # = password
				if username_text.get() == uname and calc_hash(password_text.get(), "sha256") == upass:
					messagebox.showinfo("[+] Login" , "You have Logged in successfully." , parent = signin_window)
					logger("Info", f"signin_frame.py > login successfully with ({username_text.get()}, {password_text.get()})")
					# adding backup function here.
					# calling backup function.
					backup(row[3])
					backup_path = r"C:\Users\{0}\Desktop\Backup.txt".format(getuser())
					if os.path.isfile(backup_path):
						messagebox.showinfo("[+] Done" , "Backup has created successfully." , parent = signin_window)
						logger("Info", "signin_frame.py > backup file was created successfully.")
						exit()
					else:
						messagebox.showerror("[-] Not found" , "Backup.txt file wasn't exist." , parent = signin_window)
						logger("Warning", "signin_frame.py > Backup.txt file wasn't exist. an error has occurred.")
				else:
					pass
			messagebox.showerror("[-] Not found" , "The username or password is incorrect" , parent = signin_window)
			logger("Warning", "signin_frame.py > The username or password is incorrect")
		except Exception as error:
			messagebox.showerror('[-] Error', str(error))
			logger("Warning", f"signin_frame.py > an error was occurred\n\n{error}\n\n")


# taking object from tkinter
signin_window = Tk()
# set frame title
signin_window.title("mini-PS: Sign in")
# set geometry.
signin_window.maxsize(width=500 ,  height=250)
signin_window.minsize(width=500 ,  height=250)
# Set Title 'label'
heading = Label(signin_window , text = "mini-PS Signin" , font = 'Verdana 20 bold')
heading.place(x=140 , y=10)


username_lbl = Label(signin_window, text = "Username: " , font = 'Verdana 10 bold')
username_lbl.place(x = 80, y = 90)
username_text = Entry(signin_window, width = 40)
username_text.place(x=200 , y=95)

password_lbl = Label(signin_window, text = "Password: " , font = 'Verdana 10 bold')
password_lbl.place(x = 80, y = 130)
password_text = Entry(signin_window, width = 40 , show="*")
password_text.place(x = 200 , y = 130)

# handling login
btn_signin = Button(signin_window, text = "Login", font = 'Verdana 10 bold', command = login)
btn_signin.place(x = 200, y = 180)

# handling clear button
btn_clear = Button(signin_window, text = "Clear", font = 'Verdana 10 bold', command = clear)
btn_clear.place(x = 280, y = 180)

# handling close button
close_btn = Button(signin_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x = 350, y = 180)

mainloop()

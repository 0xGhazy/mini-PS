from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from functions import read_json, calc_hash, backup


os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")
DATABASE_PATH = pathes["DATABASE_PATH"]
feedback_path = 000000000

def close():
	exit()

def clear():
	messagebox.showinfo(title='delete', message='Do you want to clear?')
	username_text.delete(0, END)
	password_text.delete(0, END)

def login():
	username_text.get()
	password_text.get()
	if username_text.get() == "" or password_text.get() == "":
		messagebox.showerror("[-] Error" , "All Fields Are Required" , parent = signin_window)	
	else:
		try:
            # connect to database.
			con = sqlite3.connect(DATABASE_PATH)
			c = con.cursor()
			for row in c.execute("Select * from users_info"):
				uname = row[2]
				upass = row[4]
				if username_text.get() == uname and calc_hash(password_text.get(), "sha256") == upass:
					messagebox.showinfo("[+] Login" , "You have Logged in successfully." , parent = signin_window)
					backup()
					messagebox.showinfo("[+] Done" , "Backup has created successfully." , parent = signin_window)
					exit()
				else:
					pass
			messagebox.showerror("[-] Not found" , "The username or password is incorrect" , parent = signin_window)

		except Exception as error:
			messagebox.showerror('[-] Error', str(error))


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

# frame vars
username = StringVar()
password = StringVar()

username_lbl = Label(signin_window, text = "Username: " , font = 'Verdana 10 bold')
username_lbl.place(x=80,y=90)
username_text = Entry(signin_window, width = 40 , textvariable = username)
username_text.place(x=200 , y=95)

password_lbl = Label(signin_window, text = "Password: " , font = 'Verdana 10 bold')
password_lbl.place(x=80,y=130)
password_text = Entry(signin_window, width = 40 , show="*s", textvariable = password)
password_text.place(x=200 , y=130)

# handling buttons
btn_signup = Button(signin_window, text = "Login", font = 'Verdana 10 bold', command = login)
btn_signup.place(x=200, y=180)
btn_clear = Button(signin_window, text = "Clear", font = 'Verdana 10 bold', command = clear)
btn_clear.place(x=280, y=180)
close_btn = Button(signin_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=350, y=180)


mainloop()
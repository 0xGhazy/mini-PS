
# Coded By:
# Tested by: Hossam hamdy
# Coding style: PEP-008


from tkinter import *
from tkinter import messagebox
import sqlite3
import os
from functions import read_json, calc_hash, logger


os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")
DATABASE_PATH = pathes["DATABASE_PATH"]


def close():
    """Closing the frame"""
    logger("Info", "signup_frame.py has been closed.")
    exit()


def signup():
	# check if Text = Null
	if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or \
	   email_address.get() == "" or user_password_txt.get() == "" or user_password2_txt.get() == "":
		messagebox.showerror("Error" , "All Fields Are Required" , parent = signup_window)
		logger("Info", "signup_frame.py > All Fields Are Required message appears.")
	else:
		if user_password_txt.get() != user_password2_txt.get():
			messagebox.showerror("[-] Error" , "Passwords don't matches", parent = signup_window)
			logger("Info", "signup_frame.py > passwords don't matches error occurred.")
		else:
			try:
				# connect to database.
				con = sqlite3.connect(DATABASE_PATH)
				cur = con.cursor()
				cur.execute("""CREATE TABLE IF NOT EXISTS users_info(fname text, lname text, username TEXT UNIQUE, email_address TEXT UNIQUE, password TEXT)""")
				con.commit()

				# inserting data into table
				cur.execute("INSERT INTO users_info VALUES (:fname, :lname, :username, :email_address, :password)", {
											'fname': first_name.get(),
											'lname': last_name.get(),
											'username': user_name.get(),
											'email_address':  email_address.get(),
											'password': calc_hash(user_password_txt.get(), "sha256")}) # hashing password for more safety.
				con.commit()
				x = calc_hash(user_password_txt.get(), "sha256")
				messagebox.showinfo("[+] Success" , "Ragistration Successfull" , parent = signup_window)
				logger("Info", f"signup_frame.py > a new data was inserted successfully: ({first_name.get()}, {last_name.get()}, {user_name.get()}, {email_address.get()}, {x})")
				exit()
			except Exception as error:
				messagebox.showerror("[-] Error" , f"Error Dui to : {str(error)}", parent = signup_window)
				logger("Warning", f"signup_frame.py > an error was occurred.\n{error}\n")


# clear data function
def clear():
	first_name.delete(0,END)
	last_name.delete(0,END)
	user_name.delete(0,END)
	email_address.delete(0,END)
	user_password_txt.delete(0,END)
	user_password2_txt.delete(0,END)



# taking object from tkinter
signup_window = Tk()
# set frame title
signup_window.title("mini-PS: Sign Up")
# set geometry.
signup_window.maxsize(width=500 ,  height=400)
signup_window.minsize(width=500 ,  height=400)
# Set Title 'label'
heading = Label(signup_window , text = "mini-PS Signup" , font = 'Arial 20 bold')
heading.place(x=140 , y=30)

# fname-> set label.
first_name = Label(signup_window, text = "First Name :" , font = 'Arial 10 bold')
first_name.place(x=80,y=130)
# fname-> set text entry.
first_name = Entry(signup_window, width = 40)
first_name.place(x=200 , y=133)

# lname-> set label.
last_name = Label(signup_window, text = "Last Name :" , font = 'Arial 10 bold')
last_name.place(x=80,y=160)
# lname-> set text entry.
last_name = Entry(signup_window, width = 40)
last_name.place(x=200 , y=163)

# username-> set label.
user_name = Label(signup_window, text = "Username :" , font = 'Arial 10 bold')
user_name.place(x=80,y=190)
# username-> set text entry.
user_name = Entry(signup_window, width = 40)
user_name.place(x=200 , y=193)

# email_address-> set email label.
email_address = Label(signup_window, text = "Email address :" , font='Arial 10 bold')
email_address.place(x=80,y=220)
# email_address-> set email text entry.
email_address = Entry(signup_window, width=40)
email_address.place(x= 200 , y= 223)

user_password_lbl = Label(signup_window, text = "Password :" , font='Arial 10 bold')
user_password_lbl.place(x=80,y=250)
# email_address-> set email text entry.
user_password_txt = Entry(signup_window, width=40, show="*")
user_password_txt.place(x= 200 , y= 253)

user_password2_lbl = Label(signup_window, text= "Re-Password :" , font='Arial 10 bold')
user_password2_lbl.place(x=80,y=280)
# email_address-> set email text entry.
user_password2_txt = Entry(signup_window, width=40, show="*")
user_password2_txt.place(x= 200 , y= 283)


btn_signup = Button(signup_window, text = "Signup", font = 'Arial 10 bold', command=signup)
btn_signup.place(x=200, y=320)

btn_clear = Button(signup_window, text = "Clear", font = 'Arial 10 bold', command = clear)
btn_clear.place(x=280, y=320)

btn_close = Button(signup_window, text = "Close", font = 'Arial 10 bold', command = close)
btn_close.place(x=350, y=320)

# calling our program.
mainloop()

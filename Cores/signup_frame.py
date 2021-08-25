from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def signup():

    # check if all fields are valide.
	if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or emailAddress.get() == "":
		messagebox.showerror("Error" , "All Fields Are Required" , parent = signup_window)

	else:
		try:
			con = sqlite3.connect()
			cur = con.cursor()
			cur.execute("select * from user_information where username=%s",user_name.get())
			row = cur.fetchone()
			if row!=None:
				messagebox.showerror("Error" , "User Name Already Exits", parent = signup_window)
			else:
				cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
					(first_name.get(), last_name.get(), age.get(), var.get(), city.get(), add.get(), user_name.get(), password.get()))
				con.commit()
				con.close()
				messagebox.showinfo("Success" , "Ragistration Successfull" , parent = signup_window)
				clear()
				switch()
				
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = signup_window)

# # close signup function			
# def switch():
# 	signup_window.destroy()

# # clear data function
# def clear():
# 	first_name.delete(0,END)
# 	last_name.delete(0,END)
# 	var.set("Male")
# 	add.delete(0,END)
# 	user_name.delete(0,END)
# 	password.delete(0,END)
# 	very_pass.delete(0,END)




#-----------------------#
# Our frame starts here #
#-----------------------#


# taking object from tkinter
signup_window = Tk()
# set frame title
signup_window.title("mini-PS: Sign Up")
# set geometry.
signup_window.maxsize(width=500 ,  height=400)
signup_window.minsize(width=500 ,  height=400)


# Set Title 'label'
heading = Label(signup_window , text = "mini-PS Signup" , font = 'Verdana 20 bold')
heading.place(x=140 , y=60)



# frame vars
first_name = StringVar()
last_name = StringVar()
user_name = StringVar()
emailAddress = StringVar()




# fname-> set label.
first_name = Label(signup_window, text = "First Name :" , font = 'Verdana 10 bold')
first_name.place(x=80,y=130)
# fname-> set text entry.
first_name = Entry(signup_window, width = 40 , textvariable = first_name)
first_name.place(x=200 , y=133)


# lname-> set label.
last_name = Label(signup_window, text = "Last Name :" , font = 'Verdana 10 bold')
last_name.place(x=80,y=160)
# lname-> set text entry.
last_name = Entry(signup_window, width = 40 , textvariable = last_name)
last_name.place(x=200 , y=163)


# username-> set label.
user_name = Label(signup_window, text = "Username :" , font = 'Verdana 10 bold')
user_name.place(x=80,y=190)
# username-> set text entry.
user_name = Entry(signup_window, width = 40, textvariable = user_name)
user_name.place(x=200 , y=193)


# email_address-> set email label.
email_address = Label(signup_window, text= "Email address :" , font='Verdana 10 bold')
email_address.place(x=80,y=220)
# email_address-> set email text entry.
email_address = Entry(signup_window, width=40,textvariable = emailAddress)
email_address.place(x= 200 , y= 223)


# handling buttons
btn_signup = Button(signup_window, text = "Signup", font = 'Verdana 10 bold')
btn_signup.place(x=200, y=280)

btn_clear = Button(signup_window, text = "Clear", font = 'Verdana 10 bold')
btn_clear.place(x=280, y=280)

sign_up_btn = Button(signup_window , text = "Switch To Login")
sign_up_btn.place(x=350 , y =20)


signup_window.mainloop()

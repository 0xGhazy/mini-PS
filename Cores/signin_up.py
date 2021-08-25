from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql


#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
            # connect to database.
			con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
			cur = con.cursor()

			cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
                # to action
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

#---------------------------------------------------------------End Login Function ---------------------------------



#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
	# signup database connect 
	def action():
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
				cur = con.cursor()
				cur.execute("select * from user_information where username=%s",user_name.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
					cur.execute("insert into user_information(first_name,last_name,age,gender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						age.get(),
						var.get(),
						city.get(),
						add.get(),
						user_name.get(),
						password.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)

	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("Male")
		city.delete(0,END)
		add.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)


	# start Signup Window	

	winsignup = Tk()
	winsignup.title("Docter Appointment App")
	winsignup.maxsize(width=500 ,  height=600)
	winsignup.minsize(width=500 ,  height=600)


	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
	heading.place(x=80 , y=60)

	# form data label
	first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
	first_name.place(x=80,y=130)

	last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
	last_name.place(x=80,y=160)

	age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
	age.place(x=80,y=190)

	Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
	Gender.place(x=80,y=220)

	city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
	city.place(x=80,y=260)

	add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
	add.place(x=80,y=290)

	user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
	user_name.place(x=80,y=320)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
	password.place(x=80,y=350)

	very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
	very_pass.place(x=80,y=380)

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	age = IntVar(winsignup, value='0')
	var= StringVar()
	city= StringVar()
	add = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=200 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=200 , y=163)

	
	age = Entry(winsignup, width=40, textvariable=age)
	age.place(x=200 , y=193)

	
	Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
	Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)


	city = Entry(winsignup, width=40,textvariable = city)
	city.place(x=200 , y=263)


	
	add = Entry(winsignup, width=40 , textvariable = add)
	add.place(x=200 , y=293)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=200 , y=323)

	
	password = Entry(winsignup, width=40, textvariable = password)
	password.place(x=200 , y=353)

	
	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=200 , y=383)


	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=413)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=413)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	


	

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Docter Appointment App")

# window size
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)


#heading label
heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)



win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


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
				deshboard()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import send_feedback

# creating tkinter obj (window)
feedback_window = Tk()
feedback_window.title("mini-PS: Sign Up")
feedback_window.maxsize(width=500 ,  height=400)
feedback_window.minsize(width=500 ,  height=400)

def clear():
    """ Clear all text entry """
    messagebox.showinfo(title='delete', message='Do you want to clear?')
    username_text.delete(0, END)
    contact_mail_text.delete(0, END)
    feedback_text.delete(1.0, END)

def close():
    exit()


def get_feedback():
    """ Reading user inputs then send it to project mail. """
    username = username_text.get()
    contact_mail = contact_mail_text.get()
    feedback = feedback_text.get("1.0",END)
    try:
        send_feedback(username, contact_mail, feedback)
    except EXCEPTION as error_msg:
        messagebox.showinfo(title='[+] Error', message=str(error_msg))
    finally:
        messagebox.showinfo(title='[+] Done!', message="Your Feedback was sent successfully :).")
    exit()


# vars
user_gmail = StringVar()
user_password = StringVar()



header_lbl = ttk.Label(feedback_window, text='mini-PS Feedback', foreground='black', font=('Arial', 24))
header_lbl.place(x=120 , y=10)

username_lbl = Label(feedback_window, text = "Your Name: " , font = 'Verdana 10 bold')      # email lbl
username_lbl.place(x=60,y=80)
username_text = Entry(feedback_window, width = 40)               # email text
username_text.place(x=200 , y=80)

contact_mail_lbl = Label(feedback_window, text = "Contact Email: " , font = 'Verdana 10 bold')    # password lnl
contact_mail_lbl.place(x=60,y=120)
contact_mail_text = Entry(feedback_window, width = 40 , show="*", textvariable = user_password)  # password text
contact_mail_text.place(x=200 , y=120)

feedback_lbl = Label(feedback_window, text = "Feedback :" , font = 'Verdana 10 bold')   # feedback lbl
feedback_lbl.place(x=60,y=160)
feedback_text = Text(feedback_window, width=30, height=10)                                   # feedback text
feedback_text.place(x=200 , y=163)


# handling buttons
send_btn = Button(feedback_window, text = "Send", font = 'Verdana 10 bold', command = get_feedback)             
send_btn.place(x=200, y=340)
clear_btn = Button(feedback_window, text = "Clear", font = 'Verdana 10 bold', command = clear)
clear_btn.place(x=280, y=340)
close_btn = Button(feedback_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=360, y=340)


if __name__ == '__main__':
    mainloop()  # calling our program
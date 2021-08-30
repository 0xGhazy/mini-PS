
# Coded by: Hossam Hamdy
# Tested by: Hossam Hamdy
# Coding style: PEP-008

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import send_feedback, logger


def clear():
    """ Clear all text entry """
    messagebox.showinfo(title='delete', message='Do you want to clear?')
    username_text.delete(0, END)
    contact_mail_text.delete(0, END)
    feedback_text.delete(1.0, END)


def close():
    """Closing the frame"""
    logger("Info", "fb_edit.py has been closed.")
    exit()


def get_feedback():
    """ Reading user inputs then send it to project mail. """
    username = username_text.get()
    contact_mail = contact_mail_text.get()
    feedback = feedback_text.get("1.0",END)
    if username == "" or contact_mail == "" or feedback == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = feedback_window)
    else:
        try:
            # try to send feedback to the project email.
            send_feedback(username, contact_mail, feedback)
            logger("Info", f"feedback.py > send_feedback was ended now.")
        except EXCEPTION as error:
            messagebox.showinfo(title='[+] Error', message=str(error))
            logger("Warning", f"feedback.py > An error was occurred\n\n{error}\n\n")
        finally:
            messagebox.showinfo(title='[+] Done!', message="Your Feedback was sent successfully :).")
            logger("Info", f"feedback.py > Feedback was sent successfully :)")
        exit()



# creating tkinter obj (window)
feedback_window = Tk()
feedback_window.title("mini-PS: Feedback")
feedback_window.maxsize(width=500 ,  height=400)
feedback_window.minsize(width=500 ,  height=400)
header_lbl = ttk.Label(feedback_window, text='mini-PS Feedback', foreground='black', font=('Arial', 24))
header_lbl.place(x=120 , y=10)


username_lbl = Label(feedback_window, text = "Your Name: " , font = 'Arial 10 bold')
username_lbl.place(x=60,y=80)
username_text = Entry(feedback_window, width = 40)
username_text.place(x=200 , y=80)


contact_mail_lbl = Label(feedback_window, text = "Contact Email: " , font = 'Arial 10 bold')
contact_mail_lbl.place(x=60,y=120)
contact_mail_text = Entry(feedback_window, width = 40)
contact_mail_text.place(x=200 , y=120)


feedback_lbl = Label(feedback_window, text = "Feedback :" , font = 'Arial 10 bold')
feedback_lbl.place(x=60,y=160)
feedback_text = Text(feedback_window, width=30, height=10)
feedback_text.place(x=200 , y=163)

# handling send button
send_btn = Button(feedback_window, text = "Send", font = 'Arial 10 bold', command = get_feedback)             
send_btn.place(x=200, y=340)

# handling clear button
clear_btn = Button(feedback_window, text = "Clear", font = 'Arial 10 bold', command = clear)
clear_btn.place(x=280, y=340)

# handling Close button
close_btn = Button(feedback_window, text = "Close", font = 'Arial 10 bold', command = close)
close_btn.place(x=360, y=340)


# calling our program
mainloop() 

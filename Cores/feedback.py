from tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
root = Tk()
frame_header = ttk.Frame(root)
frame_header.pack()


headerlabel = ttk.Label(frame_header, text='FEEDBACK', foreground='black',
                        font=('Arial', 24))
headerlabel.grid(row=0, column=1)
messagelabel = ttk.Label(frame_header,
                         text='write your comment,plz',
                         foreground='purple', font=('Arial', 10))
messagelabel.grid(row=1, column=1)

frame_content = ttk.Frame(root)
frame_content.pack()
# def submit():
#     username = entry_name.get()
#     print(username)
myvar = StringVar()
var = StringVar()
# cmnt= StringVar()
namelabel = ttk.Label(frame_content, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(frame_content, text='Email')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(frame_content, text='Comment', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(frame_content, width=40, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='delete', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='send', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(frame_content, text='send', command=submit).grid(row=4, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='delete', command=clear).grid(row=4, column=1, sticky='w')

mainloop()
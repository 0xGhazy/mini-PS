import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json

os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")
conf = pathes["TIC_TAC_TOE_CONF"]
currant_sittings = read_json(conf)
p1s = currant_sittings["player1_symbol"]
p2s = currant_sittings["player2_symbol"]

def close():
    exit()

def update():
    if p1s_text.get() == "" or p2s_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = xo_edit_window)
    elif len(p1s_text.get()) > 1 or len(p2s_text.get()) > 1:
        messagebox.showerror("Error" , "Can't accept more than one char" , parent = xo_edit_window)
    else:
        new_sittings = {
        "player1_symbol": p1s_text.get(),
        "player2_symbol": p2s_text.get(),
        "player1_color": "lawn green",
        "player2_color": "deep sky blue"
        }
        try:
            create_json(conf, new_sittings)
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = xo_edit_window)
        finally:
            messagebox.showinfo("[Done]" , "Tic Tac Toe has updated successfully." , parent = xo_edit_window)
            close()

xo_edit_window = Tk()
xo_edit_window.title("mini-PS: Tic Tac Toe Sittings")
xo_edit_window.maxsize(width=500 ,  height=200)
xo_edit_window.minsize(width=500 ,  height=200)
heading = Label(xo_edit_window , text = "Tic Tac Toe Sittings" , font = 'Verdana 15 bold')
heading.place(x=135 , y=10)

p1s_lbl = Label(xo_edit_window, text = "Player1 Symbol: " , font = 'Verdana 10 bold')
p1s_lbl.place(x=80,y=90)
p1s_text = Entry(xo_edit_window,width = 40)
p1s_text.insert(0, p1s)
p1s_text.place(x=220 , y=90)

p2s_lbl = Label(xo_edit_window, text = "Player2 Symbol:  " , font = 'Verdana 10 bold')
p2s_lbl.place(x=80,y=120)
p2s_text = Entry(xo_edit_window,width = 40)
p2s_text.insert(0, p2s)
p2s_text.place(x=220 , y=120)

# handling buttons
btn_update = Button(xo_edit_window, text = "Update", font = 'Verdana 10 bold', command = update)
btn_update.place(x=200, y=150)
close_btn = Button(xo_edit_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=290, y=150)


mainloop()
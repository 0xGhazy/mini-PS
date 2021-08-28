import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json

os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")

conf = pathes["FLAPPY_BIRD_CONF"]
currant_sittings = read_json(conf)
game_gravity = currant_sittings["game_gravity"]

def close():
    exit()

def update():
    if game_gravity_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = fb_edit_window)
    else:
        new_sittings = {"game_gravity": float(game_gravity_text.get())}
        try:
            create_json(conf, new_sittings)
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = fb_edit_window)
        finally:
            messagebox.showinfo("[Done]" , "Flappy Birds has updated successfully." , parent = fb_edit_window)
            close()

fb_edit_window = Tk()
fb_edit_window.title("mini-PS: Flappy Birds Sittings")
fb_edit_window.maxsize(width=500 ,  height=200)
fb_edit_window.minsize(width=500 ,  height=200)
heading = Label(fb_edit_window , text = "Flappy Birds Edit Sittings" , font = 'Verdana 15 bold')
heading.place(x=105 , y=10)

game_gravity_lbl = Label(fb_edit_window, text = "Game Gravity: " , font = 'Verdana 10 bold')
game_gravity_lbl.place(x=80,y=90)
game_gravity_text = Entry(fb_edit_window,width = 40)
game_gravity_text.insert(0, game_gravity)
game_gravity_text.place(x=200 , y=90)

# handling buttons
btn_update = Button(fb_edit_window, text = "Update", font = 'Verdana 10 bold', command = update)
btn_update.place(x=200, y=150)

close_btn = Button(fb_edit_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=290, y=150)


mainloop()
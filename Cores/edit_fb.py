# Coded by: Sameh Elisha 
# Tested by: Hossam Hamdy
# Coding Style: PEP-008   

# importing modules
import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json, logger

# reading Profile.json to get required pathes
os.chdir(os.path.dirname(__file__))
pathes = read_json(r"Profile.json")
conf = pathes["FLAPPY_BIRD_CONF"]
currant_sittings = read_json(conf)
game_gravity = currant_sittings["game_gravity"]


def close():
    """Closing the frame"""
    logger("Info", "fb_edit.py has been closed.")
    exit()


def update():
    # check for inbut validation.
    if game_gravity_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = fb_edit_window)
        logger("Info", "fb_edit.py > All Fields Are Required message appears.")
    else:
        try:
            new_sittings = {"game_gravity": float(game_gravity_text.get())}
            create_json(conf, new_sittings)
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = fb_edit_window)
            logger("Warning", f"fb_edit.py > an error was occurred\n\n{error_message}\n\n")
        finally:
            messagebox.showinfo("[Done]" , "Flappy Birds has updated successfully." , parent = fb_edit_window)
            logger("Info", f"fb_configurations.json was updated successfully.")
            close()


# ------------------------------------- Tkinter code starts here ------------------------------------- #

# taking an tkinter object
fb_edit_window = Tk()
# setting window title
fb_edit_window.title("mini-PS: Flappy Birds Sittings")
# setting window geometry
fb_edit_window.maxsize(width=500 ,  height=200)
fb_edit_window.minsize(width=500 ,  height=200)
# adding inner title
heading = Label(fb_edit_window , text = "Flappy Birds Edit Sittings" , font = 'Arial 15 bold')
heading.place(x=105 , y=10)


game_gravity_lbl = Label(fb_edit_window, text = "Game Gravity: " , font = 'Arial 10 bold')
game_gravity_lbl.place(x=80,y=90)
game_gravity_text = Entry(fb_edit_window,width = 40)
game_gravity_text.insert(0, game_gravity)
game_gravity_text.place(x=200 , y=90)


# handling update button
btn_update = Button(fb_edit_window, text = "Update", font = 'Arial 10 bold', command = update)
btn_update.place(x=200, y=150)

# handling Close button
close_btn = Button(fb_edit_window, text = "Close", font = 'Arial 10 bold', command = close)
close_btn.place(x=290, y=150)

# calling our program.
mainloop()

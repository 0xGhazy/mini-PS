# Coded by: Asmma Elnaggar
# Tested by: Hossam Hamdy 
# Coding Style: PEP-008

import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json, logger

# reading Profile.json to get required pathes
os.chdir(os.path.dirname(__file__))
pathes = read_json(r"Profile.json")
SNAKE_CONF = pathes["SNAKE_CONF"]
# init initial sittings values
currant_sittings = read_json(SNAKE_CONF)
cbg_color = currant_sittings["bg_color"]
ctarget_color = currant_sittings["target_color"]
cgame_over_message_color = currant_sittings["game_over_message_color"]
csnake_color = currant_sittings["snake_color"]
cscreen_width = currant_sittings["screen_width"]
cscreen_height = currant_sittings["screen_height"]
csnake_size = currant_sittings["snake_size"]
csnake_speed = currant_sittings["sanke_speed"]


def close():
    """Closing the frame"""
    logger("Info", "sn_edit.py has been closed.")
    exit()


def update():
    """Reading inputs from text fields and update snake configurations file."""
    # check if Text = Null
    if cbg_color_text.get() == "" or ctarget_color_text.get() == "" or cgame_over_message_color_text.get() == "" or csnake_color_text.get() == "" or \
        cscreen_width_text.get() == "" or cscreen_height_text.get() == "" or csnake_size_text.get() == "" or csnake_speed_text.get() == "":
        messagebox.showerror("[-] Error" , "All Fields Are Required" , parent = sn_edit_window)
        logger("Info", "edit_sn.py > All Fields Are Required message appears.")
    else:
        try:
            # check for inbut validation.
            cbg_color = cbg_color_text.get().split(" ")
            # reassign backeground color and doing the samt to the following
            cbg_color = [int(cbg_color[0]), int(cbg_color[1]), int(cbg_color[2])]
            ctc = ctarget_color_text.get().split(" ")
            ctc = [int(ctc[0]), int(ctc[1]), int(ctc[2])]
            cgomc = cgame_over_message_color_text.get().split(" ")
            cgomc = [int(cgomc[0]), int(cgomc[1]), int(cgomc[2])]
            csc = csnake_color_text.get().split(" ")
            csc = [int(csc[0]), int(csc[1]), int(csc[2])]

            new_sittings = {
            "bg_color": cbg_color,
            "target_color": ctc,
            "game_over_message_color": cgomc,
            "snake_color": csc,
            "screen_width": int(cscreen_width_text.get()),
            "screen_height": int(cscreen_height_text.get()),
            "snake_size": int(csnake_size_text.get()),
            "sanke_speed": int(csnake_speed_text.get())
            }
            create_json(SNAKE_CONF, new_sittings)
            logger("Info", "edit_sn.py > All inputs are valid.")
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = sn_edit_window)
            logger("Warning", f"edit_sn.py > an error was occurred\n\n{error_message}\n\n")
        finally:
            messagebox.showinfo("[Done]" , "Snake Game has updated successfully." , parent = sn_edit_window)
            logger("Info", f"edit_sn.py > sn_configurations.json was updated successfully.")
            close()



# ------------------------------------- Tkinter code starts here ------------------------------------- #


# taking an tkinter object
sn_edit_window = Tk()
# setting window title
sn_edit_window.title("mini-PS: Snake Sittings")
# setting window geometry and max size.
sn_edit_window.maxsize(width=500 ,  height=400)
sn_edit_window.minsize(width=500 ,  height=400)
# adding inner title
heading = Label(sn_edit_window , text = "Snake Sittings" , font = 'Arial 15 bold')
heading.place(x=165 , y=10)

# setting background color label.
cbg_color_lbl = Label(sn_edit_window, text = "BG Color: " , font = 'Arial 10 bold')
cbg_color_lbl.place(x=80,y=90)
# creating text entry field.
cbg_color_text = Entry(sn_edit_window,width = 40)
# displaying the init value.
cbg_color_text.insert(0, cbg_color)
cbg_color_text.place(x=200 , y=90)

# do the same for all following.

ctarget_color_lbl = Label(sn_edit_window, text = "Target Color: " , font = 'Arial 10 bold')
ctarget_color_lbl.place(x=80,y=120)
ctarget_color_text = Entry(sn_edit_window,width = 40)
ctarget_color_text.insert(0, ctarget_color)
ctarget_color_text.place(x=200 , y=120)

cgame_over_message_color_lbl = Label(sn_edit_window, text = "GaOv Color: " , font = 'Arial 10 bold')
cgame_over_message_color_lbl.place(x=80,y=150)
cgame_over_message_color_text = Entry(sn_edit_window,width = 40)
cgame_over_message_color_text.insert(0, cgame_over_message_color)
cgame_over_message_color_text.place(x=200 , y=150)

csnake_color_lbl = Label(sn_edit_window, text = "Snake Color: " , font = 'Arial 10 bold')
csnake_color_lbl.place(x=80,y=180)
csnake_color_text = Entry(sn_edit_window,width = 40)
csnake_color_text.insert(0, csnake_color)
csnake_color_text.place(x=200 , y=180)

cscreen_width_lbl = Label(sn_edit_window, text = "Screen Width: " , font = 'Arial 10 bold')
cscreen_width_lbl.place(x=80,y=210)
cscreen_width_text = Entry(sn_edit_window,width = 40)
cscreen_width_text.insert(0, cscreen_width)
cscreen_width_text.place(x=200 , y=210)

cscreen_height_lbl = Label(sn_edit_window, text = "Screen Height: " , font = 'Arial 10 bold')
cscreen_height_lbl.place(x=80,y=240)
cscreen_height_text = Entry(sn_edit_window,width = 40)
cscreen_height_text.insert(0, cscreen_height)
cscreen_height_text.place(x=200 , y=240)

csnake_size_lbl = Label(sn_edit_window, text = "Snake Size: " , font = 'Arial 10 bold')
csnake_size_lbl.place(x=80,y=270)
csnake_size_text = Entry(sn_edit_window,width = 40)
csnake_size_text.insert(0, csnake_size)
csnake_size_text.place(x=200 , y=270)

csnake_speed_lbl = Label(sn_edit_window, text = "Snake Speed: " , font = 'Arial 10 bold')
csnake_speed_lbl.place(x=80,y=300)
csnake_speed_text = Entry(sn_edit_window,width = 40)
csnake_speed_text.insert(0, csnake_speed)
csnake_speed_text.place(x=200 , y=300)

# handling update button
btn_update = Button(sn_edit_window, text = "Update", font = 'Arial 10 bold', command = update)
btn_update.place(x=200, y=330)

# handling Close button
close_btn = Button(sn_edit_window, text = "Close", font = 'Arial 10 bold', command = close)
close_btn.place(x=290, y=330)

# calling our application.
mainloop()

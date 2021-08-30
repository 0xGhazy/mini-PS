# Coded by: Hossam hamdy  
# Tested by: Hossam Hamdy 
# Coding Style: PEP-008   


# importing modules
import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json, logger

# changing to cwd
os.chdir(os.path.dirname(__file__))
# reading Profile.json to get required pathes
pathes = read_json(r"Profile.json")
ALIEN_INVASION_CONF = pathes["ALIEN_INVASION_CONF"]     


# init currant sittings from json file to text fields.
currant_sittings = read_json(ALIEN_INVASION_CONF)
scrrenWidth = currant_sittings["screen_width"]
screenHeight = currant_sittings["screen_height"]
bgColor = currant_sittings["bg_color"]
shipLimit = currant_sittings["ship_limit"]
bulletWidth = currant_sittings["bullet_width"]
bulletHeight = currant_sittings["bullet_height"]
bulletColor = currant_sittings["bullet_color"]
fleetDropSpeed = currant_sittings["fleet_drop_speed"]
logger("Info", "ai_edit.py has loaded currant sittings.")

def close():
    """Closing the frame"""
    logger("Info", "ai_edit.py has been closed.")
    exit()


def update():
    """Reading inputs from text fields and update Alien invasion configurations file."""
    # check if Text = Null
    if screen_width_text.get() == "" or screen_height_text.get() == "" or bg_color_text.get() == "" or shipLimit_text.get() == "" or \
        bulletWidth_text.get() == "" or bulletHeight_text.get() == "" or bulletColor_text.get() == "" or fleetDropSpeed_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = ai_edit_window)
        logger("Info", "ai_edit.py > All Fields Are Required message appears.")
    else:
        try:
            # check for inbut validation.
            # backeground color ex0 ex0 ex0
            bgc = bg_color_text.get().split(" ")
            # reassign backeground color
            bgc = [int(bgc[0]), int(bgc[1]), int(bgc[2])]

            # Bullets color ex0 ex0 ex0
            bc = bulletColor_text.get().split(" ")
            # reassign Bullets color
            bc = [int(bc[0]), int(bc[1]), int(bc[2])]

            new_sittings = {
                "screen_width": int(screen_width_text.get()),
                "screen_height": int(screen_height_text.get()),
                "bg_color": bgc,
                "ship_limit": int(shipLimit_text.get()),
                "bullet_width": int(bulletWidth_text.get()),
                "bullet_height": int(bulletHeight_text.get()),
                "bullet_color": bc,
                "fleet_drop_speed": int(fleetDropSpeed_text.get())
            }
            logger("Info", "ai_edit.py > All inputs are valid.")
        except Exception as error_message:
            # excepting for value errors
            messagebox.showerror("[-] Error" , str(error_message) , parent = ai_edit_window)
            logger("Warning", f"ai_edit.py > an error was occurred\n\n{error_message}\n\n")
        try:
            # update ai_configurations.json file
            create_json(ALIEN_INVASION_CONF, new_sittings)
        except Exception as error_message:
            # excepting for notfound errors
            messagebox.showerror("[-] Error" , str(error_message) , parent = ai_edit_window)
            logger("Warning", f"ai_edit.py > an error was occurred\n\n{error_message}\n\n")
        finally:
            # informing the user
            messagebox.showinfo("[+] Done" , "Alien Invasion has updated successfully." , parent = ai_edit_window)
            logger("Info", f"ai_edit.py > ai_configurations.json was updated successfully.")
            close()


# ------------------------------------- Tkinter code starts here ------------------------------------- #


# taking an tkinter object
ai_edit_window = Tk()
# setting window title
ai_edit_window.title("mini-PS: Alien Invasion Sittings")
# setting window geometry
ai_edit_window.maxsize(width=500 ,  height=400)
ai_edit_window.minsize(width=500 ,  height=400)
# adding inner title
heading = Label(ai_edit_window , text = "Alien Invasion Edit Sittings" , font = 'Arial 15 bold')
heading.place(x=120 , y=10)


# setting screen width label
screen_width_lbl = Label(ai_edit_window, text = "Screen Width: " , font = 'Arial 10 bold')
screen_width_lbl.place(x=80,y=90)
# setting screen width Text entry
screen_width_text = Entry(ai_edit_window,width = 40)
# init value to screen width text entry.
screen_width_text.insert(0, scrrenWidth)
screen_width_text.place(x=200 , y=90)

# doing the same to the comming sections

screen_height_lbl = Label(ai_edit_window, text = "Screen height: " , font = 'Arial 10 bold')
screen_height_lbl.place(x=80,y=120)
screen_height_text = Entry(ai_edit_window,width = 40)
screen_height_text.insert(0, screenHeight)
screen_height_text.place(x=200 , y=120)


bg_color_lbl = Label(ai_edit_window, text = "bg Color: " , font = 'Arial 10 bold')
bg_color_lbl.place(x=80,y=150)
bg_color_text = Entry(ai_edit_window,width = 40)
bg_color_text.insert(0, bgColor)
bg_color_text.place(x=200 , y=150)


shipLimit_lbl = Label(ai_edit_window, text = "Ship Limit: " , font = 'Arial 10 bold')
shipLimit_lbl.place(x=80,y=180)
shipLimit_text = Entry(ai_edit_window,width = 40)
shipLimit_text.insert(0, shipLimit)
shipLimit_text.place(x=200 , y=180)


bulletWidth_lbl = Label(ai_edit_window, text = "Bullet Width: ", font = 'Arial 10 bold')
bulletWidth_lbl.place(x=80,y=210)
bulletWidth_text = Entry(ai_edit_window,width = 40)
bulletWidth_text.insert(0, bulletWidth)
bulletWidth_text.place(x=200 , y=210)


bulletHeight_lbl = Label(ai_edit_window, text = "Bullet Height: " , font = 'Arial 10 bold')
bulletHeight_lbl.place(x=80,y=240)
bulletHeight_text = Entry(ai_edit_window,width = 40)
bulletHeight_text.insert(0, bulletHeight)
bulletHeight_text.place(x=200 , y=240)


bulletColor_lbl = Label(ai_edit_window, text = "Bullet Color: " , font = 'Arial 10 bold')
bulletColor_lbl.place(x=80,y=270)
bulletColor_text = Entry(ai_edit_window,width = 40)
bulletColor_text.insert(0, bulletColor)
bulletColor_text.place(x=200 , y=270)


fleetDropSpeed_lbl = Label(ai_edit_window, text = "Fleet Speed: " , font = 'Arial 10 bold')
fleetDropSpeed_lbl.place(x=80,y=300)
fleetDropSpeed_text = Entry(ai_edit_window,width = 40)
fleetDropSpeed_text.insert(0, fleetDropSpeed)
fleetDropSpeed_text.place(x=200 , y=300)


# handling update button
btn_update = Button(ai_edit_window, text = "Update", font = 'Arial 10 bold', command = update)
btn_update.place(x=200, y=330)


# handling Close button
close_btn = Button(ai_edit_window, text = "Close", font = 'Arial 10 bold', command = close)
close_btn.place(x=290, y=330)


# Calling our program
mainloop()

import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json

os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")
ALIEN_INVASION_CONF = pathes["ALIEN_INVASION_CONF"]

# reading currant sittings from json file
currant_sittings = read_json(ALIEN_INVASION_CONF)
scrrenWidth = currant_sittings["screen_width"]
screenHeight = currant_sittings["screen_height"]
bgColor = currant_sittings["bg_color"]
shipLimit = currant_sittings["ship_limit"]
bulletWidth = currant_sittings["bullet_width"]
bulletHeight = currant_sittings["bullet_height"]
bulletColor = currant_sittings["bullet_color"]
fleetDropSpeed = currant_sittings["fleet_drop_speed"]

def close():
    exit()

def update():
    if screen_width_text.get() == "" or screen_height_text.get() == "" or bg_color_text.get() == "" or shipLimit_text.get() == "" or \
        bulletWidth_text.get() == "" or bulletHeight_text.get() == "" or bulletColor_text.get() == "" or fleetDropSpeed_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = ai_edit_window)
    bgc = bg_color_text.get().split(" ")
    bgc = [int(bgc[0]), int(bgc[1]), int(bgc[2])]
    bc = bulletColor_text.get().split(" ")
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
    if screen_width_text.get() == "" or screen_height_text.get() == "" or bg_color_text.get() == "" or shipLimit_text.get() == "" or \
        bulletWidth_text.get() == "" or bulletHeight_text.get() == "" or bulletColor_text.get() == "" or fleetDropSpeed_text.get() == "":
        messagebox.showerror("Error" , "All Fields Are Required" , parent = ai_edit_window)
    else:
        try:
            create_json(ALIEN_INVASION_CONF, new_sittings)
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = ai_edit_window)
        finally:
            messagebox.showinfo("[Done]" , "Alien Invasion has updated successfully." , parent = ai_edit_window)
            close()

ai_edit_window = Tk()
ai_edit_window.title("mini-PS: Alien Invasion sittings")
ai_edit_window.maxsize(width=500 ,  height=40)
ai_edit_window.minsize(width=500 ,  height=400)
heading = Label(ai_edit_window , text = "Alien Invasion Edit Sittings" , font = 'Verdana 15 bold')
heading.place(x=90 , y=10)

screen_width_lbl = Label(ai_edit_window, text = "Screen Width: " , font = 'Verdana 10 bold')
screen_width_lbl.place(x=80,y=90)
screen_width_text = Entry(ai_edit_window,width = 40)
screen_width_text.insert(0, scrrenWidth)
screen_width_text.place(x=200 , y=90)

screen_height_lbl = Label(ai_edit_window, text = "Screen height: " , font = 'Verdana 10 bold')
screen_height_lbl.place(x=80,y=120)
screen_height_text = Entry(ai_edit_window,width = 40)
screen_height_text.insert(0, screenHeight)
screen_height_text.place(x=200 , y=120)

bg_color_lbl = Label(ai_edit_window, text = "bg Color: " , font = 'Verdana 10 bold')
bg_color_lbl.place(x=80,y=150)
bg_color_text = Entry(ai_edit_window,width = 40)
bg_color_text.insert(0, bgColor)
bg_color_text.place(x=200 , y=150)

shipLimit_lbl = Label(ai_edit_window, text = "Ship Limit: " , font = 'Verdana 10 bold')
shipLimit_lbl.place(x=80,y=180)
shipLimit_text = Entry(ai_edit_window,width = 40)
shipLimit_text.insert(0, shipLimit)
shipLimit_text.place(x=200 , y=180)

bulletWidth_lbl = Label(ai_edit_window, text = "Bullet Width: " , font = 'Verdana 10 bold')
bulletWidth_lbl.place(x=80,y=210)
bulletWidth_text = Entry(ai_edit_window,width = 40)
bulletWidth_text.insert(0, bulletWidth)
bulletWidth_text.place(x=200 , y=210)

bulletHeight_lbl = Label(ai_edit_window, text = "Bullet Height: " , font = 'Verdana 10 bold')
bulletHeight_lbl.place(x=80,y=240)
bulletHeight_text = Entry(ai_edit_window,width = 40)
bulletHeight_text.insert(0, bulletHeight)
bulletHeight_text.place(x=200 , y=240)

bulletColor_lbl = Label(ai_edit_window, text = "Bullet Color: " , font = 'Verdana 10 bold')
bulletColor_lbl.place(x=80,y=270)
bulletColor_text = Entry(ai_edit_window,width = 40)
bulletColor_text.insert(0, bulletColor)
bulletColor_text.place(x=200 , y=270)

fleetDropSpeed_lbl = Label(ai_edit_window, text = "Fleet Speed: " , font = 'Verdana 10 bold')
fleetDropSpeed_lbl.place(x=80,y=300)
fleetDropSpeed_text = Entry(ai_edit_window,width = 40)
fleetDropSpeed_text.insert(0, fleetDropSpeed)
fleetDropSpeed_text.place(x=200 , y=300)

# handling buttons
btn_update = Button(ai_edit_window, text = "Update", font = 'Verdana 10 bold', command = update)
btn_update.place(x=200, y=330)

close_btn = Button(ai_edit_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=290, y=330)

if __name__ == '__main__':
    mainloop()
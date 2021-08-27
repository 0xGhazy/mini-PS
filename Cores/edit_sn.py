import os
from tkinter import*
from tkinter import messagebox
from functions import create_json, read_json

os.chdir(os.path.dirname(__file__))
pathes = read_json(r"profile.json")
SNAKE_CONF = pathes["SNAKE_CONF"]
# reading currant sittings from json file
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
    exit()


def update():
    if cbg_color_text.get() == "" or ctarget_color_text.get() == "" or cgame_over_message_color_text.get() == "" or csnake_color_text.get() == "" or \
        cscreen_width_text.get() == "" or cscreen_height_text.get() == "" or csnake_size_text.get() == "" or csnake_speed_text.get() == "":
        messagebox.showerror("[-] Error" , "All Fields Are Required" , parent = sn_edit_window)

    else:
        cbg_color = cbg_color_text.get().split(" ")
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
        try:
            create_json(SNAKE_CONF, new_sittings)
        except Exception as error_message:
            messagebox.showerror("Error" , str(error_message) , parent = sn_edit_window)
        finally:
            messagebox.showinfo("[Done]" , "Snake Game has updated successfully." , parent = sn_edit_window)
            close()

sn_edit_window = Tk()
sn_edit_window.title("mini-PS: Sign in")
sn_edit_window.maxsize(width=500 ,  height=40)
sn_edit_window.minsize(width=500 ,  height=400)
heading = Label(sn_edit_window , text = "Alien Invasion Edit Sittings" , font = 'Verdana 15 bold')
heading.place(x=90 , y=10)

cbg_color_lbl = Label(sn_edit_window, text = "BG Color: " , font = 'Verdana 10 bold')
cbg_color_lbl.place(x=80,y=90)
cbg_color_text = Entry(sn_edit_window,width = 40)
cbg_color_text.insert(0, cbg_color)
cbg_color_text.place(x=200 , y=90)

ctarget_color_lbl = Label(sn_edit_window, text = "Target Color: " , font = 'Verdana 10 bold')
ctarget_color_lbl.place(x=80,y=120)
ctarget_color_text = Entry(sn_edit_window,width = 40)
ctarget_color_text.insert(0, ctarget_color)
ctarget_color_text.place(x=200 , y=120)

cgame_over_message_color_lbl = Label(sn_edit_window, text = "GaOv Color: " , font = 'Verdana 10 bold')
cgame_over_message_color_lbl.place(x=80,y=150)
cgame_over_message_color_text = Entry(sn_edit_window,width = 40)
cgame_over_message_color_text.insert(0, cgame_over_message_color)
cgame_over_message_color_text.place(x=200 , y=150)

csnake_color_lbl = Label(sn_edit_window, text = "Snake Color: " , font = 'Verdana 10 bold')
csnake_color_lbl.place(x=80,y=180)
csnake_color_text = Entry(sn_edit_window,width = 40)
csnake_color_text.insert(0, csnake_color)
csnake_color_text.place(x=200 , y=180)

cscreen_width_lbl = Label(sn_edit_window, text = "Screen Width: " , font = 'Verdana 10 bold')
cscreen_width_lbl.place(x=80,y=210)
cscreen_width_text = Entry(sn_edit_window,width = 40)
cscreen_width_text.insert(0, cscreen_width)
cscreen_width_text.place(x=200 , y=210)

cscreen_height_lbl = Label(sn_edit_window, text = "Screen Height: " , font = 'Verdana 10 bold')
cscreen_height_lbl.place(x=80,y=240)
cscreen_height_text = Entry(sn_edit_window,width = 40)
cscreen_height_text.insert(0, cscreen_height)
cscreen_height_text.place(x=200 , y=240)

csnake_size_lbl = Label(sn_edit_window, text = "Snake Size: " , font = 'Verdana 10 bold')
csnake_size_lbl.place(x=80,y=270)
csnake_size_text = Entry(sn_edit_window,width = 40)
csnake_size_text.insert(0, csnake_size)
csnake_size_text.place(x=200 , y=270)

csnake_speed_lbl = Label(sn_edit_window, text = "Snake Speed: " , font = 'Verdana 10 bold')
csnake_speed_lbl.place(x=80,y=300)
csnake_speed_text = Entry(sn_edit_window,width = 40)
csnake_speed_text.insert(0, csnake_speed)
csnake_speed_text.place(x=200 , y=300)

# handling buttons
btn_update = Button(sn_edit_window, text = "Update", font = 'Verdana 10 bold', command = update)
btn_update.place(x=200, y=330)

close_btn = Button(sn_edit_window, text = "Close", font = 'Verdana 10 bold', command = close)
close_btn.place(x=290, y=330)


mainloop()
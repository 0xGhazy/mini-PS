#
# Refactored by: Engy Essam
# The Main-idea: https://www.codespeedy.com/tic-tac-toe-gui-in-python-using-tkinter/
#


import json
from tkinter import *
from tkinter import messagebox
import random as r
import os
import json

os.chdir(os.path.dirname(__file__))
content = ""
with open("xo_configuration.json", 'r') as f:
    content = json.load(f)

# {'player1_symbol': 'O', 'player2_symbol': 'X', 'player1_color': [255, 0, 0], 'player2_color': [0, 255, 0]}

# game sittings
player1_symbol = content['player1_symbol']
player2_symbol = content['player2_symbol']
player1_color = content['player1_color']
player2_color = content['player2_color']

def button(frame):
    """ Function to define button to be choosed.
    Args:
        frame ([TkInter-Object]): [The main game window]
    Returns:
        btn ([TkInter-Object]): [player choice button]
    """

    btn = Button(frame, padx = 1, bg = "papaya whip", width = 3,
    	         text = "   ", font = ('arial', 60, 'bold'), relief = "sunken", bd = 10)
    return btn


def change_chance():
    """ Function to change play round chance between 'X' and 'O' """

    global PlayerSymbol
    for i in [player1_symbol, player2_symbol]:
        if not ( i == PlayerSymbol):
            PlayerSymbol = i
            break


def reset():
    """ Function to reset gameplay bord. """

    global PlayerSymbol
    for i in range(3):
        for j in range(3):
                bord[i][j]["text"] = " "
                bord[i][j]["state"] = NORMAL
    # Choose random player to strart the game.
    PlayerSymbol = r.choice([player1_symbol, player2_symbol])


def check():
    """ Function for checking game status Win/Draw. """

    for i in range(3):
        # Checking for winers
            if(bord[i][0]["text"] == bord[i][1]["text"] == bord[i][2]["text"] == PlayerSymbol \
            or bord[0][i]["text"] == bord[1][i]["text"] == bord[2][i]["text"] == PlayerSymbol):
                                        # msg geader, message content
                    messagebox.showinfo("Congrats!", f"{PlayerSymbol}' Player Has Won the game <3")
                    reset() # calling reset function
    
    if(bord[0][0]["text"] == bord[1][1]["text"] == bord[2][2]["text"] == PlayerSymbol \
    or bord[0][2]["text"] == bord[1][1]["text"] == bord[2][0]["text"] == PlayerSymbol):
        messagebox.showinfo("Congrats!", f"{PlayerSymbol}' Player Has Won the game <3")
        reset()
    
    elif(bord[0][0]["state"] == bord[0][1]["state"] == bord[0][2]["state"] == bord[1][0]["state"] \
    == bord[1][1]["state"] == bord[1][2]["state"] == bord[2][0]["state"] == bord[2][1]["state"] == bord[2][2]["state"] == DISABLED):
        messagebox.showinfo("Oops!!","The match ended in a draw")
        reset()


def click(row,col):
    """ Function to draw the player symbole on the clicked button.
    Args:
        row ([TkInter-Object-Propirity]): [description]
        col ([TkInter-Object-Propirity]): [description]
    """

    # draw player symbol in its color
    bord[row][col].config(text = PlayerSymbol, state = DISABLED, disabledforeground = colour[PlayerSymbol])
    check()                                             # calling check function to check game status.
    change_chance()                                     # change to the another player.
    label.config(text = PlayerSymbol + "'s Chance")     # change to player chance.

"""
The Main program
"""


# Create Window.
root = Tk()
# Set windows Title.
root.title("mini-PS: Tic-Tac-Toe")

# Define Two players.
PlayerSymbol = r.choice([player1_symbol, player2_symbol])

# define players symbols color.
colour = {player1_symbol: player1_color, player2_symbol : player2_color}

bord = [[], [], []]                                       # gameplay bord.
# draw game play bord
for i in range(3):
	for j in range(3):
	    bord[i].append(button(root))
	    bord[i][j].config(command = lambda row = i, col = j : click(row,col))
	    bord[i][j].grid(row = i, column = j)
label = Label(text = PlayerSymbol + "'s Chance", font = ('arial',20,'bold'))    # Inform players.
label.grid(row = 3, column = 0, columnspan = 3)                                 # put the lbl on the frame.


def _RunXoGame_():
    """ This function used to call thw game in the main application. """
    root.mainloop()


_RunXoGame_()
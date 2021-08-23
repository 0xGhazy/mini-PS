
import os
import sys
import subprocess
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic

# change wd to cwd to run from cmd/vscode/python interpreter.
os.chdir(os.path.dirname(__file__))

# import games.
AI_Game_handle = r"Games\Alien_Invasion\alien_invasion.py"  # Handling Alien Invasion game.
FB_Game_handle = r"Games\Flappy_Bird\fb_game.py"            # Handling Flappy bird game.
XO_Game_handle = r"Games\TicTacToe\XO.py"                   # importing XO game.
SN_Game_handle = r"Games\Snake\SnakeGames.py"               # importing Snake game.

# project documentation handler
doc_handler = r"Documentation\Docs.html"

class ApplicationUI(QtWidgets.QMainWindow):
    """  """

    def __init__(self):
        super(ApplicationUI, self).__init__()
        uic.loadUi('UI\mini_PS_UI.ui', self)
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.tabBar().setVisible(False)
        self.show()
        self.HandelButtons()
        

    def HandelButtons(self):
        # Handling All buttons in the application.
        self.home_btn.clicked.connect(self.ch_to_home)
        self.ai_btn.clicked.connect(self.ch_to_ai)
        self.fb_btn.clicked.connect(self.ch_to_fb)
        self.sn_btn.clicked.connect(self.ch_to_sn)
        self.xo_btn.clicked.connect(self.ch_to_xo)

        # handling start buttons
        self.play_ai.clicked.connect(self.start_ai)
        self.play_fb.clicked.connect(self.start_fb)
        self.play_sn.clicked.connect(self.start_sn)
        self.play_xo.clicked.connect(self.start_xo)

        # doc button
        self.doc_btn.clicked.connect(self.open_doc)


    # ------------------------- #
    # Handling navigaionbuttons #
    # ------------------------- #

    # handling home_btn actions
    def ch_to_home(self):
        """ Changing tab page to home page """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(0)

    # handling ai_btn acction
    def ch_to_ai(self):
        """  Changing tab page to Alien invasion game."""
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(1)

    # handling fb_btn action
    def ch_to_fb(self):
        """ Changing tab page to flappy bird page. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(2)

    # handling sn_btn action
    def ch_to_sn(self):
        """ Changing tab page to snake game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(3)
    
    # handling xo_btn
    def ch_to_xo(self):
        """ Changing tab page to xo game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(4)

    # --------------------------- #
    # Handling game start buttons #
    # --------------------------- #

    def start_ai(self):
        CMD = subprocess.Popen(AI_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()

    def start_fb(self):
        CMD = subprocess.Popen(FB_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()

    def start_sn(self):
        CMD = subprocess.Popen(SN_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()

    def start_xo(self):
        CMD = subprocess.Popen(XO_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()

    def open_doc(self):
        CMD = subprocess.Popen(doc_handler, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationUI()
    app.exec_()

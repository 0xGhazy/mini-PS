import os
import sys
import subprocess
os.chdir(os.path.dirname(__file__))
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from Cores.functions import run, read_json

# Reading pathes from profile.json file.
pathes = read_json(r"Cores\profile.json")
ALIEN_INVASION_PATH = pathes["ALIEN_INVASION_PATH"]
ALIEN_INVASION_EDIT = pathes["ALIEN_INVASION_EDIT"]
FLAPPY_BIRD_PATH = pathes["FLAPPY_BIRD_PATH"]
FLAPPY_BIRD_EDIT = pathes["FLAPPY_BIRD_EDIT"]
SNAKE_PATH = pathes["SNAKE_PATH"]
SNAKE_EDIT = pathes["SNAKE_EDIT"]
TIC_TAC_TOE_PATH = pathes["TIC_TAC_TOE_PATH"]
TIC_TAC_TOE_EDIT = pathes["TIC_TAC_TOE_EDIT"]
DOCUMENTATION_PATH = pathes["DOCUMENTATION_PATH"]
VISIT_REPOSITORY = 'explorer "https://github.com/0xGhazy/mini-PS"'
FEEDBACK = pathes["FEEDBACK"]

signin_path = r"Cores\signin_frame.py"
XO_Game_handle = r"Cores\edit_xo.py"
SN_Game_handle = r"Cores\edit_sn.py"


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
        """[summary]"""
        # (Navigation) events
        self.home_btn.clicked.connect(self.ch_to_home)
        self.ai_btn.clicked.connect(self.ch_to_ai)
        self.fb_btn.clicked.connect(self.ch_to_fb)
        self.sn_btn.clicked.connect(self.ch_to_sn)
        self.xo_btn.clicked.connect(self.ch_to_xo)

        self.play_ai.clicked.connect(self.start_ai)
        self.play_fb.clicked.connect(self.start_fb)
        self.play_sn.clicked.connect(self.start_sn)
        self.play_xo.clicked.connect(self.start_xo)

        self.sn_sittings.clicked.connect(self.sn_sittings_fn)
        self.xo_sittings.clicked.connect(self.xo_sittings_fn)
        self.ai_sittings.clicked.connect(self.ai_sittings_fn)
        self.fb_sittings.clicked.connect(self.fb_sittings_fn)

        self.doc_btn.clicked.connect(self.open_doc)
        self.github_btn.clicked.connect(self.visit_github)
        self.feedback_btn.clicked.connect(self.get_feedback)
        


    # Handling navigaionbuttons #
    def ch_to_home(self):
        """ Changing tab page to home page """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(0)
    def ch_to_ai(self):
        """  Changing tab page to Alien invasion game."""
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(1)
    def ch_to_fb(self):
        """ Changing tab page to flappy bird page. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(2)
    def ch_to_sn(self):
        """ Changing tab page to snake game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(3)
    def ch_to_xo(self):
        """ Changing tab page to xo game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(4)


    # Handling game start buttons #
    def start_ai(self):
        run(ALIEN_INVASION_PATH)
    def start_fb(self):
        run(FLAPPY_BIRD_PATH)
    def start_sn(self):
        run(SNAKE_PATH)
    def start_xo(self):
        run(TIC_TAC_TOE_PATH)


    # Handling Sittings buttons #
    def ai_sittings_fn(self):
        run(ALIEN_INVASION_EDIT)
    def fb_sittings_fn(self):
        run(FLAPPY_BIRD_EDIT)
    def sn_sittings_fn(self):
        # os.system(SN_Game_handle)
        CMD = subprocess.Popen(SN_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()
    def xo_sittings_fn(self):
        CMD = subprocess.Popen(XO_Game_handle, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CMD.stdout.read()
        CMD.stderr.read()

    # Handling home tabe buttons #
    def open_doc(self):
        run(DOCUMENTATION_PATH)
    def visit_github(self):
        run(VISIT_REPOSITORY)
    def get_feedback(self):
        run(signin_path)
        run(FEEDBACK)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationUI()
    app.exec_()

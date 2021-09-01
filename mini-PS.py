import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
from Cores.functions import run, read_json, logger
from Cores.sittings_runner import runner as rn

# Reading pathes from profile.json file.
os.chdir(os.path.dirname(__file__))
pathes = read_json(r"Cores\Profile.json")
ALIEN_INVASION_PATH = pathes["ALIEN_INVASION_PATH"]
FLAPPY_BIRD_PATH = pathes["FLAPPY_BIRD_PATH"]
SNAKE_PATH = pathes["SNAKE_PATH"]
TIC_TAC_TOE_PATH = pathes["TIC_TAC_TOE_PATH"]
DOCUMENTATION_PATH = pathes["DOCUMENTATION_PATH"]
VISIT_REPOSITORY = 'explorer "https://github.com/0xGhazy/mini-PS"'
FEEDBACK = pathes["FEEDBACK"]
SIGNIN_PATH = pathes["SIGNIN_FRAME_PATH"]
signin_path = r"Cores\signin_frame.py"


class ApplicationUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationUI, self).__init__()
        # loading .ui design file
        os.chdir(os.path.dirname(__file__))
        uic.loadUi("UI\mini_PS_UI.ui", self)
        # hidding tab widgets bar
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.tabBar().setVisible(False)
        # display the window
        self.show()
        self.HandelButtons()

    def HandelButtons(self):
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
        self.take_backup.clicked.connect(self.get_backup)


    # Handling navigaionbuttons #
    def ch_to_home(self):
        """ Changing tab page to home page """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(0)
        logger("Info", "mini-PS.py > Navigate to home tabe.")

    def ch_to_ai(self):
        """  Changing tab page to Alien invasion game."""
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(1)
        logger("Info", "mini-PS.py > Navigate to alien invasion tab.")

    def ch_to_fb(self):
        """ Changing tab page to flappy bird page. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(2)
        logger("Info", "mini-PS.py > Navigate to flappy birds tab.")

    def ch_to_sn(self):
        """ Changing tab page to snake game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(3)
        logger("Info", "mini-PS.py > Navigate to snake tabe.")

    def ch_to_xo(self):
        """ Changing tab page to xo game. """
        self.tabWidgets = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.tabWidgets.setCurrentIndex(4)
        logger("Info", "mini-PS.py > Navigate to tic tac toe tabe.")


    # Handling game start buttons #
    def start_ai(self):
        logger("Info", "mini-PS.py > Starting alien invasion game.")
        run(ALIEN_INVASION_PATH)
        logger("Info", "mini-PS.py > Ending alien invasion game.")

    def start_fb(self):
        logger("Info", "mini-PS.py > Starting flappy birds game.")
        run(FLAPPY_BIRD_PATH)
        logger("Info", "mini-PS.py > Ending flappy birds game.")

    def start_sn(self):
        logger("Info", "mini-PS.py > Starting snake game.")
        run(SNAKE_PATH)
        logger("Info", "mini-PS.py > Ending snake game.")

    def start_xo(self):
        logger("Info", "mini-PS.py > Starting tic tac toe game.")
        run(TIC_TAC_TOE_PATH)
        logger("Info", "mini-PS.py > Ending tic tac toe game.")


    # Handling Sittings buttons #
    def ai_sittings_fn(self):
        logger("Info", "mini-PS.py > Starting alien invasion game sittings")
        rn.run_ai_sittings()
        logger("Info", "mini-PS.py > Ending alien invasion game sittings")

    def fb_sittings_fn(self):
        logger("Info", "mini-PS.py > Starting flappy birds game sittings.")
        rn.run_fb_sittings()
        logger("Info", "mini-PS.py > Ending flappy birds game sittings.")

    def sn_sittings_fn(self):
        logger("Info", "mini-PS.py > Starting snake game sittings.")
        rn.run_sn_sittings()
        logger("Info", "mini-PS.py > Ending snake game sittings.")
        
    def xo_sittings_fn(self):
        logger("Info", "mini-PS.py > Starting tic tac toe game sittings.")
        rn.run_xo_sittings()
        logger("Info", "mini-PS.py > Ending tic tac toe game sittings.")


    # Handling home tabe buttons #
    def open_doc(self):
        logger("Info", "mini-PS.py > Open project documentation.")
        run(DOCUMENTATION_PATH)

    def visit_github(self):
        logger("Info", "mini-PS.py > Visiting project remote repository.")
        run(VISIT_REPOSITORY)

    def get_feedback(self):
        run(FEEDBACK)

    def get_backup(self):
        logger("Info", "mini-PS.py > Try to backup games sittings.")
        run(SIGNIN_PATH)


# ================================= Application calling start here ================================= #


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationUI()
    app.exec_()

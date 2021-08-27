import os
from time import sleep
from Cores.functions import create_json


MAIN_APPLICATION_PATH =  os.path.dirname(__file__)
# Don't touch it's art :) Hahahaha, no i'm joking any change here will affect the whole application.
default_profile_content = {
    "DATABASE_PATH": r"{0}\Database\users.db".format(MAIN_APPLICATION_PATH),
    "LOGGING_PATH" : r"{0}\Database\users.db".format(MAIN_APPLICATION_PATH),
    "ALIEN_INVASION_PATH" : r"{0}\Games\Alien_Invasion\alien_invasion.py".format(MAIN_APPLICATION_PATH),
    "ALIEN_INVASION_CONF" : r"{0}\Games\Alien_Invasion\ai_configurations.json".format(MAIN_APPLICATION_PATH),
    "ALIEN_INVASION_EDIT" : r"{0}\Cores\edit_ai.py".format(MAIN_APPLICATION_PATH),
    "FLAPPY_BIRD_PATH" : r"{0}\Games\Flappy_Bird\fb_game.py".format(MAIN_APPLICATION_PATH),
    "FLAPPY_BIRD_CONF" : r"{0}\Games\Flappy_Bird\fb_configuration.json".format(MAIN_APPLICATION_PATH),
    "FLAPPY_BIRD_EDIT" : r"{0}\Cores\edit_fb.py".format(MAIN_APPLICATION_PATH),
    "SNAKE_PATH" : r"{0}\Games\Snake\Snake.py".format(MAIN_APPLICATION_PATH),
    "SNAKE_CONF" : r"{0}\Games\Snake\sn_configuration.json".format(MAIN_APPLICATION_PATH),
    "SNAKE_EDIT" : r"{0}\Games\Snake\edit_sn.py".format(MAIN_APPLICATION_PATH),
    "TIC_TAC_TOE_PATH" : r"{0}\Games\TicTacToe\XO.py".format(MAIN_APPLICATION_PATH),
    "TIC_TAC_TOE_CONF" : r"{0}\Games\TicTacToe\xo_configuration.json".format(MAIN_APPLICATION_PATH),
    "TIC_TAC_TOE_EDIT" : r"{0}\Games\TicTacToe\edit_xo.py".format(MAIN_APPLICATION_PATH),
    "DOCUMENTATION_PATH" : r"{0}\Documentation\Docs.html".format(MAIN_APPLICATION_PATH),
    "VISIT_REPOSITORY" : "explorer 'https://github.com/0xGhazy/mini-PS'",
    "SIGNUP_FRAME_PATH" : r"{0}\Cores\signup_frame.py".format(MAIN_APPLICATION_PATH),
    "FEEDBACK" : r"{0}\Cores\feedback.py".format(MAIN_APPLICATION_PATH)
}


def install_req():
    libs = ['pygame', 'PyQt5']
    for i in libs:
        print("[+] Installing {}".format(i))
        os.system('pip install {}'.format(i))
        print("""\n\n===================={} Has installed successfully <3====================\n\n""".format(i))
        sleep(3)
        os.system('cls')

def create_profile(default_profile_content):
    CD = os.path.dirname(__file__)
    path = r"{0}\Cores\profile.py".format(CD)
    with open(path, "w+") as f:
        f.write(default_profile_content)

def signup_call():
    path = MAIN_APPLICATION_PATH + "\Cores\signup_frame.py"
    os.system(path)


if __name__ == '__main__':
    #install_req()
    create_profile(str(default_profile_content))
    signup_call()
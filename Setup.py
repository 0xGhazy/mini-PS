import os
import json


MAIN_APPLICATION_PATH =  os.path.dirname(__file__)


def create_profile():
    # creating profile file [all pathes handler]
    profile_content = {
    "DATABASE_PATH": r"{0}\Database\users.db".format(MAIN_APPLICATION_PATH),
    "LOGGING_PATH" : r"{0}\Database\log.txt".format(MAIN_APPLICATION_PATH),
    "ALIEN_INVASION_PATH" : r"{0}\Games\Alien_Invasion\alien_invasion.py".format(MAIN_APPLICATION_PATH),
    "ALIEN_INVASION_CONF" : r"{0}\Games\Alien_Invasion\ai_configurations.json".format(MAIN_APPLICATION_PATH),
    "FLAPPY_BIRD_PATH" : r"{0}\Games\Flappy_Bird\fb_game.py".format(MAIN_APPLICATION_PATH),
    "FLAPPY_BIRD_CONF" : r"{0}\Games\Flappy_Bird\fb_configuration.json".format(MAIN_APPLICATION_PATH),
    "SNAKE_PATH" : r"{0}\Games\Snake\Snake.py".format(MAIN_APPLICATION_PATH),
    "SNAKE_CONF" : r"{0}\Games\Snake\sn_configuration.json".format(MAIN_APPLICATION_PATH),
    "TIC_TAC_TOE_PATH" : r"{0}\Games\TicTacToe\XO.py".format(MAIN_APPLICATION_PATH),
    "TIC_TAC_TOE_CONF" : r"{0}\Games\TicTacToe\xo_configuration.json".format(MAIN_APPLICATION_PATH),
    "DOCUMENTATION_PATH" : r"{0}\Documentation\Docs.html".format(MAIN_APPLICATION_PATH),
    "VISIT_REPOSITORY" : "explorer 'https://github.com/0xGhazy/mini-PS'",
    "SIGNUP_FRAME_PATH" : r"{0}\Cores\signup_frame.py".format(MAIN_APPLICATION_PATH),
    "SIGNIN_FRAME_PATH" : r"{0}\Cores\signin_frame.py".format(MAIN_APPLICATION_PATH),
    "FEEDBACK" : r"{0}\Cores\feedback.py".format(MAIN_APPLICATION_PATH)
    }
    path = r"{0}\Cores\Profile.json".format(MAIN_APPLICATION_PATH)
    with open(path, 'w') as f:
        json.dump(profile_content, f)


def install_req():
    # installing required modules
    libs = ['pygame', 'PyQt5']
    for i in libs:
        print("[+] Installing {}".format(i))
        os.system('pip install {}'.format(i))


def signup_call():
    # calling signup_frame
    path = MAIN_APPLICATION_PATH + "\Cores\signup_frame.py"
    os.system(path)


def main():
    install_req()
    create_profile()
    signup_call()


# calling our ptogram.
main()

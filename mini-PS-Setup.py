import os
from time import sleep


def install_req():
    libs = ['pygame', '', '', '']
    for i in libs:
        print("[+] Installing {}".format(i))
        os.system('pip install {}'.format(i))
        print("""\n\n===================={} Has installed successfully <3====================\n\n""".format(i))
        sleep(3)
        os.system('cls')


install_req()
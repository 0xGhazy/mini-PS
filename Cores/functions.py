import os
import json
import smtplib
import hashlib
from getpass import getuser
import subprocess
from datetime import datetime


# handling project email from feedbacks
PROJECT_EMAIL = "minips941@gmail.com"
PROJECT_PASSWORD = "123456789pythonproject"


def logger(msg_type, message):
    os.chdir(os.path.dirname(__file__))
    log_statement = f"[{msg_type}] :: {datetime.now()} :: {getuser()} :: {message}\n"
    log_path = read_json("Profile.json")
    log_path = log_path["LOGGING_PATH"]
    with open(log_path, "a") as log:
        log.write(log_statement)


def calc_hash(plain_text, hash_type = "sha256"):
	hashed_text = hashlib.new(hash_type)
	hashed_text.update(plain_text.encode())
	hashing_result = hashed_text.hexdigest()
	return hashing_result


def create_json(file_name, data_dictionary):
    with open(file_name, 'w') as f:
        json.dump(data_dictionary, f)


def read_json(file_path):
    with open(file_path, 'r+') as f:
        content = json.load(f)
    return content


def send_feedback(username, contact_mail, feedback):
    # TODO: Need to accept attachments and fancy emails
    """ Function to send users feed back to the auther mail or org mail using stmp.gmail server with secure access
    it doesn't accept 2FA accounts, for connection problems check this: https://www.google.com/settings/security/lesssecureapps """

    message_content = f"""
    Hello it's a feedback from {username}:{contact_mail}\n
    feedback-Content:\n
    {feedback}\n
    By: mini-PS mailing system :)\n"""

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    try:
        # login to stmp server
        smtpserver = smtplib.SMTP(smtp_server, port)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(PROJECT_EMAIL, PROJECT_PASSWORD)
        # sender, recv, msg
        smtpserver.sendmail(PROJECT_EMAIL, contact_mail, feedback)
        logger("Info", "functions.py:send_feedback() > try to send the feedback.")
    except Exception as error:
        print(error)
    finally:
        logger("Info", "functions.py:send_feedback() > Done.")
        smtpserver.quit()
        logger("Info", "functions.py:send_feedback() > closing the stmp server.")


def run(command):
    CMD = subprocess.Popen(command, shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return CMD.stdout.read().decode(), CMD.stderr.read().decode()

# Updating This function to send backup to user account.
def backup(recver_email):
    """ Function to read all games configurations files and then copy its content to txt file """
    os.chdir(os.path.dirname(__file__))
    json_pathes = read_json(f"Profile.json")
    ALIEN_INVASION_CONF = json_pathes["ALIEN_INVASION_CONF"]
    FLAPPY_BIRD_CONF = json_pathes["FLAPPY_BIRD_CONF"]
    SNAKE_CONF = json_pathes["SNAKE_CONF"]
    TIC_TAC_TOE_CONF = json_pathes["TIC_TAC_TOE_CONF"]
    Desktop_path = r"C:\Users\{0}\Desktop".format(getuser())
    l = [ALIEN_INVASION_CONF, FLAPPY_BIRD_CONF, SNAKE_CONF, TIC_TAC_TOE_CONF]
    message = ""
    for i in l:
        data = read_json(i)
        with open(f"{Desktop_path}\Backup.txt", "a+") as back:
            message += f"\n\n{data}\n\n"
    print(message)
    send_feedback(PROJECT_EMAIL, recver_email, message)

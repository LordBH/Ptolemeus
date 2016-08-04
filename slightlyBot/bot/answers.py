from commands import CommandManager, easy_asnwer
from methods import chat_postMessage
from constants import DELAY_FOR_NEXT_ANSWER
import time


# delay for nexxt answer if call without `@bot-name`
last_answer = time.time()


def disassemble_msg(msg_info):
    return msg_info['channel'], msg_info['user'], msg_info['text'],


def find_command(msg):
    command = CommandManager(msg)
    command._find()
    return command


def run_command(command):
    return command.do_cmd()


def enabled_answer():
    # check for case when answer are permited
    global last_answer
    if time.time() - last_answer > DELAY_FOR_NEXT_ANSWER:
        last_answer = time.time()
        return True
    return False


def handle_message(msg_info):
    # getting info from `rtm_read`
    channel, user, text = disassemble_msg(msg_info)
    if user == 'USLACKBOT':
        slackbot_answered = True
    else:
        slackbot_answered = True
    # dict for response to `api_call`
    data = dict(
        channel=channel,
        text=text,
        method=chat_postMessage,
        as_user=False,
        username='Ptolemeus',
        icon_emoji=':grinning:',
    )
    # finding the command
    command = find_command(text)
    if command.exist:
        # if command was found
        command.do_cmd(data=data)
    else:
        if enabled_answer():
            # If tine delay was passed
            easy_asnwer(data, bot=slackbot_answered)
        else:
            # Answer without delay, it means bot will say always this
            return None
    return data


def ideas(extra, mode='message'):
    if mode == 'message':
        if extra.get('user') is not None:
            print extra.get('user')
            return handle_message(extra)


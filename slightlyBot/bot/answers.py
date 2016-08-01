from commands import Commands
from methods import *
from mind import *


def disassemble_msg(msg_info):
    return msg_info['channel'], msg_info['user'], msg_info['text'],


def find_command(msg):
    command = Commands(msg)
    command._find()
    return command


def run_command(command):
    return command.do_cmd()


def handle_message(msg_info):
    channel, user, text = disassemble_msg(msg_info)
    print user
    command = find_command(text)
    if command.exist:
        text = command.do_cmd()
    else:
        text = MIND['random_answer']()

    data = dict(
        channel=channel,
        text=text,
        method=chat_postMessage,
        as_user=False,
        username='Ptolemeus',
        icon_emoji=':grinning:',
    )

    return data


def ideas(extra, mode='message'):
    if mode == 'message':
        if extra.get('user') is not None:
            return handle_message(extra)


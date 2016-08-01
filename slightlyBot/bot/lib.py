from constants import USERS, EMOJI, logger
from reply import COMMAND_NOT_EXIST
import random
import string



def _exit(*args, **kwargs):
    logger
    exit()


def answer_to_slack_bot(*args, **kwargs):
    postMessage['text'] = "Smart ass !"
    postMessage['channel'] = kwargs['channel']
    postMessage['as_emoji'] = emoji()

    return postMessage


def create_random_token(*args, **kwargs):
    # Creates random tokem
    token = [random.choice(string.ascii_uppercase + string.digits) for rand in range(8)]
    user_id = random.choice(USERS.keys())
    user = USERS[user_id]['name']
    response = "%s\n%s" % (user, ''.join(token))
    return response


def emoji(*args, **kwargs):
    return EMOJI['trollface']


def dreaming(*args, **kwargs):
    time.sleep(3600)


def random_answer(*args, **kwargs):
    return random.choice(COMMAND_NOT_EXIST)

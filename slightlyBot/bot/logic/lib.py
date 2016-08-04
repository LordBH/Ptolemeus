from bot._log import logger
import random
import string



COMMAND_NOT_EXIST = [
    'May itself this command',
    'Don\'t do it',
    'I\'ll think about that :) but i poor for this info',
]


def _exit(*args, **kwargs):
    logger.info("Exit API")
    exit()


def answer_to_slack_bot(*args, **kwargs):
    data = kwargs['data']
    data['text'] = "Smart ass !"
    data['as_emoji'] = emoji()


def create_random_token(*args, **kwargs):
    # Creates random tokem
    token = [random.choice(string.ascii_uppercase + string.digits) for rand in range(8)]
    user_id = random.choice(USERS.keys())
    user = USERS[user_id]['name']
    response = "%s\n%s" % (user, ''.join(token))
    return response


def emoji(*args, **kwargs):
    print CHANNELS, USERS, EMOJI
    return EMOJI['trollface']


def dreaming(*args, **kwargs):
    logger.info("Goind sleep for 1 hour")
    time.sleep(3600)


def random_answer(*args, **kwargs):
    return random.choice(COMMAND_NOT_EXIST)

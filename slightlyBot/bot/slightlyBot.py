from constants import *
import answers
import logging
import slackclient
import time


# instantiate Slack & Twilio clients
slack_client = slackclient.SlackClient(TOKEN)


def run():
    get_team_info()
    get_slack_emoji()
    start_bot_loop()


def call(*args, **kwargs):
    return slack_client.api_call(*args, **kwargs)


def start_bot_loop():
    logger.info("ID: %r started, NAME: %r." % (BOT_ID, USERS[BOT_ID]['name']))
    while True:
        pike = parse_slack_output(slack_client.rtm_read())
        if pike is not None:
            reply(pike)
        time.sleep(WEBSOCKET_DELAY)


def reply(output):
    if 'type' in output:
        if output['type'] == 'message':
            response = answers.ideas(output, mode='message')
            if response is not None:
                call(**response)


def get_team_info():
    global CHANNELS, USERS
    # Get info about channels
    channels = call('channels.list')
    users = call('users.list')
    if not (users['ok'] or channels['ok']):
        logger.warning("Get info fail, users = %r, channels = %r" % \
                       (users['ok'] or channels['ok']))
    logger.info("Team info fetched")
    for channel in channels['channels']:
        CHANNELS[channel['id']] = channel
    for user in users['members']:
        USERS[user['id']] = user


def get_slack_emoji():
    global EMOJI
    emoji = call('emoji.list')
    logger.info("Emotion info fetched")
    EMOJI = emoji['emoji']


def parse_slack_output(output_list):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    if output_list and len(output_list) > 0:
        for output in output_list:
            return output

    return None


def start_logging():
    global logger
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)


def main():
    # starting logging
    start_logging()
    # check for connection to Slack
    connected = slack_client.rtm_connect()
    if connected:
        # running API
        run()
        exit()
    logger.critical("Wrong Bot ID %s or Team TOKEN %s" % (BOT_ID, TOKEN))

from _log import logger
from constants import TOKEN, BOT_ID, BOT_DIRECT_CALL, WEBSOCKET_DELAY
import answers
import slackclient
import time
import btools


# instantiate Slack & Twilio clients
slack_client = slackclient.SlackClient(TOKEN)


def call(*args, **kwargs):
    return slack_client.api_call(*args, **kwargs)


def get_team_info():
    # Get info about channels
    channels = call('channels.list')
    logger.info("Channels info fetched")
    CHANNELS = {}
    for channel in channels['channels']:
        CHANNELS[channel['id']] = channel
    users = call('users.list')
    logger.info("Users info fetched")
    USERS = {}
    for user in users['members']:
        USERS[user['id']] = user
    emoji = call('emoji.list')
    logger.info("Emotions info fetched")
    EMOJI = emoji['emoji']
    if not (users['ok'] or channels['ok']):
        logger.warning("Get info fail, users = %r, channels = %r, emoji = %r" %
                       (users['ok'] or channels['ok'], emoji['ok']))
    flows = [(CHANNELS, 'channels.info'),
             (USERS, 'users.info'),
             (EMOJI, 'emoji.info')]
    btools.sflow(flows, folder='team-info')


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


def reply(output):
    if 'type' in output:
        if output['type'] == 'message':
            response = answers.ideas(output, mode='message')
            if response is not None:
                call(**response)


def start_bot_loop():
    logger.info("BOT %r started" % (BOT_ID,))
    while True:
        pike = parse_slack_output(slack_client.rtm_read())
        if pike is not None:
            reply(pike)
        time.sleep(WEBSOCKET_DELAY)

from lib import USERS, CHANNELS, EMOJI
from bot.btools import gflow
from bot import logger



def get_flows():
    CHANNELS = gflow('channels.info', folder='team-info')
    USERS = gflow('users.info', folder='team-info')
    EMOJI = gflow('emoji.info', folder='team-info')
    logger.debug("Info loaded: channel = %r, users = %r, emoji = %r" % \
                (bool(CHANNELS), bool(USERS), bool(EMOJI)))

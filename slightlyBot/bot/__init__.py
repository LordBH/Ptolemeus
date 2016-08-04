from app import *
from _log import *
from logic.mtools import get_flows


def main():
    # check for connection to Slack
    connected = slack_client.rtm_connect()
    if connected:
        # running API
        get_team_info()
        get_flows()
        start_bot_loop()
        logger.info("Exiting API")
        exit()
    logger.critical("Wrong Bot ID %s or Team TOKEN %s" % (BOT_ID, TOKEN))

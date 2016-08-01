import lib
from mind import MIND


class Commands:

    cmds = set(MIND.keys())


    def __init__(self, msg):
        # formated message
        self.msg = msg.lower().strip()
        # all message keys in set
        self.msg_keys = set(self.msg.split())
        # Commands which bot has in message
        self.commons = None
        # message startswith
        self.starts = ''
        self.func = None

        self.exist = False

    def _find(self):
        # Find commands which bot has in message
        self.commons = self.msg_keys & self.cmds
        if self.commons:
            # if command found in mind.MIND
            # determine which symbol start message
            self.starts = self.msg[0]
            # for case with only one found command
            if len(self.commons) == 1:
                # commands for mananaging bot
                if self.starts == '$':
                    self.func(self.msg)
                # For special use, not use now
                # elif self.starts == '@':
                #     pass
                else:
                    # gets name of command from set
                    bot_cmd = list(self.commons)[0]
                    # get function with value of `bot_cmd`
                    self.func = MIND[bot_cmd]
            if self.func is not None:
                self.exist = True


    def do_cmd(self):
        return self.func(self.msg)

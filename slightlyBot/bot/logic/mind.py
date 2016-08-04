import lib


# Bot will respond on this commands
MIND = {
    'answer_to_slack_bot': lib.answer_to_slack_bot,
    'off': lib._exit,
    'token': lib.create_random_token,
    'random_answer': lib.random_answer,
    'sleep': lib.dreaming,
}

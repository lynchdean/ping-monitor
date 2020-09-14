import asyncio

import tweepy


class TwitterListener(tweepy.StreamListener):
    def __init__(self, disc, loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discord = disc
        self.loop = loop

    def on_status(self, status):
        if from_creator(status):
            self.send_message(status)

    def send_message(self, msg):
        future = asyncio.run_coroutine_threadsafe(self.discord(msg), self.loop)
        future.result()


def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id is not None:
        return False
    elif status.in_reply_to_screen_name is not None:
        return False
    elif status.in_reply_to_user_id is not None:
        return False
    else:
        return True

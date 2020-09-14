import asyncio

import tweepy


class TwitterListener(tweepy.StreamListener):
    def __init__(self, disc, loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discord = disc
        self.loop = loop

    def on_status(self, status):
        self.send_message(status)

    def send_message(self, msg):
        future = asyncio.run_coroutine_threadsafe(self.discord(msg), self.loop)
        future.result()
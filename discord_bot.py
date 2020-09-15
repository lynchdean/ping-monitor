import asyncio
import re

import discord
import tweepy

import follow
import secrets
from twitter_listener import TwitterListener

# Twitter secrets
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret
consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
# Discord Secrets
discord_token = secrets.discord_token
channel_id = secrets.channel_id


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

        api = tweepy.API(get_auth())
        my_stream = tweepy.Stream(
            auth=api.auth,
            listener=TwitterListener(disc=self.send_tweet, loop=asyncio.get_event_loop())
        )
        my_stream.filter(follow=follow.all_, is_async=True, )

    async def send_tweet(self, status):
        channel = self.get_channel(channel_id)
        url = f"https://twitter.com/{status.user.screen_name}/status/{status.id_str}"

        embed = discord.Embed(title=status.user.screen_name, description=status.text, url=url, colour=0x1DA1F2)
        embed.set_thumbnail(url=status.user.profile_image_url_https)
        tweet_urls = re.findall(r'(https?://\S+)', status.text)
        for idx, url in enumerate(tweet_urls):
            embed.add_field(name="url [{0}]".format(str(idx + 1)), value=url, inline=False)

        await channel.send(embed=embed)


def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


client = MyClient()
client.run(discord_token)

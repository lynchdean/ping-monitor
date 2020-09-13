import tweepy
import yaml


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


def get_auth():
    secrets = yaml.load(open('secrets.yaml'), Loader=yaml.FullLoader)["twitter"]
    auth = tweepy.OAuthHandler(secrets["consumer_key"], secrets["consumer_secret"])
    auth.set_access_token(secrets["access_token"], secrets["access_token_secret"])
    return auth


def main():
    auth = get_auth()
    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    myStream.filter(follow=["24748610"])
    # public_tweets = api.home_timeline()
    # for tweet in public_tweets:
    #     print(tweet.text)


if __name__ == '__main__':
    main()

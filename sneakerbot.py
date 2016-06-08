#!/bin/bash
import time
import tweepy
import os

ckey = 'f9Po492GGWCtNv0ahUtK6SmlY'
consumer_secret = 'HUJd0BAuarrZ7aTkU263faiahpbf3hVgMQiGGEgmNfWegDtFFn'
access_token_key = '734936642536898560-kpbhg2WRms7WKeN7acpRxhmuXWYwCw8'
access_token_secret = 'Otk9fVmM80Ui274SJ1BNrvDbm7vOIUc0vxllkFa9tVqrP'


class  Tweets():
    def setup_stream_listener(self):
            """
            Setup Twitter API streaming listenner
            """
            listener = Listener()
            listener.set_tweets(self)
            auth = tweepy.OAuthHandler(ckey,consumer_secret)
            auth.set_access_token(access_token_key, access_token_secret)

            self.stream = tweepy.Stream(auth, listener, timeout=3600)

    def stream_filter(self):
        """
        Start listening based on a list of account names.
        """
        track_list = 'SneakerBot0929'
        print('track_list: %s', track_list)
        while True:
            try:
                self.stream.filter(track=[track_list])
            except (Exception) as e:
                print(e)



class Listener(tweepy.StreamListener):
    """
    Twitter Streaming API listener
    """
    def on_status(self, status):
        """
        Callback when post is received ok
        """
        if status.author.lang == 'en':
            print(status.text)
            message = {'author_name': status.author.screen_name,
                       'author_id': status.author.id,
                       'id': status.id,
                       'text': status.text,
                       'retweeted': status.retweeted,
                       'coordinates': status.coordinates,
                       'time': int(time.time())}

            print(message)
            print ('author: %s, tweet: %s' % (status.author.screen_name, status.text))

    def set_tweets(self, t):
        """
        Set Tweets class object
        """
        self.tweets = t



if __name__ == '__main__':
    tweets = Tweets()
    tweets.setup_stream_listener()
    tweets.stream_filter()

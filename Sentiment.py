import tweepy
from tweepy import Stream
from text2emotion import get_emotion
import streamlit as st
import numpy as np
import pandas as pd
import time

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):

    def __init__(self, time_limit=10):
        self.start_time=time.time()
        self.time_limit=time_limit
        super(StreamListener, self).__init__()
    
    def on_status(self, status):
        if (time.time() - self.start_time) < self.time_limit:
            print(status.text)
            print("***************************Emotions detected******************************************")
            print(get_emotion(status.text))
            return True
        else:
            return False

listener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=listener)

stream.filter(track=['Presidential Debate'])

import tweepy
from tweepy import Stream
from text2emotion import get_emotion
import streamlit as st
import numpy as np
import pandas as pd
import time
import os
ckey,csecret,atoken,asecret = os.environ.get('ckey'),os.environ.get('csecret'),os.environ.get('atoken'),os.environ.get('asecret')
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
data=pd.DataFrame([{'Happy':0.0,'Angry':0.0,'Surprise':0.0,'Sad':0.0,'Fear':0.0}])

st.title("Sentwit")
st.subheader("Find out how the twitterati is feeling about a particular trend")
chart=st.line_chart(data)
st.text("Enter the keyword you want to track the emotions on, and hit enter! As simple as that :)")

class StreamListener(tweepy.StreamListener):

    def __init__(self, time_limit=10):
        self.start_time=time.time()
        self.time_limit=time_limit
        super(StreamListener, self).__init__()
    
    def on_status(self, status):
        if (time.time() - self.start_time) < self.time_limit:
            print(status.text)
            print("***************************Emotions detected******************************************")
            data_dict=get_emotion(status.text)
            data_dict={k:float(v) for k,v in data_dict.items()}
            data=pd.DataFrame([data_dict])
            chart.add_rows(data)
            print(data_dict)
            return True
        else:
            return False

listener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=listener)
user_input = st.text_input("Track", "Made with love")
stream.filter(track=[user_input])

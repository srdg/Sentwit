
# coding: utf-8

# In[1]:


import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re



# In[2]:


def calctime(a):
    return time.time()-a


# In[3]:


positive=0
negative=0
compound=0


# In[4]:


count=0
initime=time.time()
plt.ion()


# In[5]:


import keys

ckey=keys.ckey
csecret=keys.csecret
atoken=keys.atoken
asecret=keys.asecret


# In[6]:


class listener(StreamListener):
    
    def on_data(self,data):
        global initime
        t=int(calctime(initime))
        all_data=json.loads(data)
        #print(type(all_data['text']))
        tweet=all_data["text"]
        #username=all_data["user"]["screen_name"]
        tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
        blob=TextBlob(tweet.strip())

        global positive
        global negative     
        global compound  
        global count
        
        count=count+1
        senti=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity >= 0:
                positive=positive+sen.sentiment.polarity   
            else:
                negative=negative+sen.sentiment.polarity  
        compound=compound+senti        
        #print (count,end='')
        print ('#'+str(count) + ":"+ tweet.strip())
        #print (senti)
        #print (t)
        #print (str(positive) + ' ' + str(negative) + ' ' + str(compound) )
        
    
        plt.axis([ 0, 200, -20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[positive],'go--',[t] ,[negative],'ro',[t],[compound],'bo')
        plt.draw()
        plt.pause(0.05)
        if count==200:
            return False
        else:
            return True
        
    def on_error(self,status):
        print (status)


# In[7]:


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


# In[8]:


twitterStream=  Stream(auth, listener(count))
twitterStream.filter(track=["Narendra Modi"])


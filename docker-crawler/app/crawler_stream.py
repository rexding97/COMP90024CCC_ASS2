import tweepy
import json
import sys
#from database import tweetsDB
from database_cloudant import CloudantDB
from sentiment_analysis import sentiment_analyzer
#import geopandas
from crawler_keywords import words
from zoneFeatures import zone_info, getBoundingbox
from TwitterProcessor import filtKeywords, filtLocations, parseTweet
import time

# Yanze' Key
consumer_key="7jWNg1jENq2hvmAzqZeKvfcF4"
consumer_secret="l9C5m1JCbdYTOTbLYWC3W8AkEE7BC3ofHkLDgos37clTxDJUyc"
access_token="1366203266162253825-CvOHBqKvMEqbN9iOpr975BOg6OttrO"
access_token_secret="7lRZSvtwo2bh8uuM3J2wJbb3rFSSBYy7zfR1u8H30Fb27"
"""
consumer_key = "Ozup2OAf8pHZhha38AELtzswf"
consumer_secret = "T0QCvEWdUm2PakSKDsho9usdvaPWZsUB0hhB2XE1JwgwCGp7wV"
access_token = "1252083222189498368-BZUECSVoWd6IDSWGnETwH4krVS3AHh"
access_token_secret = "y9UNO50rhFndcMPy4S4cY5qLEcZdz6NygWyl8t0ZY7H8s"
"""
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

env_path = Path('./crawler.env')
load_dotenv(dotenv_path=env_path, verbose=True)


USERNAME=os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")
def main():
    

    # connect database
    db_vac = CloudantDB("tweets_vaccine",USERNAME,PASSWORD,URL)
    db_covid = CloudantDB("tweets_covid",USERNAME,PASSWORD,URL)
    db_all = CloudantDB("tweets_no_keywords",USERNAME,PASSWORD,URL)
    db_raw = CloudantDB("tweets_raw",USERNAME,PASSWORD,URL)
    sa = sentiment_analyzer.SentimentAnalyzer()
    data=[]
    class UserTimelineListener():
        def __init__(self,api,keywords,locations):
            self.searched = set()
            self.api = api
            self.keywords = keywords
            self.locations = locations
        def searchUser(self,userid):
            if(userid in self.searched):
                print("user has already been searched")
                return
            self.searched.add(userid)
            try:
                tweets = self.api.user_timeline(user_id=userid, count=100, exclude_replies=True,lang='en')
            except tweepy.TweepError:
                print("API error")
                time.sleep(16*60)
                return
            print("searching user:",userid,"filtering ",len(tweets)," tweets")
            for tweet in tweets:
                zone = filtLocations(tweet,self.locations)
                if(zone is None):
                    continue
                db_raw.add_record(tweet._json)
                db_all.add_record(parseTweet(tweet,sa,zone,["no keywords"]))
                vac_words = filtKeywords(tweet,self.keywords['vaccine'])
                if(vac_words is not None):
                    record = parseTweet(tweet,sa,zone,vac_words)
                    data.append(record)
                    print("---new tweet found----- keywords:",vac_words,"zone",zone)
                    db_vac.add_record(record)
                    print("saved to database")
                    continue
                cov_words = filtKeywords(tweet,self.keywords['covid'])
                if(cov_words is not None):
                    record = parseTweet(tweet,sa,zone,cov_words)
                    data.append(record)
                    print("---new tweet found----- keywords:",cov_words,"zone",zone)
                    db_covid.add_record(record)
                    print("saved to database")
                
                
                
    
    class MyStreamListener(tweepy.StreamListener):
        def __init__(self,keywords,locations,userListener):
            super().__init__()
            self.keywords = keywords
            self.userListener = userListener
            self.locations = locations
        def on_status(self, status):
            if(status.place is not None):
                zone = filtLocations(status,self.locations)
                if(zone is not None):
                    db_raw.add_record(status._json)
                    db_all.add_record(parseTweet(status,sa,zone,["no keywords"]))
                vac_words = filtKeywords(status,self.keywords['vaccine'])
                if(vac_words is not None and zone is not None):
                    record = parseTweet(status,sa,zone,vac_words)
                    data.append(record)
                    print("---new tweet found----- keywords:",vac_words,"zone",zone)
                    db_vac.add_record(record)
                    print("saved to database")
                cov_words = filtKeywords(status,self.keywords['covid'])
                if(cov_words is not None and zone is not None):
                    record = parseTweet(status,sa,zone,cov_words)
                    data.append(record)
                    print("---new tweet found----- keywords:",cov_words,"zone",zone)
                    db_covid.add_record(record)
                    print("saved to database")
                
                try:
                    self.userListener.searchUser(status.user.id)
                except Exception as e:
                    print(e)
                    return
    
        def on_error(self, status_code):
            print(status_code)
            if status_code == 420:
                # returning False in on_error disconnects the stream
                time.sleep(60)
                return False

    
    # connect twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    


    box= getBoundingbox(zone_info["features"])
    box_1d = [j for sub in box.values() for j in sub]
    
    myUserListener = UserTimelineListener(api,words,box.keys())
    myStreamListener = MyStreamListener(words,box.keys(),myUserListener)
    while True:
        try:
            myStream = tweepy.Stream(auth, listener=myStreamListener)
            myStream.filter(locations=box_1d, languages=["en"])
        except Exception as e:
            time.sleep(5)
            print(e)

if __name__ == '__main__':
    main()
    """
    with open('data_streaming.json', 'w') as outfile:
        json.dump(data, outfile)
    
    
    import jsonlines
    with jsonlines.open('data_streaming.jsonl', mode='a') as writer:
        for d in data:
            writer.write(d)
    """

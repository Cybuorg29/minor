"""
Get the top 10 trending topics on Twitter with their volume using the Twitter API
"""

import tweepy

#Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_KEY", "ACCESS_SECRET")

#Create API Object
api = tweepy.API(auth)

#Get top 10 trending topics
trends = api.trends_place(23424975) # 23424975 is the WOEID code for the US

#Print the top 10 trending topics
for trend in trends[0]["trends"][:10]:
    print(trend["name"] + " (Volume: " + str(trend["tweet_volume"]) + ")")
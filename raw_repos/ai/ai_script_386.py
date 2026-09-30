import tweepy

# create OAuth handler
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# authenticate 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
  
# overridable get method
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 
 
# results
trends = api.trends_place(1) 
data = trends[0]
trends_list = data['trends']

# top 3 trending topics 
for i in range(3): 
    print(trends_list[i]['name'])
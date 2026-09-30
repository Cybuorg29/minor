import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://twitter.com/').text

soup = BeautifulSoup(website_url,'html.parser')

tweets_list = []
for tweet in soup.findAll('div',{'class':'tweet'}):
    text = tweet.find('p',{'class':'tweet-text'}).text
    tweets_list.append(text)

print(tweets_list)
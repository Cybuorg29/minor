import requests
import json 

def content_aggregator():
    api_url = "https://www.example.com/api/"
    response = requests.get(api_url)
    response_data = json.loads(response.text)
    for item in response_data:
        print(item)

if __name__ == '__main__':
    content_aggregator()
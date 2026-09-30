import requests

API_ENDPOINT = 'api.example.com/data'

response = requests.get(API_ENDPOINT)

if response.status_code == 200:
    data = response.json()
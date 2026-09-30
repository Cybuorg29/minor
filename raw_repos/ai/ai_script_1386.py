import json
import requests

url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=India'
response = requests.get(url)
data = json.loads(response.text)
population = data['query']['pages']['571045']['revisions'][0]['*'].split('\n')[3].split('=')[1].strip().split('|')[0]
print('The population of India is', population)
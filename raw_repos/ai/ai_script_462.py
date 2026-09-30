import requests

url = "http://openlibrary.org/api/books"
 
querystring = {"bibkeys":"ISBN:0201558025","format":"json","jscmd":"data"}

headers = {
    'cache-control': "no-cache",
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)
 
print(response.text)
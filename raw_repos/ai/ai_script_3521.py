import re
import requests

urls = set()
 
def get_urls(url):
    website = requests.get(url)
    content = website.text
    links = re.findall(r'<a .*?href=[\'"](.*?)[\'"].*?>', content)
 
    for i in links:
        if i.startswith("/"):
            base_url = url
            i = base_url + i
            if i in urls:
                continue
            urls.add(i)
            get_urls(i)
        elif url in i:
            if i in urls:
                continue
            urls.add(i)
            get_urls(i)
 
if __name__ == "__main__":
    get_urls("https://www.example.com")
    for i in urls:
        print(i)
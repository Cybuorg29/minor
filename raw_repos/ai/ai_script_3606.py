import re

html_code = '''
<a href="https://example.com/about">About</a>
<a href="https://example.com/products">Products</a>
'''

links = re.findall(r'href="(.*?)"', html_code)
print(links)
# Output: ['https://example.com/about', 'https://example.com/products']
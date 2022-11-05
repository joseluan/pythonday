import requests, re

response = requests.get('https://pythonscraping.com/pages/page1.html')

regex_title = re.search(r'<title[^>]*>(?P<title>[^<]+)', response.text, flags=re.DOTALL)

title = regex_title.group('title')

print(title)
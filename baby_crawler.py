import requests, re, time

def crawler(link: str):
    response = requests.get(link)
    regex_link = re.finditer(r'<a[^>]*href="(?P<link>[^"]+)"[^>]*>', response.text, flags=re.DOTALL)
    for link_temp in regex_link:
        link_temp = link_temp.group('link')
        print(link_temp)
        time.sleep(0.5)
        crawler(link_temp)



if __name__ == '__main__':
    crawler('https://pythonscraping.com/pages/aPage.html')
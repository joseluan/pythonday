import requests, re


def remove_tag(text):
    return re.sub(r'<[^>]*>', '', text)


response = requests.get('https://pythonscraping.com/pages/page3.html')

regex_linha = re.finditer(r'<tr[^>]*id="gift[^>]*>[^<]*<td[^>]*>(?P<title>[^<]*)</td>[^<]*<td[^>]*>(?P<description>.*?)</td>[^<]*<td[^>]*>(?P<cost>[^<]*)</td>[^<]*<td[^>]*>[^<]*<img[^<]*src="\.\.(?P<image>[^"]*)', response.text, flags=re.DOTALL)

linhas = []
for linha in regex_linha:
    title = linha.group('title')
    
    description = linha.group('description')
    description = remove_tag(description)
    
    cost = linha.group('cost')
    image = 'https://pythonscraping.com' + linha.group('image')

    linhas.append({
        'Title': title, 'Description': description, 'Cost': cost, 'Image': image
    })


print(linhas)
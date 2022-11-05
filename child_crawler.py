import requests, re, time


visited_links=[]
def crawler(link: str, recursion=0):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://compras.natal.rn.gov.br',
        'Referer': 'https://compras.natal.rn.gov.br/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(link, headers=headers)
    regex_link = re.finditer(r'<a[^>]*href="(?P<link>[^"]+)"[^>]*>', response.text, flags=re.DOTALL)
    recursion += 1
    for link_temp in regex_link:
        link_temp = link_temp.group('link')
        if link_temp not in visited_links:
            print(recursion, '-', link_temp)
            visited_links.append(link_temp)
            if recursion <= 2:
                try:
                    crawler(link_temp, recursion=recursion)
                    time.sleep(0.5)
                except Exception:
                    pass



if __name__ == '__main__':
    crawler('https://compras.natal.rn.gov.br/')
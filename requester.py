import requests
import random
import json


class Requester:
    

    def __init__(self):
        self.proxies = []
        self.attemps = 15
        # with open('proxies.json', 'r') as arq:
        #     self.proxies = json.loads(arq.read())
            #self.proxies = [proxie for proxie in self.proxies if proxie['pais'] == 'Brazil']


    def request(self, method: str, url:str, session=None, **options):
        for _ in range(self.attemps):
            try:
                proxie = {}
                if self.proxies:
                    proxie = random.choice(self.proxies)
                    protocolo = proxie["protoloco"].lower()
                    proxie = {
                        'http': f'{protocolo}://{proxie["ip"]}:{proxie["porta"]}',
                        'https': f'{protocolo}://{proxie["ip"]}:{proxie["porta"]}'
                    }

                if session is not None:
                    response = session.request(method, url, proxies=proxie, **options)
                else:
                    response = requests.request(method, url, proxies=proxie, **options)
                
                if response.status_code != 403:
                    return response

            
            except Exception as e:
                print(e)

        return requests.Response()


requester = Requester()
headers = {
    'authority': 'ident.me',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-PT,pt;q=0.9',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}
r = requester.request(method='get', url='https://ident.me', headers=headers)
print(r.text)
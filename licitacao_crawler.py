import requests
import re
import time
import json


session = requests.session()

regex_link = r'paginas\/licitacoes\/consulta\/[^\"]+'
regex_modalidade = r'<th[^>]*>\s*Modalidade\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'
regex_nr_licitacao = r'<th[^>]*>\s*Nr\.Licitação\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'
regex_nr_processo = r'<th[^>]*>\s*Nr\.Processo\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'
regex_nr_titulo = r'<th[^>]*>\s*Titulo\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'
regex_secretaria = r'<th[^>]*>\s*Secretaria\s+Licitante\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'
regex_data_abertura = r'<th[^>]*>\s*Data\s+Abertura\s*</th>[^<]*<td[^>]*>(?P<value>[^<]*)'


dados_licitacoes = {'licitacoes': []}

for indice in range(1, 10):
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

    data = {
        'mod': '',
        'pagina': indice,
    }

    response = session.post('https://compras.natal.rn.gov.br/', headers=headers, data=data)    
    
    links = re.finditer(regex_link, response.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE)
    
    
    for link_licitacao in links:
        link_licitacao = f'https://compras.natal.rn.gov.br/{link_licitacao.group()}'
        response_licitacao = session.get(link_licitacao, headers=headers)    
        
        modalidade = re.search(regex_modalidade, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        nr_licitacao = re.search(regex_nr_licitacao, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        nr_processo = re.search(regex_nr_processo, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        titulo = re.search(regex_nr_titulo, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        secretaria = re.search(regex_secretaria, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        data_abertura = re.search(regex_data_abertura, response_licitacao.content.decode('iso-8859-1'), flags=re.DOTALL|re.IGNORECASE).group('value')
        
        licitacao = {   
            'Titulo': titulo,
            'Modalidade': modalidade,
            'NrLicitacao': nr_licitacao,
            'NrProcesso': nr_processo,
            'SecretariaLicitante': secretaria,
            'DataAbertura': data_abertura,
        }
        
        
        print(titulo)
        
        dados_licitacoes['licitacoes'].append(licitacao)
        time.sleep(0.5)

    print('Pagina:', indice)


with open('out.json', 'w', encoding='iso-8859-1') as arq:
    arq.write(json.dumps(dados_licitacoes, ensure_ascii=False))

import requests
import codecs
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8'}
domain = 'https://tomsk.rosrabota.ru'
url = 'https://tomsk.rosrabota.ru/vac'; resp = requests.get(url, headers=headers)
jobs = []; errors = []
if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.select_one('.row:nth-of-type(2)')
    if main_div:
        section_lst = main_div.find_all('section')
        for section in section_lst:
            title = section.find('h3'); href = title.a['href']
            content = section.find('div', attrs={'class': 'description'})
            company = section.find('div', attrs={'class': 'company'})
            jobs.append({'title': title.text, 'url': domain+href,
                         'description': content, 'company': company})
    else: errors.append({'url': url, 'title': "Div doesn't exists"})
else: errors.append({'url': url, 'title': "Page don't response"})
h = codecs.open('tomskrosrab.html', 'w', 'utf-8'); h.write(str(resp.text)); h.close()
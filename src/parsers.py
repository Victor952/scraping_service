import requests
import codecs
from bs4 import BeautifulSoup as BS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8'}
def tomskrosrab(url):
    jobs = []; errors = []; domain = 'https://tomsk.rosrabota.ru'
    url = 'https://tomsk.rosrabota.ru/vac'; resp = requests.get(url, headers=headers)
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
    return jobs, errors
def tomskcareer(url):
    jobs = []; errors = []; domain = 'https://tomsk.careerist.ru'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', class_='vacSearchList')
        if main_div:
            div_lst = main_div.find_all('div', class_='list send-res-from-catalog-container')
            for div in div_lst:
                div_block = div.find('div', class_='list-block')
                title = div_block.find('p', class_='h5')
                href = title.a['href']
                description = div_block.select_one('.card-text:nth-of-type(4)')
                jobs.append({'title': title.text, 'url': href,
                             'description': description.text})
        else: errors.append({'url': url, 'title': "Div doesn't exists"})
    else: errors.append({'url': url, 'title': "Page don't response"})
    return jobs, errors
if __name__ == '__main__':
    url = 'https://tomsk.careerist.ru/jobs-python/'
    jobs, errors = tomskcareer(url)
    h = codecs.open('tomskcareer.txt', 'w', 'utf-8');
    h.write(str(jobs))
    h.close()
import requests
from bs4 import BeautifulSoup as bs

start_site = '/сканворд/слово-из-5-букв/'

all_words = []


def get_words_from(site):
    site = 'https://vfrsute.ru' + site
    html = requests.get(site).text
    soup = bs(html, 'html.parser')
    word_groups = soup.find_all('div', class_='words_group')
    for group in word_groups:
        more = group.find_all('a', class_=False)
        if more:
            get_words_from(more[0]["href"])
        else:
            word_links = group.find_all('a', class_='word-link')
            words = [link['href'].split('=')[-1].replace('/', '') for link in word_links]
            all_words.extend(words)


get_words_from(start_site)
with open('russian.txt', 'w', encoding='utf-8') as f:
    for word in all_words:
        f.write(word + '\n')

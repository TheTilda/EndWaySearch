import requests
from bs4 import BeautifulSoup

def search(query):
    #settings
    url = f'https://endway.org/search/quick-search?keywords={query}?type=post'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    responce = requests.get(url, headers={'User-Agent': user_agent})

    soup = BeautifulSoup(responce.text, 'lxml').find_all('h3', class_='contentRow-title')
    if len(soup) < 1:
        return None
    else:
        result = []
        for i in soup:
            rslt = i.find('a', href=True)
            link = 'https://endway.org/' + rslt.get('href')
            header = rslt.text
            result.append({'link' : link, 'header' : header})

        return result




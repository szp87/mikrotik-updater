import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def pobierz_wersje():
    url = "https://mikrotik.com/download.rss"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for item in soup.find_all('item'):
        tytul = item.find('title').text
        if '[stable]' in tytul:
            wersja = tytul.replace('RouterOS ', '').replace(' [stable]', '')
            return wersja

    return None
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
source = requests.get('https://1001tracklists.com', headers=headers).text

soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('div'):
    try:
        article = soup.find('div', class_='tlLink')
    except Exception as e:
        article = None
    
    # soup = soup.find('div', class_='tlLink')
    # url = soup.a['href']
    print(article)
import requests
from bs4 import BeautifulSoup

url = 'https://jupi-ter.github.io'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')
    parags = soup.find_all('p') #could be div, h titles, etc any element
    for link in links:
        print(link.get('href'))
    for parag in parags:
        print(parag.get_text())
else:
    print('Failed to retrieve the webpage')

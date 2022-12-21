import requests
from bs4 import BeautifulSoup

cidade = str(input('Informe a ciade que deseja consultar: '))
url = "https://www.google.com/search?q="+"weather"+cidade
html = requests.get(url).content  
soup = BeautifulSoup(html,'html.parser')
print(soup)
print('CLIMA')
temperatura = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
print('*' * 30)
print(f'Temperatura {temperatura}')
data = soup.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
print(f'Dia da Semana: {data}')
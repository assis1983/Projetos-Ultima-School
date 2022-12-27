import requests
from bs4 import BeautifulSoup

while True:
    cidade = str(input('Informe a ciade que deseja consultar o clima: '))
    url = "https://www.google.com/search?q="+"weather"+cidade
    html = requests.get(url).content  
    soup = BeautifulSoup(html,'html.parser')
    print('CLIMA ATUALIZADO')
    temperatura = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    print('*' * 30)
    print(f'Temperatura {temperatura}')
    data = soup.find('div', attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
    print(f'Dia da Semana: {data}')
    info = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    dados = info[5].text
    print(f'Mais informações: {dados}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if resp == 'N':
        break
print('Obrigado por utilizar o programa')
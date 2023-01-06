from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://www.gov.br/receitafederal/pt-br/assuntos/agenda-tributaria/2023/01/dia-04-01-2023")
bs = BeautifulSoup(html, 'html.parser')
linhas = bs.find_all('tr', {'class':'even'})

codigo, descricao, periodo = [], [], []
for i in linhas:
    children = i.findChildren("td")
    codigo.append(children[0].text)
    descricao.append(children[1].text)
    periodo.append(children[2].text)

df = pd.DataFrame({'CÓDIGO': codigo, 'DESCRIÇÃO': descricao, 'PERÍODO': periodo})
df.head()
print(df)

df.to_excel('dados.xlsx')

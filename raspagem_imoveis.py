from requests_html import HTMLSession
import sqlite3

conexao = sqlite3.connect('bancoimoveis')
cursor = conexao.cursor()

sessao = HTMLSession()
imoveis = []
url = 'https://www.olx.com.br/imoveis/estado-sp/regiao-de-presidente-prudente/regiao-de-adamantina-e-dracena'
resposta = sessao.get(url)
links = resposta.html.find("#ad-list li a")
for link in links:
    url_imovel = link.attrs['href']
    resposta_imovel = sessao.get(url_imovel)
    titulo = resposta_imovel.html.find('h1', first=True).text
    preco = resposta_imovel.html.find('h2')[0].text
    imoveis.append({
        'url': url_imovel,
        'titulo': titulo,
        'preco': preco
    })
    
valores = []
sql = 'insert into imoveis (url, titulo, preco) values (?,?,?)'
for imovel in imoveis:
    valores = [imovel['url'], imovel['titulo'], imovel['preco']]
    cursor.execute(sql, valores)
conexao.commit()
conexao.cursor()
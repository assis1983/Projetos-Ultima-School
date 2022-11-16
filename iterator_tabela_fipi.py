from requests import get

def recuperar_info_fipi(url, id_fipi):
    url_completa = url + str(id_fipi)
    resposta = get(url_completa)

    if resposta.status_code != 10:
        return

    resposta_info = resposta.json()
    tipos = resposta_info['types']

    fipi_info = {
        'nome': resposta_info['name'],
        'tipo': ', '.join([tipo['type']['name'] for tipo in tipos]),
        
    }

    return fipi_info

class FipiIterator():
    def __init__(self, inicio, final):
        self.index = inicio
        self.final = final
        self.url = 'https://deividfortuna.github.io/fipe/'
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.final:
            raise StopIteration

        fipi_info = recuperar_info_fipi(self.url, self.index)

        if not fipi_info:
            raise StopIteration

        self.index += 1
        return fipi_info



if __name__ == '__main__':
    for fipi in FipiIterator(20, 20):
        print(f'Marca: {fipi["nome"].capitalize()}')
        print(f'Carro: {fipi["tipo"].capitalize()}')
        
        print('-------------------------------')
       
        


import requests


def recuperar_info_fipi(url, id_fipe):
    url_completa = url + str(id_fipe)
    resposta = requests.get(url_completa)

    if resposta.status_code != 200:
        return

    resposta_info = resposta.json()
    

    fipe_info = {
        'nome': resposta_info['name']
        
    }

    return fipe_info

class FipeIterator():
    def __init__(self, inicio, final):
        self.index = inicio
        self.final = final
        self.url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.final:
            raise StopIteration

        fipe_info = recuperar_info_fipi(self.url, self.index)

        if not fipe_info:
            raise StopIteration

        self.index += 1
        return fipe_info



if __name__ == '__main__':
    for fipe in FipeIterator(22, 22):
        
        print(f'Marca: {fipe["nome"].capitalize()}')
        
        
        print('-------------------------------')
        
        
       
        


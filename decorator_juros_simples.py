
def imprimir_dados(funcao):
    def wrapper():
        print('\nDigite os dados para calculo do juros simples.')               
        funcao()
        print('Resultados apresentados.')
    return wrapper
    
@imprimir_dados        
def juros_simples():
    capital = float(input('\nCapiatal: '))
    taxa = float(input('Taxa: '))
    tempo = float(input('Taxa: '))
    resposta = capital * (taxa / 100) * tempo
    print('*'*30)
    print(f'Capital investido: {capital} reais')
    print(f'Taxa de juros: {taxa}%')
    print(f'Tempo: {tempo} meses')
    print('*'*30)

    print(f'O valor calculado é de: {resposta}')
    

juros_simples()


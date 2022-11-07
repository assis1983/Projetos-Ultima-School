import time

def cont():
    
    print('Contagem de 1 até 10 de 1 em 1!')
    for i in range(1, 11):
        time.sleep(0.3)
        print(i)

    print('\nContagem de 10 até 1 de 1 em 1!')
    for i in range(10, 0, -1):
        time.sleep(0.3)
        print(i)
cont ()
resposta = ' '
while True:
    inicio = int(input('\nDigite o valor para Início da Contagem: '))
    
    fim = int(input('\nDIgite o Fim da Contagem: '))
  
    passo = int(input('\nDigite o Passo da Contagem: '))
       
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio > fim:
        fim -= passo
        for i in range(inicio, fim, -passo):
            time.sleep(0.3)
            print(i)
    if inicio < fim:
        fim += passo
        for i in range(inicio, fim, passo):
            time.sleep(0.3)
            print(i)
    try:
        resposta = str(input('Deseja continuar? SIM/NÃO: ')).strip().upper()[0]
    except IndexError:
        print('Valor inválido')    
    if resposta == 'N':
        break

print('OBRIGADO')


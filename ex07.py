titulo = 'EXERCÍCIO NUMERO 07'
print(titulo.center(100, '*'))

print('1 - PAGAMENTO À VISTA EM DINHIERO, RECEBE 15% DE DESCONTO')
print('2 - PAGAMENTO À VISTA NO CARTÃO DE CRÉDITO, RECEBE 10% DE DESCONTO')
print('3 - PAGAMENTO EM DUAS VEZES, PREÇO NORMAL DO PRODUTO')
print('4 - PAGAMENTO EM MAIS DE DUAS VEZES, PREÇO NORMAL DO PRODUTO,MAIS JUROS DE 10%')
print(100 * '*')
while True:
    try:
        valor_produto = float(input('DIGITE O VALOR DO PRODUTO: '))
    except ValueError:
        print('VALOR INVÁLIDO')
    try:
        forma_pagamento = int(input('Digite a forma de pagamento conforme opções acima: '))
    except ValueError:
        print('VALOR INVÁLIDO')
    if forma_pagamento == 1:
        valor_final = valor_produto - (valor_produto * 0.15)
        print(f'Valor Final para pagamento à vista no dinheiro R$ {valor_final:.2f}.')
    
    elif forma_pagamento == 2:
        valor_final = valor_produto - (valor_produto * 0.10)
        print(f'Valor Final para pagamento à vista no cartão de crédito R$ {valor_final:.2f}.')
    
    elif forma_pagamento == 3:
        valor_final = valor_produto
        print(f'Valor Final para pagamento em duas vezes R$ {valor_final:.2f}.')
        
    elif forma_pagamento == 4:
        valor_final = valor_produto + (valor_produto * 0.10)
        print(f'Valor Final para pagamento em mais de duas vezes R$ {valor_final:.2f}.')
    
    sair = ' '
    while sair not in 'SN':
        try:
            sair =str(input('DESEJA CONTINUAR? SIM/NÃO: ')).strip().upper()[0]
        except IndexError:
            print('VALOR INVÁLIDO, DIGITE NOVAMENTE!')
    if sair == 'N':
        break
    
print('OBRIGADO POR UTILIZAR O PROGRAMA')

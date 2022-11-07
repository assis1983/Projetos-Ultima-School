from datetime import datetime
from time import sleep
from unittest.loader import VALID_MODULE_NAME

titulo = 'CAIXA BANCO DOS BANCOS' 
print(titulo.center(100,'*'))

class CaixaEletronico:
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome
        

    def sacar(self,valor_saque):
        valor = valor_saque
        resto = -1
        notas_entregues = []
        
        for valor_nota in self.notas:
            qtd_notas = valor // valor_nota
            resto = valor % valor_nota
            valor = resto
            
            if qtd_notas > 0:
                notas_entregues.append(f'\n{qtd_notas} NOTAS DE R$ {valor_nota},00 REAIS')

              
        if resto == 0:
            self.imprimir_resultado(notas_entregues)
            sleep(1)
            print('SAQUE REALIZADO COM SUCESSO')
            print(100 * '*')
        else:
            print(f'NÃO É POSSÍVEL SACAR O VALOR DE  R$ {valor_saque},00 REAIS')
            print(100 * '*')
        sleep(1)
        opc = ''
        while True:
            try:
                opc = str(input('DESEJA REALIZAR OUTRA OPERAÇÃO (SIM/NÃO): ')).strip().upper()[0]
            except IndexError:
                print('VALOR INVÁLIDO')
                print(100 * '*')
            while opc not in 'SN':
                opc = str(input('VALOR INVÁLIDO, DIGITE SIM PARA CONTINUAR/NÃO PARA FINALIZAR: ')).strip().upper()[0]
                print(100 * '*')
                print(100 * '*')
            if opc == 'S':
                valor = int(input('INFORME UM VALOR PARA SAQUE: '))
                print(100 * '*')
                caixa_eletronico.sacar(valor)
            if opc == 'N':
                break
         
        self.encerrar_atendimento()
     
    def encerrar_atendimento(self):
        hora = datetime.today().hour
                       
        sleep(2)
        print(f'OBRIGADO POR UTILIZAR O {self.nome_banco}')
        
        if hora > 0 and hora < 12:
            print('TENHA UM BOM DIA!')

        elif hora > 12 and hora < 18:
            print('TENHA UMA BOA TARDE!')
        
        elif hora > 18 and hora < 24:
            print('TENHA UMA BOA NOITE!')

        
    def imprimir_resultado(self, notas_entregues):
        print('  '.join(notas_entregues))


if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('BANCO DOS BANCOS')
    valor = 0
    try:
        valor = int(input('INFORME UM VALOR PARA SAQUE: '))
    except ValueError:
        print('VALOR INVÁLIDO!')
    caixa_eletronico.sacar(valor)



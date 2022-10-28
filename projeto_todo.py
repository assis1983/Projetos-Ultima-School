from asyncio.windows_events import NULL
from genericpath import exists
from inspect import trace
import sqlite3
from sys import breakpointhook, float_repr_style
from time import sleep
from xmlrpc.client import boolean
from datetime import datetime
titulo = 'PROJETO MÓDULO 2'
print(titulo.center (100, '*'))

conexao = sqlite3.connect('bancotodo.sqlite3')
cursor = conexao.cursor()

while True:
    print('MENU DE OPÇÕES')
    print('''
    DIGITE 1 - PARA CADASTRAR TAREFAS
    DIGITE 2 - PARA ATUALIZAR TAREFAS
    DIGITE 3 - PARA EXCLUIR TAREFAS
    DIGITE 4 - PARA LISTAR TAREFAS
    DIGITE 5 - PARA SAIR
    ''')
    menu = ' '
    coluna = 0
    a = [1,2,3,4]
    while menu == ' ':
        try:
            print(100 * '*')
            menu = int(input('DIGITE UMA OPÇÃO DO MENU ACIMA: '))
        except ValueError:
            print('VALOR INVÁLIDO, DIGITE NOVAMENTE! ')
    
    if menu == 1:
        print(f'DIGITE AS INFORMAÇÕES PARA REALIZAR O CADASTRO DE TAREFAS! ')
        print(100 * '_')
        tarefa = str(input('INFORME A TAREFA A SER REALIZADA: '))
        print(100 * '_')
        data = input('INFORME A DATA PARA REALIZAR A TAREFA: ')
        print(100 * '_')
        horario = input('INFORME O HORÁRIO PARA REALIZAR A TAREFA: ')
        cursor.execute('INSERT INTO todo (tarefas, data, horario) VALUES (?,?,?)', (tarefa, data, horario))
        print('CADASTRANDO TAREFA...')
        sleep(2)
        print(100 * '_')
        print('TAREFA CADASTRADA COM SUCESSO')
        print(100 * '_')

    elif menu == 2:
        cursor.execute('SELECT * FROM todo;')
        print('ID   TAREFA      DATA          HORÁRIO')
        for i in cursor.fetchall():
            print(f'\n{i}')
        saida = 0
        while (saida == 0):
            try:
                print(100 * '_')
                id_tarefas = input('INFORME O ID DA TAREFA QUE DESEJA ATUALIZAR: ')
            except ValueError:
                print(100 * '_')
                print('VALOR INVÁLIDO!')
            listaid = [id_tarefas]
            nova = 'SELECT count (*) FROM todo WHERE id = ?'
            cursor.execute(nova,listaid)
            sql = cursor.fetchone()[0]
            if sql == 0:
                print(100 * '_')
                print('ID INVÁLIDO, INFORME UM ID VÁLIDO!')
            else:
                saida = 1
        
        while coluna != a:  
            try:
                coluna = int(input('INFORME O NÚMERO DA COLUNA QUE DESEJA ATUALIZAR:\n 1 - Tarefa\n 2 - Nova Data\n 3 - Novo Horário\n 4 - Concluir Tarefa\n 5 - Sair e Atualizar\n'))
            except ValueError:
                print('VALOR INVÁLIDO!')   
            if coluna == 1:
                nova_tarefa = ''
                print(100 * '*')
                while nova_tarefa == '':
                    nova_tarefa = input('INFORME A NOVA TAREFA: ')
                    tarefa = [nova_tarefa, id_tarefas]
                    sql_update = 'UPDATE todo SET tarefas = ? WHERE id = ?'
                    cursor.execute(sql_update, tarefa)
                            
            elif coluna == 2:
                nova_data = ''
                print(100 * '*')
                while nova_data == '':
                    nova_data = input('INFORME A NOVA DATA: ')
                    data = [nova_data, id_tarefas]
                    sql_update = 'UPDATE todo SET data = ? WHERE id = ?'
                    cursor.execute(sql_update, data)   
                                        
            elif coluna == 3:
                novo_horario = ''
                print(100 * '_')
                while novo_horario == '':
                    novo_horario = input('INFORME O NOVO HORÁRIO: ')
                    horario = [novo_horario, id_tarefas]
                    sql_update = 'UPDATE todo SET horario = ? WHERE id = ?'
                    cursor.execute(sql_update, horario)
                    
            elif coluna == 4:
                concluir = ' '  
                while concluir not in 'SN':
                    print(100 * '_')
                    try:
                        concluir = str(input('DIGITE SIM PARA CONCLUÍDO E NÃO PARA PENDENTE: ')).strip().upper()[0]
                    except IndexError:
                        print('VALOR INVÁLIDO!')
                if concluir == 'S':
                    concluir  = 'SIM'
                    conclusao = [concluir, id_tarefas]
                    sql_update = 'UPDATE todo SET situacao = ? WHERE id = ?'
                    cursor.execute(sql_update, conclusao)
                elif concluir == 'N':
                    concluir = 'NÃO'
                    conclusao = [concluir, id_tarefas]
                    sql_update = 'UPDATE todo SET situacao = ? WHERE id = ?'
                    cursor.execute(sql_update, conclusao)
            elif coluna == 5:
                break       
        print(100 * '_')  
        print('ATUALIZANDO TAREFAS...')
        sleep(2)
        print(100 * '_')
        print('TAREFA ATUALIZADA COM SUCESSO!') 
                
    elif menu == 3:
        cursor.execute('SELECT * FROM todo;')
        for i in cursor.fetchall():
            print(f'\n{i}')
        saida = 0
        
        while (saida == 0):
            try:
                print(100 * '_')
                id_tarefas = input('INFORME O ID DA TAREFA QUE DESEJA EXCLUIR: ')
            except ValueError:
                print(100 * '_')
                print('VALOR INVÁLIDO!')
            listaid = [id_tarefas]
            nova = 'SELECT count (*) FROM todo WHERE id = ?'
            cursor.execute(nova,listaid)
            sql = cursor.fetchone()[0]
            if sql == 0:
                print(100 * '_')
                print('ID INVÁLIDO, INFORME UM ID VÁLIDO!')
            else:
                saida = 1
        decisao = ' '
        try:
            decisao = str(input('TEM CERTEZA QUE DESEJA EXCLUIR (SIM/NÃO): ')).strip().upper()[0]
        except IndexError:
            print('VALOR INVÁLIDO, CADASTRO NÃO EXCLUIDO!')
        
        if decisao == 'S':
            cursor.execute('DELETE FROM todo WHERE id = ?', (id_tarefas,))
            conexao.commit()
            print('EXCLUINDO CADASTRO...')
            sleep(2)
            print(100 * '_')
            print('CADASTRO EXCLUIDO COM SUCESSO!')
        else:
            print(100 * '_')
            print('CADASTRO MANTIDO!')
            print(100 * '_')
        
    elif menu == 4:
        print(100 * '*')
        print('DATAS COM ATIVIDADES AGENDADAS!')
        cursor.execute('SELECT id, data FROM todo')
        for i in cursor.fetchall():
            print('ID       DATA')
            print(i)
        saida = 0
        while (saida == 0):
            try:
                id_tarefas = input('INFORME O ID DA DATA QUE DESEJA REALIZAR A CONSULTA DE TAREFAS AGENDADAS: ')
            except ValueError:
                print('VALOR INVÁLIDO!')
            listaid = [id_tarefas]
            nova = 'SELECT count (*) FROM todo WHERE id = ?'
            cursor.execute(nova,listaid)
            sql = cursor.fetchone()[0]
            if sql == 0:
                print('ID INVÁLIDO, INFORME UM ID VÁLIDO!')
            else:
                saida = 1    
        cursor.execute('SELECT tarefas, horario FROM todo WHERE id = ?',(id_tarefas,))
        for i in cursor.fetchall():
            print(100 * '_')
            print('  TAREFA    HORÁRIO')
            print(f'\n{i}')
            print(100 * '_')
    
    elif menu == 5:
        opcao = ' '
        while opcao not in 'SN':
            try:
                print(100 * '_')
                opcao = str(input('DESEJA CONTINUAR (SIM/NÃO): ')).strip().upper()[0]
            except IndexError:
                print(100 * '_')
                print('VALOR INVÁLIDO! DIGITE SIM OU NÃO!')
        if opcao == 'N':
            hora = datetime.today().hour    
            if hora > 0 and hora < 12:
                print('TENHA UM BOM DIA!')
            elif hora > 12 and hora < 18:
                print('TENHA UMA BOA TARDE!')
            elif hora > 18 and hora < 24:
                print('TENHA UMA BOA NOITE!')
            break
sleep(2)
print('OBRIGADO POR UTILIZAR O PROGRAMA') 
conexao.commit()
conexao.close()

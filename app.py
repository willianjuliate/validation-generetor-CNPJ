import os
import sys

from valida_cnpj import novo_cnpj_re, formata_cpf
from time import sleep
from gera_cnpj import new_cnpj

while True:
    # print("\x1b[2J\x1b[1;1H")
    print('### ESCOLHA UMA DAS OPÇÕES ABAIXO.')
    print('1 - Validar um CNPJ')
    print('2 - Gerar um CNPJ valido')
    print('3 - Sair')
    opc = input('..: ')

    if opc == '1':
        value = formata_cpf(input('INFORME UM CNPJ.: '))
        novo_cnpj = novo_cnpj_re(value, value[:12])

        if novo_cnpj:
            print(f'\nCNPJ VALIDO!\n')
        else:
            print(f'\nCNPJ INVALIDO!\n')
        continue
    elif opc == '2':
        print(f'Gerando CNPJ...')
        sleep(1.5)
        print(f'\nCNPJ.: {new_cnpj()}\n')
        continue
    elif opc == '3':
        break

    else:
        print('\nOPÇÃO INVALIDA...\n')
        continue


if sys.platform == 'Win32':
    os.system('pause')

"""
Fazer um programa que peça ao usuário para digitar um número inteiro,
informar se este número é par ou ímpar, e caso o usuário não digite
um número inteiro, informar que não é um número inteiro.
"""

# 1° solução
 
import re

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

num = input('Digite um número inteiro: ')

if is_int(num):
    num = int(num)

    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
else:
    print('Por favor insira um número inteiro válido.')

# 2° solução

num = input('Digite um número inteiro: ')

try:
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
except:
    print(f'Não é possível converter {num} para inteiro.')

"""
Fazer um programa que pergunte a hora ao usuário e baseando-se no horário
descrito, exiba a saudação apropriada. Ex: input(6) -> bom dia!
"""

# 1° solução

import re

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

hora = input('Informe a hora com um número inteiro: ')

if is_int(hora):
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Booom diaaa!')
    elif hora >= 12 and hora <= 17:
        print('Boooa taaarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite. Zzzzz')
    else:
        print('Horário fora dos parâmetros!')
else:
    print(f'Não foi possível converter o {hora} em inteiro.')

# 2° solução

hora = input('Informe a hora com um número inteiro: ')

try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Booom diaaa!')
    elif hora >= 12 and hora <= 17:
        print('Boooa taaarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite. Zzzzz')
    else:
        print('Horário fora dos parâmetros!')
except:
    print(f'Não é possível converter {hora} para inteiro.')

"""
Fazer um programa que peça o primeiro nome do usuário, e se este nome conter 4
letras ou menos, informar 'Seu nome é curto'. Se conter entre 5 e 6 letras
informar 'Seu nome é normal' e se conter mais de 6 letras, informar 'Seu nome
é muito grande'.
"""

primeiro_nome = input('Informe seu primeiro nome: ')

if primeiro_nome.isalpha():
    qtd_letras = len(primeiro_nome)

    if qtd_letras <= 4:
        print('Seu primeiro nome é curto.')
    elif qtd_letras >= 5 and qtd_letras <= 6:
        print('Seu primeiro nome é normal.')
    else:
        print('Seu primeiro nome é muito grande.')
else:
    print(f'O nome {primeiro_nome} possui caracteres ou espaços não válidos.')

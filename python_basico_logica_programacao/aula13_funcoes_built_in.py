"""
https://docs.python.org/3/library/stdtypes.html#built-in-types

Funções Built-in são funções nativas do python, ou seja, integradas (internas).
Existem diversas funções built-in para diferentes tipos de dados.
Também é possível personalizar essas funções.
"""

# Imagine que queremos fazer uma calculadora simples que só realiza soma.
# 1° Solução

num1 = input('Digite o 1° número: ')
num2 = input('Digite o 2° número: ')

if num1.isnumeric() and num2.isnumeric(): # função bastante limitada
    print(int(num1) + int(num2))
else:
    print('Não foi possível converter os valores.')

# 2° Solução

try:
    num1 = input('Digite o 1° número: ')
    num2 = input('Digite o 2° número: ')

    print(int(num1) + int(num2))
except:
    print('Não foi possível converter os valores.')

# 3° Solução

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digite o 1° número: ')
num2 = input('Digite o 2° número: ')

if is_number(num1) and is_number(num2): # função personalizada
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
else:
    print('Não foi possível converter os valores.')
 
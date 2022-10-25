"""
Formatar valores utilizando os modificadores da função format e f strings

:s ---> Texto (strings)
:d ---> Inteiros (int)
:f ---> Números de ponto flutuante (float)
:.(número)f ---> Quantidade de casas decimais (float)
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

Observações

> esquerda 
< direita
^ centro 

https://docs.python.org/3/library/stdtypes.html#string-methods
"""

num_1 = 5
num_2 = 12

# por padrão, número quebrado com muitas casas decimais
div = num_1 / num_2
print('\nResultado (sem formatação): ', div) 

# formatando o resultado da divisão utilizando a função format
print('Resultado (com formatação usando format): {:.3f}'.format(div))

# formatando o resultado da divisão utilizando f strings
print(f'Resultado (com formatação usando f strings): {div:.3f}')

num_3 = 400

# preenchendo o valores com algum elemento, especificando a quantidade e local
# OBS: a quantidade de elementos subtrai a quantidade do valor

# ex: preenchendo o valor 400 com cerquilhas, de modo que tenha 7 casas
# e alinhamento ao centro
print(f'Com F Strings: {num_3:#^7}')
print('Com Format: {:#^7}'.format(num_3))

# ex: preenchendo o valor 400 com zeros à direita, de modo que tenha 7 casas 
print(f'Com F Strings: {num_3:0>7}')
print('Com Format: {:0>7}'.format(num_3))

# ex: preenchendo o valor 400 com cifrões à esquerda, de modo que tenha 7 casas
print(f'Com F Strings: {num_3:$<7}')
print('Com Format: {:$<7}'.format(num_3))

# combinando valores e arredondamentos
print(f'Com F Strings: {num_3:$<7.1f}')
print('Com Format: {:$<7.1f}'.format(num_3))

# também funciona com texto (strings)
nome = 'willian junior'

print(f'Com F Strings: {nome:_^20}')
print('Com Format: {:_^20}'.format(nome))

# as strings possuem diversos métodos embutidos pela classe String
print(nome.capitalize())
print(nome.upper())
print(nome.ljust(20, '_'))

# entre muitos outros...
print()

"""
Operadores aritméticos 

adição (+)
subtração (-)
multiplicação (*)
divisão (/)
divisão inteira (//)
exponenciação (**)
resto da divisão / módulo  (%)

Precedência básica:

1#  ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são
realizadas primeiro.

2#  ** - Depois vem a exponenciação.

3#  * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo.

4#  +  - - Por fim, soma e subtração.

OBS: Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

OBS: Existem outros operadores, e cada um possui a sua ordem de precedência:

https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

print(10 + 7)
print(10 - 7)
print(10 * 7)
print(10 / 7)
print(10 // 7)
print(10 ** 7)
print(10 % 7)

# Situações em que o operador aritmético emprega outra função

print(10 * '7')
print('10' + '7')

# os '( )'  parênteses servem para alterar a precedência dos operadores

print(10 + 7 * 10)
print((10 + 7) * 10)

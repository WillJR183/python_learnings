"""
Na maioria das linguagens de programação, quando precisamos ou desejamos inverter o
valor entre duas variaveis, fazemos o uso de uma variavel auxiliar para armazenar
temporariamente o valor de uma variavel a fim de possibilitar a troca. Essa solução
é valida, porém em Python esse processo pode ser muito mais simples e de outra forma.
"""

# 1° solução : tradicional

x = 6
y = 4

z = x
x = y
y = z

print()
print(f'X = {x} | Y = {y}')

# 2° solução: pythonica

x, y = y, x

print(f'X = {x} | Y = {y}')

"""

Tipos de dados

str (string): "exemplo", 'outro exemplo'
int (inteiro): 10, -10, 9999 ... etc
float (real / ponto flutuante): 3.14, 0.762, -23.44, 0.0 .. etc
bool (booleano / lógico): True ou False, os tipos booleanos possuem
comportamentos diferentes dos outros dados, por exemplo, uma lista vazia
é dada como False, assim como outros tipos de dados vazios ou nulos.
type casting (converter tipos de dados): dependendo do tipo de dado
não é possível fazer a conversão. ex: string ('Will') -> int , isso
gera um erro.
"""

print('Willian Jr', type('Willian Jr'))
print('"777"', type('777'))
print(7, type(7))
print(77.77, type(77.77))
print(7 == 7 , type(7 == 7))
print('W' == 'w', type('W'=='w'))
print('777', type('777'), type(int(777)))  # type casting
print(bool([])) # lista vazia

# string: nome
print('Willian Junior', type('Willian Junior'))
# int: idade
print(22, type(22))
# float: altura
print(1.83, type(1.83))
# bool: maior de idade?
print(22 >= 18, type(22 >= 18))

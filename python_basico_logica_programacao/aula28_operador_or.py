"""
Expressão condicional com operador or em Python
"""

# Exemplo hipotético sem usar o operador or

print()
entrada = input('Digite algo: ')

if entrada:
    print(f'\n{entrada}\n')
else:
    print('\nNada foi digitado.\n')


# Exemplo usando o operador or

entrada = input('Digite algo: ')
print()
print(entrada or 'Nada foi digitado.')
print()

# Mais um exemplo

A = 0  # 0 possui um valor lógico igual a False
B = None  # o tipo de dado None atribui um valor nulo ou vazio, então é apenas diferente de True
C = False  
D = []  # uma lista vazia possui um valor lógico False
E = {}  # assim como um dicionário vazio
F = 7  # um valor atribuido, isto posto, True

# o valor atribuido a variavel vai ser o primeiro que seja igual a True

var = A or B or C or D or E or F
print(var)

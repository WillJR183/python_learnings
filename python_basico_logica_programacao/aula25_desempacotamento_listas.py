"""
Desempacotamento de listas em Python
Basicamente consiste em atribuir valores de uma lista em variáveis
Podendo especificar na ordem os valores desejados e tratar o restante da lista
"""

frutas = ['abacaxi', 'acerola', 'ameixa', 'abacate', 'etc']
objetos = ['lapis', 'caneta']

# exemplo atribuindo todos os valores da lista a variaveis

fruta_1, fruta_2, fruta_3, fruta_4, fruta_5 = frutas

print()
print(fruta_1, fruta_2, fruta_3, fruta_4, fruta_5)

# E quando queremos apenas alguns valores da lista?
# podemos utilizar *nome_variavel para armazenar o restante dos valores que não serão usados

fruta_1, fruta_2, *resto = frutas

print()
print(fruta_1, fruta_2)
print(*resto)
print()

# E para atribuir a uma variavel o ultimo elemento da lista?
# basta usar *nome_variavel primeiro e depois obter o ultimo elemento

*primeiros, ultima_fruta = frutas

print(*primeiros)
print(ultima_fruta)

# E caso os valores que não serão usados da lista sejam descartaveis?
# podemos usar *_ para varios valores ou simplesmente _ para um valor

fruta_1, *_ = frutas

print()
print(fruta_1)

fruta_1, fruta_2, fruta_3, fruta_4, _ = frutas

print()
print(fruta_1, fruta_4)

"""
Funções Split, Join e Enumerate em Python

split : serve para dividir uma string -> str
join : serve para juntar uma lista -> str (gera uma string)
enumerate : serve para enumerar elementos da lista -> list ou objetos iteráveis
"""


# O método split consegue dividir uma cadeia de caracteres (strings) com base em um
# caractere, como por exemplo, espaços ou ',' etc. 

print()
frase = 'Hoje é segunda feira. Amanhã é terça feira.'
lista = frase.split(' ')
print(lista)

print()

# iterando sobre a lista e printando cada elemento

for item in lista:
    print(item)

print()


# iterando sobre a lista e contando quantas vezes cada elemento apareceu nela

for item in lista:
    print(f'A palavra "{item}" apareceu {lista.count(item)}x na frase.')

print()

# itera sobre a lista, verifica e guarda o elemento que mais apareceu nela
# nesse caso as variáveis 'palavra' e 'contagem' são auxiliares

palavra = ''
contagem = 0
for item in lista:
    qtd_vezes = lista.count(item)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = item

print(f'A palavra "{palavra}" apareceu {contagem}x na frase.')

print()

# O método join é usado para juntar uma lista com base em um caractere e gera uma string

frase_juntada = ' '.join(lista)
print(frase_juntada)


# O recurso enumerate possibilita enumerar uma lista, dessa forma cada item da lista
# tem um identificador associado a ele. OBS: enumerate retorna tuplas

for enum, item in enumerate(lista):
    print(enum, item)


# listas dentro de uma lista. É possível ter várias listas encadeadas

lista_exemplo = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

print()

# iterando sobre a lista e acessando as listas

for item in lista_exemplo:
    print(item)

print()

# iterando sobre a lista e acessando os valores das listas

for item in lista_exemplo:
    print(item[0], item[1])

print()

# simulando o comportamento do enumerate com indices em uma lista
# nesse caso o retorno é também uma lista

lista_exemplo = [
    [1, 'Amora'],
    [2, 'Abacaxi'],
    [3, 'Abacate'],
    [4, 'Ameixa'],
    [5, 'Acerola'],
]

for indice, item in lista_exemplo:
    print(indice, item)

print()

# exemplo de desempacotamento de lista em Python

notas = [6, 7.5, 9]
n1, n2, n3 = notas
print(n2)

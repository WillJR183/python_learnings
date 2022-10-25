"""
Sanando dúvidas e aprofundando conceitos a respeito do enumerate em Python

OBS: O enumerate basicamente enumera os elementos de uma lista ou objeto iterável
"""

lista_de_nomes = [
#       0        1          2 
    ['Will', 'Guilherme', 'Luis'],  # 0
    ['Joao', 'Erik', 'Italo'],  # 1
    ['Jose', 'Eduardo', 'Douglas']  # 2
]

# acessando um elemento da lista de listas

print()
print(lista_de_nomes[1][1])
print()

# convertendo a lista em um objeto enumerate
lista_enumerada = enumerate(lista_de_nomes)
print(lista_enumerada)  # objeto

# transformando o objeto enumerate em uma lista
lista_enumerada = list(lista_enumerada)  # casting 
print(lista_enumerada)  # exibe a lista de tuplas, pois o enumerate gera tuplas

"""
    Saída do exemplo acima

-->      0  |            1
    [       |
-->            0         1          2      
        (0, ['Will', 'Guilherme', 'Luis']),  --> 0
               0        1       2
        (1, ['Joao', 'Erik', 'Italo']),  --> 1
                0       1          2
        (2, ['Jose', 'Eduardo', 'Douglas'])  --> 2
    ]

"""

# acessando o indice da tupla
print()
print(lista_enumerada[1])

# acessando os elementos da lista de tuplas através do indice e posição
print() 
print(lista_enumerada[2][1])

# acessando um elemento da lista de tuplas
print() 
print(lista_enumerada[2][1][0])
print()

# aplicando um comportamento diferente ao enumerate para exemplificar que 
# ele não cria indices, apenas enumera os elementos com base nos parametros

for enum, item in enumerate(lista_de_nomes, 7):  # faz com que enumere os elementos começando com 7
    print(enum, item)

print()

# Mesmo exemplo de cima porém usando também o desempacotamento de listas

for item in enumerate(lista_de_nomes, 7):  # faz com que enumere os elementos começando com 7
    item_enum, item_lista = item
    nome_1, *_ = item_lista
    print(nome_1)

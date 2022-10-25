"""
Listas em Python

A lista é um tipo de dado que pode conter vários valores e com diferentes tipos de dados,
diferentemente da variável que só pode conter um valor de um tipo de dado.  

sintaxe:

nome_da_lista = [ valor_1, valor_2, ... ]

A lista possui índices, e é através dele que acessamos cada valor da lista. Assim como
em outros objetos iteráveis, o índice pode ser positivo e negativo. E o indice -1 sempre
busca o ultimo elemento da lista.

veja:

indices positivos          0          1          2           3
uma_lista_de_frutas = ['morango', 'abacaxi' ,'maracujá', 'laranja']
indices negativos         -4         -3         -2          -1

As listas também suportam o fatiamento, assim como as strings

veja:

lista = lista[0:2:1] # inicio, fim, passo

As listas possuem diversos métodos built-in:
-append: adiciona ao final da lista
-insert: adiciona em qualquer posição da lista
-pop: remove o último elemento da lista
-del: remove um elemento ou uma fatia de elementos da lista
-clear: limpa a lista
-extend: adiciona elementos de outra lista ao final ou adiciona novos elementos
etc ...

-max: retorna o maior elemento da lista
-min: retorna o menor .................

É possível utilizar a função range para criar sequências e transforma-las em listas

veja:

lista = list(range(1,100))
"""

print()

frutas = ['morango', 'abacaxi' ,'maracujá', 'laranja']  # lista só de strings
print(frutas)
print(frutas[::-1])  # inverte a lista
print(frutas[-1])  # acessa o último elemento da lista

coisas = ['morango', True, False, 7, 3.14, 'w']  # lista com diferentes tipos de dados
print(coisas)

# modificando um valor de uma lista
coisas[-1] = 'z'
print(coisas)

# fatiando(slice) listas
lista_fatiada = coisas[0:2:1]
print(lista_fatiada)

print()

# usando alguns métodos da lista
print('Listas originais')
lista_01 = [1, 2, 3, 4]
lista_02 = [5, 6, 7]

print(lista_01)
print(lista_02)

print('Usando as Funções')

lista_03 = lista_01 + lista_02  # concatena os valores das listas em uma nova lista
print(lista_03)

# extend
lista_01.extend(lista_02)  # nesse caso, causa o mesmo efeito do exemplo acima
print(lista_01)

lista_01.extend([8, 9])
print(lista_01)

# Geralmente quando queremos adicionar elementos a uma lista utilizamos o append
# pois na maioria das vezes precisamos adicionar elementos ao final de uma lista
lista_02.append(1)
print(lista_02)

# com o insert podemos adicionar elementos em qualquer posição (indice) de uma lista
lista_02.insert(2, 77) # adiciona no indice 2 o valor 77
print(lista_02)

lista_01.pop()  # remove o ultimo elemento da lista
print(lista_01)

# com o del podemos remover fatias de elementos da lista
del(lista_01[0:3])
print(lista_01)

# max retorna o maior elemento da lista
# min retorna o menor ....
print(max(lista_01))
print(min(lista_01))

lista_4 = list(range(0,21,2))  # cria uma lista de 0 a 20 pulando de 2 em 2
print(lista_4)

# utilizando o for para iterar sobre uma lista
for item in lista_4:
    print(item)

# iterando sobre a lista e somando os valores
soma = 0
for item in lista_4:
    soma += item
print(soma)

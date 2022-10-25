"""
for o while

0  10
1  9
2  8
3  7
4  6
5  5
6  4
7  3
8  2
"""

contador_crescente = 0
contador_decrescente = 10

while contador_crescente < 9 and contador_decrescente > 1:
    print(f'{contador_crescente} {contador_decrescente}')
    contador_crescente += 1
    contador_decrescente -= 1

print()


# 1° solução usando for

contador = 10

for cc, cd in enumerate(range(0, 9)):
    print(f'{cd} {contador}')
    contador -= 1

print()

# 2° solução usando for

contador = range(0 , 9)
contador_desc = 10
for i in contador:
    print(f'{i} {contador_desc}')
    contador_desc -= 1

print()

# 3° solução usando for
# ultimo parametro no range define uma sequencia descrecente

for crescente, decrescente in enumerate(range(10, 1, -1)):  
    print(crescente, decrescente)

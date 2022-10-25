"""
Diferentemente do laço while em que precisamos manter um loop sobre algo que não
sabemos precisamente quando vai terminar, o for já é voltado para situações
precisas, ou seja, finitas.

For in em Python

sintaxe:

for alvo in sequencia:
    implementações... (ações)

É possível simular o for com contador utilizando o elemento enumerate

Também é possível utilizar em conjunto com o for a função built-in range
A função range basicamente cria uma sequência de inteiros
range(start, stop, step)

Também é possível utilizar com for os elementos continue e break
continue: pula para a próxima execução do laço
break: para e termina o laço
"""

# iterando sobre strings
# iterar strings com for faz muito mais sentido do que while
texto = 'minha mãe é uma peça.'
for letra in texto:
    print(letra)

print()

# for com enumarate
for contador, letra in enumerate(texto):
    print(contador, letra)

print()

# for com range
for i in range(1, 100, 2):
    print(i)

print()

# fazendo a cópia de um texto com for
copia = ''
for letra in texto:
    copia += letra

print(copia)

print()

# fazendo uma cópia e modificando a string

copia = ''
for letra in texto:
    if letra == ' ':
        copia += '_'
    else:
        copia += letra

print(copia)

print()

# for com continue

copia = ''
for letra in texto:
    if letra == ' ':
        continue  # vai pular os espaços
    else:
        copia += letra

print(copia)

print()

# for com break

copia = ''
for letra in texto:
    if letra == 'p':
        break  # termina o laço quando encontrar a letra p
    else:
        copia += letra

print(copia)

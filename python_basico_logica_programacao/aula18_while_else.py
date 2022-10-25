"""
A estrutura de repetição while na linguagem Python, ao contrário da maioria,
dispoẽ o uso do else. O emprego do else serve para executar um bloco
de código que só é executado quando a condição do while for falsa
(ou deixar de ser verdadeira).

Além disso temos 2 elementos em laços de repetição: o contador e o acumulador.

Contador: variável utilizada para controlar o fluxo do laço, simplesmente
possui um lógica de incremento ou decremento linear.

Acumulador: variável utilizada para acumular todos os valores dentro do laço.
"""

contador = 1
acumulador = 0

while contador <= 20:
    print(f'{contador},{acumulador}')
    acumulador += contador
    contador += 1   
else:
    print('Condição do while falsa. Executando bloco else...')

print('fim')

"""
A estrutura de repetição (também chamada de laço) while é usada quando
precisamos que alguma ação ou ações, seja(m) executada(s) enquanto uma condição for 
verdadeira. 

sintaxe:

while condição:
    implementações... (ações)

Quando temos uma situação em que a condição nunca será falsa, então temos
um loop infinito, o que é um problema indesejável.

continue: serve para pular um trecho do laço.
break: serve para encerrar um bloco de repetição (seja for ou while)
"""

# exemplo de loop infinito
# while True:
#     valor = input('Informe um valor: ')
#     print(f'O valor é {valor}.')

# exemplo útil
contador = 0
while contador <= 100:
    print(contador)
    # mesmo que: contador = contador + 1
    contador += 1; 

print('fim')

# exemplo com continue
contador = 0
while contador < 5: 
    if contador == 2: # 0 1 3 4 (vai pular o laço em que o contador é 2)
        contador = contador + 1
        continue

    print(contador)
    contador = contador + 1

print('fim')

# exemplo com break
contador = 0
while contador < 5: 
    if contador == 2: # 0 1 (vai sair do laço quando o contador for 2)
        contador += 1
        break

    print(contador)
    contador += 1

print('fim')

# exemplo divertido
x = 0

while x <= 4:
    y = 0

    while y <= 2:
        print(f'[{x},{y}]')
        y += 1

    x += 1

print('fim')

# calculadora básica com while
while True:
    exec = input('Deseja entrar na calculadora? [s] ou [n]: ')

    if exec == 'n':
        break

    num1 = input('Informe o 1° Valor: ')
    num2 = input('Informe o 2° Valor: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Por favor informe valores válidos.')
        continue

    num1 = float(num1)
    num2 = float(num2)
    op = input('Informe o Operador: ')

    if op == '+':
        print(f'Resultado é: {num1 + num2}')
    elif op == '-':
        print(f'Resultado é: {num1 - num2}')
    elif op == '*':
        print(f'Resultado é: {num1 * num2}')
    elif op == '/':
        print(f'Resultado é: {num1 / num2}')
    else:
        print('Operador inválido')

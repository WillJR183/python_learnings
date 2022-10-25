"""
A entrada de dados (input) em Python pode ser feita utilizando a função interna input.
Basicamente serve para o usuário interagir com o programa, dessa forma podemos capturar
dados, alterar o fluxo de execução e etc.

OBS: Todo e qualquer dado obtido através do input é um objeto string (str). Isto posto,
dependendo do contexto e operações em que o dado será obtido, é necessário fazer o type
casting (conversão de tipos de dados)
"""

teste = input('Esse é o texto informativo para auxiliar na entrada de dados. Digite algo: ')  # 7

print(f'Dado: {teste}, Tipo de dado: {type(teste)}')  # 7 == string
print()

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nasc = 2022 - int(idade)  # type casting

print()
print(f'{nome} tem {idade} anos.')
print()

num_1 = int(input('Digite o primeiro número: '))  # type casting diretamente no input
num_2 = int(input('Digite o segundo número: ')) 

soma = num_1 + num_2

print()
print(f'A soma de {num_1} e {num_2} é {soma}')

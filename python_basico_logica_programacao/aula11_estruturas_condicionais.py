"""
Estruturas condicionais: IF , ELIF, ELSE

A estrutura básica de condicional é o IF (se). Ele basicamente verifica se uma expressão é
verdadeira, caso seja, executa o bloco indentado daquele nivel.

O ELIF (se não se) é usado quando temos outras alternativas caso a primeira condição (IF) seja
falsa. Dessa forma obrigatoriamente temos que ter um IF para ter um ou mais ELIF.

O ELSE (se não) é usado para executar um bloco de código quando todas as outras condições IF ou ELIF
(caso exista) sejam falsas. Ele não é obrigatório, mas para usa-lo deve existir um IF inicialmente. 
"""

num = int(input('Digite um número (inteiro e positivo): '))

if num == 0:  # verifica se a condição é verdadeira, caso seja, executa o bloco indentado
    print(f'O numero {num} é igual a zero.')  # implementação
elif num < 50 and num > 0:
    print(f'O número {num} é menor que 50.')
elif num > 50:
    print(f'O numero {num} é maior que 50.')
else:  # executa esse bloco caso nenhuma condição seja atendida
    print(f'Número fora dos parâmetros.')

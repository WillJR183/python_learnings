"""
O ponto de entrada para o contexto de formatação de strings em python é utilizando
o mecanismo (recurso) fstrings. Com esse recurso podemos de uma forma mais simplificada
imprimir os valores das variáveis e também formatar a forma como esse valor é impresso.

ex: imc:.2f -> imprime o valor com duas casas decimais
"""

nome = 'Willian JR'
idade = 22
altura = 1.83
peso = 69.2

imc = peso / (altura ** 2)

print(f'{nome} possui {idade} anos de idade e seu IMC é de {imc:.1f}.')

"""
Também existe outro recurso para formatar strings. Essa outra alternativa é utilizando
o método format. Com ele também é possível nomear as variávies que serão impressas
dessa forma pode-se trocar a ordem de exibição ou facilitar a digitação.
"""

print('{} possui {} anos de idade e seu IMC é de {:.1f}.'.format(nome, idade, imc))
print('{0} possui {1} anos de idade e seu IMC é de {2:.1f}.'.format(nome, idade, imc))
print('{n} possui {i} anos de idade e seu IMC é de {im:.1f}.'.format(n=nome, i=idade, im=imc))

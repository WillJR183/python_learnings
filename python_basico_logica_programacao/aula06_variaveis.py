"""
As variáveis em programação são basicamente valores alocados na memória e que recebem
um nome (apelido) ou chave de identificação para acessa-los.

Dentre as recomendações e regras para criar variáveis estão:

- O nome da variável deve ser minúscula.
- O nome da variável deve iniciar com letra.
- Ela pode conter números, portanto que não seja no inicío.
- Pode-se utilizar o '_' underline para separar um nome composto (complexo) ex: data_hora

OBS: Essas diretrizes também se extendem para nomes de pastas e diretórios
"""

nome = 'Willian JR'
idade = 22
altura = 1.83
e_maior = 22 >= 18
peso = 69.2

print('Nome:', nome)
print('Idade:', idade)
print('Altura', altura)
print('Maior de idade:', e_maior)
print('Idade x Altura:', idade * altura)

# Desafio calcular IMC

# 1° solução

imc = peso / (altura ** 2)  # ou altura * altura
print(nome, 'possui', idade, 'anos de idade e, seu IMC é de', imc)

# 2° solução

print(nome, 'possui', idade, 'anos de idade e, seu IMC é de', peso / (altura ** 2))

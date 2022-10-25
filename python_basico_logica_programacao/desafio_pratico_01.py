"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float)
* Criar uma variável com o ano atual
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa com duas casas decimais
* Imprimir um texto com todos os valores usando f-strings
"""

# Solução 1°

nome = 'Willian Junior'
idade = 22
altura = 1.83
peso = 69.2
ano_atual = 2022

ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade, possui {altura} de altura e pesa {peso}kg.')
print(f'{nome} nasceu em {ano_nasc} e seu IMC atualmente é de {imc:.2f}')

# Solução 2°

nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade (int): '))
altura = float(input('Informe sua altura (ex 1.72): '))
peso = float(input('Informe seu peso (ex 81.2): '))
ano_atual = 2022

ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade, possui {altura} de altura e pesa {peso}kg.')
print(f'{nome} nasceu em {ano_nasc} e seu IMC atualmente é de {imc:.2f}')

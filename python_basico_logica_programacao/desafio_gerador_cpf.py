"""
Com base no desafio anterior implementar um gerador de CPFs
"""

# usamos o módulo interno do python random parar gerar valores aleatórios

from random import randint

digitos = str(randint(100000000, 999999999))  # gera 9 digitos entre 1 e 9
novo_cpf = digitos  # atributo a variavel convertida pra string ao novo_cpf
print(novo_cpf)
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    
    print(novo_cpf[index], index, reverso)
    
    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        
        verifica_digito = 11 - (total % 11)
        if verifica_digito > 9:
            verifica_digito = 0

        reverso = 11
        total = 0
        novo_cpf += str(verifica_digito)

print(f'\n{novo_cpf}\n')  # novo cpf gerado !

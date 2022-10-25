"""
ex: CPF = 168.995.350-09

------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
-------------------------------------------------
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9

"""
# 1° solução

print()

# string cpf usada para realizar a validação

cpf = '168.995.350-09'

print(f'CPF Original: {cpf}\n')

# atribuo a variavel os primeiros 9 digitos do cpf e os digitos finais em outra var

digitos_primarios, digitos_finais = cpf.split('-')

# substituo o '.' por uma string vazia para eliminar os espaços

digitos_primarios = digitos_primarios.replace('.', '')  
print(f'Digitos Primários do CPF: {digitos_primarios}\nDigitos Finais do CPF: {digitos_finais}')

print()

# variaveis auxiliares

contador = 10
soma = 0

# enumero a cadeira de caracteres para acessar cada item e uso o contador para fazer os calculos

for enum, item in enumerate(digitos_primarios):
    print(f'{item} x {contador}')
    mp = int(item) * contador
    soma += mp
    contador -= 1

print(f'\nSoma = {soma}\n')

# aplico a fórmula no digito verificador
# formula = 11 - (297 % 11)

result_digito_1 = 11 - (soma % 11)

if result_digito_1 > 9:
    result_digito_1 = 0

print(f'Digito verificador 1: {result_digito_1}\n')

# refaço os passos acima para o segundo digito verificador acrescentando o novo digito válido

digitos_primarios = digitos_primarios + str(result_digito_1)

contador = 11
soma = 0

for enum, item in enumerate(digitos_primarios):
    print(f'{item} x {contador}')
    mp = int(item) * contador
    soma += mp
    contador -= 1

print(f'\nSoma = {soma}\n')

result_digito_2 = 11 - (soma % 11)

if result_digito_2 > 9:
    result_digito_2 = 0

print(f'Digito verificador 2: {result_digito_2}\n')

# adiciono o ultimo digito validado a variavel e verifico com base no cpf original

digitos_primarios = digitos_primarios + str(result_digito_2)

cpf = cpf.replace('.', '').replace('-', '')

if digitos_primarios == cpf:
    print('CPF Válido!\n')
else:
    print('\nCPF Inválido!?\n')

print('\n\n')

# 2° solução
while True:
    cpf_original = input('Digite um CPF: ')
    # cpf_original = '16899535009'
    novo_cpf = cpf_original[:-2]
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

    print(f'\n{novo_cpf}\n')

    seq = novo_cpf == str(novo_cpf[0] * len(cpf))

    if novo_cpf == cpf_original and not seq:
        print('CPF Válido!\n')
    else:
        print('\nCPF Inválido!?\n')
        
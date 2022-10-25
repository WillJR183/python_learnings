# A função print() serve para exibir (imprimir) valores em Python. 
# Ela possui 3 argumentos básicos: values, sep, end.

print('Meu nome é Willian Junior!', end = ' | ')  # default end = '\n'
print('Meu', 'nome', 'é', 'Willian', 'Junior', '!')
print('Meu', 'nome', 'é', 'Willian', 'Junior', '!', sep = '_', end = '\n')

# Formatando o número de CPF. OBS: CPF gerado automaticamente em:
# https://www.4devs.com.br/gerador_de_cpf
# 767.258.902-45

print('767','258','902', sep = '.', end = '-')
print('45')

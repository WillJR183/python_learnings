"""
Operador ternário em Python
"""

# exemplo hipotético, em um sistema de login temos uma variavel para
# identificar se um usuário está logado ou não

# exemplo hipotético sem usar o operador ternário

logged = False  # bool
print()

if logged:  # isso é o mesmo que: if logged == True:
    msg = 'Usuário está logado.'
else:
    msg = 'Login necessário.'

print(msg)
print()


# exemplo hipotético usando operador ternário

logged = False  # bool
msg = 'Usuário está logado.' if logged else 'Login necessário.'

print(msg)
print()


# exemplo mais elaborado

idade = input('Informe sua idade:')

if not idade.isnumeric():
    print('Por favor digite apenas números.\n')
else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg = '\nPode acessar.\n' if maior_de_idade else '\nNão pode acessar.\n'
    print(msg)

"""
A função len() serve basicamente para contar a quantidade de caracteres de uma
variável válida.

OBS: A função len não funciona com tipos de dados numéricos e booleanos.
OBS: A função len funciona com qualquer objeto iterável.

https://docs.python.org/3/library/functions.html#len
"""

dado = input('Informe um dado: ')
qtd_caracteres = len(dado)
print(qtd_caracteres, type(qtd_caracteres))

"""
Exemplo hipotético

Vamos imaginar que precisamos validar a quantidade de caracteres do formuário
de cadastro de um sistema web. Nesse formulário, o campo nome_de_usuario 
digitado pelo cliente no ato de inscrição, deve conter no mínimo 8 caracteres
para que seja válido.
"""

nome_de_usuario = input('Informe seu nome de usuário: ')
qtd_caracteres = len(nome_de_usuario)

if qtd_caracteres < 8:
    print('Atenção! Nome de usuário deve atender as regras. Minimo 8 caracteres.')
else:
    print('Usuário cadastrado com sucesso!')
    
"""
As vezes precisamos deixar em braco algum trecho de código em que vamos codificar
depois, e pra isso utilizamos o que chamam de placeholders. No Python existem 2
formas de utilizar placeholders: 1° pelo termo reservado, feito pra isso 'pass'
ou 2° pelas reticências
"""

# Exemplo

vai_chover = True

if vai_chover:
    pass
else:
    print('xablau')

# Ou

if vai_chover:
    ...
else:
    print('xablau')

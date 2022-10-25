"""
Operadores Lógicos

Esses operadores nos permitem realizar testes lógicos.

and : Retorna verdadeiro (true), se ambas as afirmações forem verdadeiras.
or : Retorna verdadeiro (true), se uma das afirmações for verdadeira.
not: Retorna falso (false), se o resultado for verdadeiro.
"""

# Digamos que hipoteticamente vamos julgar se uma pessoa vai sair ou não. 
# E sabemos que a pessoa só vai sair se estiver com dinheiro e com tempo.
# Dessa forma precisamos utilizar o operador AND. Abaixo estão outras
# abordagens mas que não atendem a condição.

esta_chovendo = False
estou_com_tempo = True
estou_com_dinheiro = False

print(estou_com_dinheiro and estou_com_tempo)

print(esta_chovendo or estou_com_tempo)
print(not esta_chovendo or estou_com_tempo)

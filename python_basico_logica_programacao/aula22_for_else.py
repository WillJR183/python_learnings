"""
Assim como a estrutura de repetição while, também é possível utilizar o for com else,
embora em ambos os casos seja muito raro o emprego do mesmo.
"""

# exemplo hipotético

frutas = ['laranja', 'abacaxi', 'maracujá', 'morango', 'uva']

for fruta in frutas:
    if fruta.upper().startswith('B'):
        print(f'A fruta {fruta.upper()} começa com A')
        break
else:
    print("Não existe palavras que começam com 'a' na lista.")
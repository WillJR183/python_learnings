"""
Implementar um simples jogo da forca utilizando os conhecimentos aprendidos até agora
"""

print()

palavra_secreta = 'GALILEU'
tamanho = len(palavra_secreta)
letras_digitadas = []
tentativas = 5

print(f'A palavra secreta possui {tamanho} letras.')
print(f'Tentavivas: {tentativas}')

mascara = ''

for letra in palavra_secreta:  # itero sobre a string e substituo os caracteres
    mascara += '_ '

print(mascara)

while True: # inicializa e mantém loop até acabar o jogo

    if tentativas == 0:  # verifica se a quantidade de tentativas chegou em zero
        print('\n###############################################\n')
        print('| Game Over |')
        print('\n###############################################') 
        break

    print()

    letra = input('Digite uma letra: ')
    tam_letra = len(letra)
    letra = letra.upper()  # transformo o caractere de entrada em maisculo

    if tam_letra != 1:  # verifica se digitou mais de  uma letra
        print()
        print('Por favor insire UMA letra!')
        continue  # caso entre no if, volta para o laço while
    
    print()

    if letra in letras_digitadas:  # verifico se a letra digitada já foi informada antes
        print(f'Você já tentou essa letra "{letra}".')
        continue  # se entrar no if então volta pro laço
    
    letras_digitadas.append(letra)  # adiciono na lista as letras digitadas
    print(f'Letras usadas: {letras_digitadas}')
        
    if letra in palavra_secreta:  # verifico se a letra digitada contém na palavra secreta
        print(f'Boaa! A palavra secreta possui a letra {letra}.')
    else:
        print(f'Erooou! A palavra secreta não possui a letra {letra}.')
        tentativas -= 1  # se cair no else, então diminuo a quantidade de tentativas
        print(f'Tentavivas restantes: {tentativas}')

    mascara = ''

    for letra_secreta in palavra_secreta:  # itero sobre a palavra secreta
        
        if letra_secreta in letras_digitadas:  # verifico quais letras já foram descobertas
            mascara += letra_secreta  # as que foram descobertas, revelamos 
        else:
            mascara += '_'  # as que ainda não foram, colocamos uma mascara para ocultar

    if mascara == palavra_secreta:  # verifico se a palavra secreta foi descoberta
        print('\n###############################################\n')
        print('Aleeluuia ! Você venceu, parabéns!!')
        print('\n#################################################')
        print(f'\nPalavra secreta era: {mascara}\n')
        break

    print(f'Palavra secreta: {mascara}')

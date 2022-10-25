"""
A estrutura de repetição while também pode ser usada para iterar sobre strings,
apesar da estrutura for se mais usada para esse propósito.
"""

#        Índices 
#        012345678.........19
texto = 'Minha mãe é uma peça'  # objeto iterável
tamanho_texto = len(texto)

contador = 0
while contador < tamanho_texto:  # iteração
    print(texto[contador])
    contador += 1

print()

copia_texto = ''
contador = 0
while contador < tamanho_texto:
    copia_texto += texto[contador]  # concatenando strings
    print(copia_texto)  # printando cada passo da cópia
    contador += 1

print()
print(f'Cópia: {copia_texto}')
print()

# montando um novo texto com os caracteres 'm' maiusculos 

copia_texto_02 = ''
contador = 0
while contador < tamanho_texto:
    if texto[contador] == 'm':
        copia_texto_02 += 'M'
    else:    
        copia_texto_02 += texto[contador]  # concatenando strings
    contador += 1

print(copia_texto_02)

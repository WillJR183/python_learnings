"""
Strings, assim como qualquer outro objeto iterável, possuem indices
Além disso, através desse indice é possível aplicar algo chamado
de fatiamento (slice). Em uma string, cada caractere representa 
um indice que começa com 0 e vai até o final da string, incluindo
espaços. Os indices podem ser positivos e negativos, a diferença
está na ordem de contagem do indice. O principal recurso e muito
utilizado com o emprego dos indices negativos é acessar o último
elemento ou caractere com o indice -1

O fatiamento de String: string[inicio:fim:passo]

https://docs.python.org/3/library/stdtypes.html#string-methods
"""
#indice  0123456789.....
teste = 'Willian Marques'

print(teste[0:4]) # fatia do indice 0 até 4 (não inclui o caractere do indice 4)
print(teste[:4]) # mesmo efeito do exemplo acima
print(teste[8:]) # fatia do indice 8 em diante
print(teste[0::2]) # fatia do indice 0 em diante pulando de 2 em 2
print(teste[-15::2]) # mesmo efeito do exemplo acima, porém com indices negativos
print(teste[-1]) # acessa o último elemento

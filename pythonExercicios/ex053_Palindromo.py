"""Faça um script que que leia uma frase qualquer e diga se ela é um palíndromo, d
esconsiderando os espaços"""
"""frase = str(input('Informe uma frase: ')).strip().upper().replace(' ', '')
for f in range(0, len(frase)):
    #print(frase[f])
    continue
for f2 in range(f, -1, -1):
    #print(f'Frase invertida: {frase[f2]}')
    continue
if frase[f] == frase[f2]:
    print('A frase é PALINDROMO')
else:
    print('A frase não é palindromo')
"""
frase = str(input('Informe uma frase: ')).strip().upper().replace(' ', '')
fraseInversa = ''
for f in range(len(frase) - 1, -1, -1):
    fraseInversa += frase[f]
if frase == fraseInversa:
    print('A frase é PALINDROMO')
else:
    print('A frase não é palindromo')

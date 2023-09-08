"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando estrutura while"""
primeiroTermo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
cont = 0
while cont < 10:
    print(f'{primeiroTermo + (razao * cont)}', end=' -> ')
    cont += 1
print('Fim')

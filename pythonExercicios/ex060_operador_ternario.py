"""Faça um script que leia um número qualquer e mostre o seu fatorial"""
num = int(input('Informe um número inteiro: '))
cont = num
fat = 1
print(f'{num}! = ', end='')
while cont > 0:
    simbolo = '=' if cont == 1 else 'X'
    print(f'{cont} {simbolo}', end=' ')
    fat *= cont
    cont -= 1
print(fat)

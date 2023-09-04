"""Faça um script que que leia um número inteiro e diga se ele é ou não um número primo"""
num = int(input('Informe um número inteiro: '))
cont = 0
for i in range(1, num + 1):
    if num % 1 == 0:
        cont += 1
print(f'O {num}, foi divisível {cont} vezes')
if cont == 2:
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')
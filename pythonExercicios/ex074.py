"""Faça um script que vai gerar cinco número aleatorios e colocar em uma tupla.
Depois mostrar a listagem dos números gerados e mostrar o maior e menos número da tupla"""
from random import randint
maior = menor = 0
print(f'Os valores sorteados foram: ',end='')
for i in range(0, 5):
    num = randint(1, 10)
    numeros = (num)
    numeros = (randint(1, 10))
    print(f'{numeros}', end=' ')

    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'\nO maior valor foi {maior}')
print(f'O menor valor foi {menor}')

print('-=' * 40)
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nMaior número na tupla: {max(numeros)}')
print(f'Menor número na tupla: {min(numeros)}')

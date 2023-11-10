'''Faça um script que tenha uma lista chamada números e duas funções chamadas sorteio() e soma_par()
A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda vai mostrar
a soma entre todos os valores pares sorteados pela função anterior'''
from random import randint
numeros = []
def sorteio():
    for n in range(0, 5):
        numeros.append(randint(1, 10))

    print(f'Sorteando {len(numeros)} valores da lista', end=' ')
    for num in numeros:
        print(f'{num}', end=' ')
    print('PRONTO!')


def soma_pares(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}')

sorteio()
soma_pares(numeros)
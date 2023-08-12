"""Faça um script que leia um número real qualquer e mostre na tela
a sua porção inteira. Ex: digitando 6.127 vai mostrar 6"""
from math import trunc
num = float(input('Informe um número real: '))
#print(f'O valor informado foi {num} e sua porção inteira é: {int(num)}')
print(f'O valor informado foi {num} e sua porção inteira é: {trunc(num)}')

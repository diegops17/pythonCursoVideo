"""Faça um script que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""
from math import hypot
catetoOposto = float(input('Informe o cateto oposto: '))
catetoAdjaceste = float(input('Informe o cateto adjaceste: '))
hipotenusa = hypot(catetoOposto, catetoAdjaceste)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')

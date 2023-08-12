"""Faça um script que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo"""
import math
angulo = float(input('Informe um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Ângulo informado: {angulo}\nSeno: {seno:.2f}'
      f'\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}')
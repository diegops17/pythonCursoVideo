"""Faça um script que faça um computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import randint
numeroSorteado = randint(0, 5)
numero = int(input('Digíte um número inteiro: '))
if numero == numeroSorteado:
    print(f'Parabéns você venceu! Computador pensou em: {numeroSorteado}')
else:
    print(f'Você perdeu! Computador pensou em: {numeroSorteado}')

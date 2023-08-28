"""Faça um script para criar um jogo de jokenpô"""
from random import choice
from time import sleep
escolhaHumano = str(input('Escolha PEDRA, PAPEL OU TESOURA: ')).strip().upper()
escolhaComputador = choice(['PEDRA', 'PAPEL', 'TESOURA'])

print('JO..'), sleep(0.5)
print('KEN..'), sleep(0.5)
print('JOKENPÔ'), sleep(0.5)
print('-'*30)
if ((escolhaHumano == 'PEDRA' and escolhaComputador == 'TESOURA')
        or (escolhaHumano == 'TESOURA' and escolhaComputador == 'PAPEL')
        or (escolhaHumano == 'PAPEL' and escolhaComputador == 'PEDRA')):
    print(f'VOCÊ VENCEU!\nVOCÊ: {escolhaHumano} X PC: {escolhaComputador}')

elif ((escolhaHumano == 'PEDRA' and escolhaComputador == 'PEDRA')
        or (escolhaHumano == 'TESOURA' and escolhaComputador == 'TESOURA')
        or (escolhaHumano == 'PAPEL' and escolhaComputador == 'PAPEL')):
    print(f'EMPATE!\nVOCÊ: {escolhaHumano} X PC: {escolhaComputador}')
else:
    print(f'VOCÊ PERDEU!\nVOCÊ: {escolhaHumano} X PC: {escolhaComputador}')
print('-'*30)
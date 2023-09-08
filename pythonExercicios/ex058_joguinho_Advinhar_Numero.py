"""Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
numComputador = randint(0, 10)
contPalpites = 0
flag = False
print('Computador pensando...')
sleep(1)
#while not flag:
while flag != True:
    palpite = int(input('Chute um número: '))
    if palpite == numComputador:
       flag = True
    else:
        if palpite < numComputador:
            chute = 'maior'
        else:
            chute = 'menor'
        print(f'Opção incorreta! Chute um número {chute}!')
    contPalpites += 1
print(f'Parabéns você acertou! com {contPalpites} chutes')

"""058 Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
numComputador = randint(0, 10)
contPalpites = 0
flag = False

print('Computador pensando...')
sleep(1)
palpite = int(input('Chute um número: '))
while flag != True:
    if palpite == numComputador:
       print(f'Parabéns você acertou!', end=' ')
       flag = True
    else:
        palpite = int(input('Opção incorreta! Chute um novo número: '))
    contPalpites += 1
print(f'Quantidade de chutes {contPalpites}')

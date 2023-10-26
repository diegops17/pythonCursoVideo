'''Faça um script onde 4 jogadores joguem um dado e tenham resultados aleatórios
Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem
Sabendo que o vencedor tirou o maior número do dado'''
from random import randint
from time import sleep
jogo = {}

for i in range(1, 5):
    numero = randint(1, 6)
    jogo[f'jogador{i}'] = numero

print('Valores sorteados:')
for i, v in jogo.items():
    print(f'O {i} tirou {v}')
    sleep(1)

print('Ranking do jogadores:')
for i in range(1, 5):
    print(jogo.values())
    #print(f'{i}º lugar: ')
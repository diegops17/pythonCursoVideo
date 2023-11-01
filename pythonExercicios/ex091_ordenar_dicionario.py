'''Faça um script onde 4 jogadores joguem um dado e tenham resultados aleatórios
Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem
Sabendo que o vencedor tirou o maior número do dado'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
for i in range(1, 5):
    numero = randint(1, 6)
    jogo[f'jogador{i}'] = numero
print('Valores sorteados:')
for i, v in jogo.items():
    print(f'O {i} tirou {v}')
    sleep(2)
print('Ranking do jogadores:')
cont = 1
for i, v in sorted(jogo.items(), key=itemgetter(1), reverse=True):
    print(f'O {cont}º lugar é {i} com {v} pontos')
    cont += 1
    sleep(1)
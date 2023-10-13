"""Faça o script que ajude um jogador da mega sena a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
cadastrando tudo em uma lista"""
from random import randint
from time import sleep
quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantidadeJogos} JOGOS -=-=-=')
listaJogos = [[] for _ in range(quantidadeJogos)]

for i in range(quantidadeJogos):
    for j in range(0, 6):
        numero = randint(1, 60)
        if numero not in listaJogos:
            listaJogos[i].append(numero)
#print(listaJogos)
for index, valor in enumerate(listaJogos):
    print(f'Jogo {index + 1}: {valor}')
    sleep(2)

#for indice, valor in enumerate(listaJogos):
#    print(f'{indice} = {valor}')print(listaJogos)

print(f'-=-=-= < BOA SORTE > -=-=-=')

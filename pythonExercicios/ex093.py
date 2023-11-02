"""Faça um script que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e a quantidade partidas ele jogou. Gepois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluíndo o total de gols
feitos durante o campeonato."""
jogador = {}
gols = []
totalGols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols.insert(i, int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
#for g in gols:
#    totalGols += g
#    jogador['total'] = totalGols
print('-=' * 20)
print(jogador)
print('-=' * 20)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
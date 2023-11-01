jogador = {}
jogadores = []
gols = []
totalGols = 0
while True:
    opcao = ' '
    totalGols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, partidas):
        gols.insert(i, int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = gols[:]

    for g in gols:
        totalGols += g
        jogador['total'] = totalGols

    gols.clear()

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? '))[0].strip().upper()

    jogadores.append(jogador.copy())

    if opcao == 'N':
        break

'''for g in gols:
    totalGols += g
    jogador['total'] = totalGols
print('-=' * 20)
print(jogador)
print('-=' * 20)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')'''
print(jogadores)
print('-=' * 20)
print('cod nome gols total')
print('-' * 40)
#for i, v in enumerate(jogadores):
#    print(i, v)

for i, j in enumerate(jogadores):
    print(f'{i}', end=' ')
    for v in j.values():
        print(f'{v}', end=' ')
    print('\n')
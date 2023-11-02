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
    jogador['total'] = sum(gols)
    gols.clear()

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]'))[0].strip().upper()

    jogadores.append(jogador.copy())

    if opcao == 'N':
        break
print(jogadores)
print('-=' * 20)
print('cod nome gols total')
print('-' * 40)
for i, j in enumerate(jogadores):
    print(f'{i}', end=' ')
    for v in j.values():
        print(f'{v}', end=' ')
    print(' ')

while True:
    codigo = ''
    for i, v in enumerate(jogadores):
        codigo = int(input('Mostrar os dados de qual jogador 999 para parar? '))
        if codigo == i:
            print(f'-- LEVANTAMENTO DO JOGADOR  {v["nome"]}: --')
            for indice, valor in enumerate(v["gols"]):
                print(f'No jogo {indice}, fez {valor} gols.')
        elif codigo != i:
            print(f'ERRO! não existe jogador com o códgo {codigo}! Tente novamente!')
        print('-' * 50)
    if codigo == 999:
        break
print('<< VOLTE SEMPRE >>')

"""Faça um script que tenha função chamada ficha(), que recebe dois parâmetros opcionais: o nome
de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha sido informado corretamente."""


def ficha(jogador='', gols=''):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato.'


print('-' * 40)
jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
print(ficha(jogador, gols))



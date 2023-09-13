"""Faça um script que jogue par ou impar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando no final o total de vitórias consecutivas que ele conquistou no final do jogo"""
from random import randint
totalVitorias = 0
while True:
    valorJogador = int(input('Diga um valor: '))
    parImparJogador = str(input('Par ou Ímpar [P/I]: '))[0].strip().upper()
    valorComputador = randint(0, 10)
    parImpar = ''
    soma = valorJogador + valorComputador

    if soma % 2 == 0 and parImparJogador == 'P':
        parImpar = 'PAR'
        totalVitorias += 1
    elif soma % 2 != 0 and parImparJogador == 'I':
        parImpar = 'IMPAR'
        totalVitorias += 1
    else:
        print('-' * 50)
        print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma} DEU {parImpar}')
        print('Você PERDEU!')
        break
    print('-' * 50)
    print(f'Você jogou {valorJogador} e o computador {valorComputador}. Total de {soma} DEU {parImpar}')
    print('-' * 50)
    print('Você VENCEU!\nVamos jogar novamente...')
    print('-=' * 25)
print('-'*50)
print(f'GAME OVER! Você venceu {totalVitorias} consecutivas!')

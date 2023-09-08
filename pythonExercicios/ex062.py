"""Melhore o desafio 061, perguntando se o usupario deseja mostrar mais alguns termos.
O programa deve encerrar quando ele disser que quer mostrar 0 termos"""
primeiroTermo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('\nMais quantos termos deseja mostrar? '))
print('FIM')




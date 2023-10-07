"""Faça um script qure recebe um número inteiro e mostre n primeiros números da sequência fibonacci"""
num = int(input('Informe um número inteiro: '))
cont = penul = 1
atual = ant = 0
while cont <= num:
    print(f'{atual}', end=' -> ')
    ant = penul
    penul = atual
    atual = ant + penul
    cont += 1
print('FIM')

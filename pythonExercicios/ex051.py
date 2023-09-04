"""Faça um script que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão"""
primeiroTermo = int(input('Informe o primeiro termo do PA: '))
razao = int(input('Informe a razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razao
for i in range(primeiroTermo, decimoTermo, razao):
    print(f'{i}', end=' -> ')
print('Fim')
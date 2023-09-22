"""Crie um script que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostre ele por extenso"""
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
num = int(input('Digite um número: '))

while num < 0 or num > 5:
    num = int(input('Tente novamente. Digite um número: '))
    if 0 <= num <= 5:
        break
for indice, valor in enumerate(numeros):
    if num == indice:
        print(f'Você digitou o número {valor}')
print('FIM')
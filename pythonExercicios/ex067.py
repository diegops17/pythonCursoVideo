"""Faça um script que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando um número negativo for digitado"""
num = 0
while True:
    print('-'*40)
    cont = 1
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 40)
    while cont <= 10:
        print(f'{num} X {cont:2} = {num * cont}')
        cont += 1
print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

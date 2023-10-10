"""Crie uma matriz dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação completa"""
numeros = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        numeros[i].append(num)
#print(numeros)
for n in numeros:
    print('')
    for j in n:
        print(f'[{j:^4}]', end=' ')
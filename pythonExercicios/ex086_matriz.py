"""Crie uma matriz dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação completa"""
numeros = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Digite um valor para [{l}, {c}]: '))
        numeros[l].append(num)
for n in numeros:
    print('')
    for j in n:
        print(f'[{j:^5}]', end=' ')

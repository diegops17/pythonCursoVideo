"""Crie uma matriz dimensão 3x3 e preencha com os valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação completa
A-Soma de todos números pares digitados; B-A soma dos valores da terceira coluna
C-O maior valor da segunda coluna"""
somaPares = somaTerceiraColuna = maiorValorSegundaLinha = 0
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
print('\n')
print('-='*30)
for n in numeros:
    p = 1
    for j in n:
        if j % 2 == 0:
            somaPares += j
    somaTerceiraColuna += n[2]
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')

for i in range(len(numeros[1])):
    #print(numeros[1])
    if i == 0:
        maiorValorSegundaLinha = numeros[1][i]
    else:
        if numeros[1][i] > maiorValorSegundaLinha:
            maiorValorSegundaLinha = numeros[1][i]
print(f'A o maior valor da segunda linha é {maiorValorSegundaLinha}.')

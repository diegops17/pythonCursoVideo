"""Faça um script onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista
já na posição correta de inserção sem usar o sort(), no final mostre a lista ordenada na tela"""
numeros = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0:
        numeros.append(num)
    else:
        if numeros[i] < num:
            numeros.insert(numeros[i], num)
            print(f'Adicionado na posição {numeros[i]} da lista')

print(numeros)
"""Crie um script onde o usuário possa digitar sete valores númericos e cadastre-os
em uma lista única que mantenha separados os valores pares e impares, no final
mostre os valores pares e impares em ordem crescente"""
numeros = [[], []]
for i in range(1, 7+1):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f'Lista completa: {numeros}')
print(f'O valores pares digitados foram: {sorted(numeros[0])}')
print(f'O valores impares digitados foram: {sorted(numeros[1])}')
"""Faça um script que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menos peso lidos."""
listaPesos = []
for i in range(1, 5+1):
    peso = float(input(f'Informe o {i}º peso: '))
    listaPesos.append(peso)
print(f'Maior Peso: {max(listaPesos)}')
print(f'Menor Peso: {min(listaPesos)}')
"""
maiorPeso = 0
menorPeso = 0
for i in range(1, 5+1):
    peso = float(input(f'Informe o {i}º peso: '))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        elif peso < menorPeso:
            menorPeso = peso
print(f'Maior Peso: {maiorPeso} Kg')
print(f'Menor Peso: {menorPeso} Kg')
"""
"""Faça um script que simule um caixa eletrônico. No inicio pergunte ao usuário o
valor a ser sacado (número inteiro) e o programa deve informar quantas notas
de  cada valor serão entregues, considere 50, 20, 10 e 1"""
valorsacar = float(input('Qual valor quer sacar? '))
notas50 = notas20 = notas10 = notas5 = notas2 = 0
while True:
    if valorsacar >= 50:
        valorsacar -= 50
        notas50 += 1
    elif valorsacar >= 20:
        valorsacar -= 20
        notas20 += 1
    elif valorsacar >= 10:
        valorsacar -= 10
        notas10 += 1
    elif valorsacar >= 5:
        valorsacar -= 5
        notas5 += 1
    elif valorsacar >= 2:
        valorsacar -= 2
        notas2 += 1
    if valorsacar == 0:
        break
print('-' * 30)
print(f'Total de: {notas50} notas de R$ 50 reais')
print(f'Total de: {notas20} notas de R$ 20 reais')
print(f'Total de: {notas10} notas de R$ 10 reais')
print(f'Total de: {notas5} notas de R$ 5 reais')
print(f'Total de: {notas2} notas de R$ 2 reais')
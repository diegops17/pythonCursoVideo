"""Faça um script que leia 5 valores númericos e guarde-os em uma lista.
No final mostre qual foi o maior o menor valor digitado e as suas respectivas posições na lista"""
numeros = []
maior = menor = 0
for i in range(0, 5):
  numeros.append(int(input(f'Informe um valor para posição {i}: ')))
  if i == 0:
    maior = numeros[i]
    menor = numeros[i]
  else:
    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
print(f'Números na lista: {numeros}')
print(f'O maior número é {maior} e está nas posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor número é {menor} e está nas posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print()
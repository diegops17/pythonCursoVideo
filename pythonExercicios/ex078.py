"""Faça um script que leia 5 valores númericos e guarde-os em uma lista.
No final mostre qual foi o maior o menor valor digitado e as suas respectivas posições na lista"""
numeros = []
maior = menor = posicaoMaior = posicaoMenor = 0
for i in range(0, 5):
  numeros.append(int(input('Informe um valor: ')))

  if i == 0:
    maior = numeros[i]
    menor = numeros[i]
  else:
    if numeros[i] > maior:
        maior = numeros[i]
        posicaoMaior = i
    elif numeros[i] < menor:
        menor = numeros[i]
        posicaoMenor = i
print(f'Números na lista: {numeros}')
print(f'O maior número é {maior} e está na posição {posicaoMaior}')
print(f'O menor número é {menor} e está na posição {posicaoMenor}')
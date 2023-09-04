"""Faça um script que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date
anoAtual = date.today().year
contMaiores = 0
contMenores = 0
for i in range(1, 7+1):
    ano = int(input(f'Informe o {i}ª ano: '))
    idade = anoAtual - ano
    if idade < 18:
        contMenores += 1
    else:
        contMaiores += 1
print(f'Total de menores de idade: {contMenores}')
print(f'Total de maiores de idade: {contMaiores}')
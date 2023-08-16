"""Faça um script que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados"""
ano = int(input('Informe o ano: '))
print(f'Unidade: {ano // 1 % 10}')
print(f'Dezena: {ano // 10 % 10}')
print(f'Centena: {ano // 100 % 10}')
print(f'Milhar: {ano // 1000 % 10}')
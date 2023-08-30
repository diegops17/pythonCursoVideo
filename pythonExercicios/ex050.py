"""Faça um script que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar desconsidere-o"""
soma = 0
for cont in range(1, 6+1):
    num = int(input(f'Informe um {cont}º inteiro: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares é: {soma}')
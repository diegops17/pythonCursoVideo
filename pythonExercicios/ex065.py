"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre:
a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
se ele quer ou não continuar a digitar valores"""
soma = 0
maior = 0
menor = 0
cont = 0
media = 0
op = ''
while op != 'N':
    num = int(input('Informe um número inteiro: '))
    op = str(input('Deseja continuar [S] - SIM ou [N] = Não: '))[0].strip().upper()
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont += 1
    soma += num
media = soma / cont
print(f'A média entre os números digitados é: {media:.2f}')
print(f'O maior número foi o: {maior}, o menor número foi o: {menor}')
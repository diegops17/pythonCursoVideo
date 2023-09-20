"""Faça um script que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar 999, que é a condição de parada. No final mostre quantos números
foram digitados e qual foi a soma entre eles desconsiderando o flag"""
soma = cont = num = 0
while True:
    num = int(input('informe um número inteiro [999] para parar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram dígitados {cont} números e a soma entre eles é {soma}')

"""Faça um script que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999 no final da parada. No final
mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando o flag"""
soma = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Informe um número inteiro: [999] para parar: '))
    if num != 999:
        cont += 1
        soma += num
print(f'Foram digitados: {cont} números\nA soma entre os números são: {soma}')
"""
Faça um script que leia dois números inteiros e comparare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior, -O segundo valor é maior, -Não existe valor maior, -Os dois são iguais
"""
n1 = int(input('Informe o primeiro número inteiro: '))
n2 = int(input('Informe o segundo número inteiro: '))

if n1 > n2:
    print(f'O primeiro valor é maior que o segundo')
elif n2 > n1:
    print(f'O segundo valor é maior que o primeiro')
else:
    print('Os valores são iguais!')

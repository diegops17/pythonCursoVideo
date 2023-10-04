"""Faça um script onde o usuario possa digitar vários valores númericos e cadastre-os em uma lista,
caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados em ordem crescente."""
numeros = []
while True:
    opcao = ' '
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('valor duplicado! não vou adicionar')
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
    if opcao == 'N':
        break
print(sorted(numeros))
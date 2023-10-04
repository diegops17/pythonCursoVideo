"""Crie um script que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares
No final mostre as 3 listas"""
numeros = []
pares = []
impares = []
while True:
    opcao = ' '
    num = int(input('Digite um valor: '))
    numeros.append(num)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
    if opcao == 'N':
        break
for i in numeros:
    pares.append(i) if i % 2 == 0 else impares.append(i)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {pares}')
print(f'A lista impares é: {impares}')

"""Crie um script que vai ler vários números e colocar em uma lista, depois disso,
A - Quantos números foram digitados; B - A lista de valores em ordem decrescente
C - Se o valor 5 foi digitado ou não na lista"""
numeros = []
while True:
    opcao = ' '
    num = int(input('Digite um valor: '))
    numeros.append(num)

    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
    if opcao == 'N':
        break
print(f'Foram digitados: {len(numeros)} elementos')
print(f'Os valores em ordem decrescente: são {sorted(numeros, reverse=True)}')
print(f'O valor 5 faz parte da lista' if 5 in numeros else ' O valor 5 não foi encontrado na lista')
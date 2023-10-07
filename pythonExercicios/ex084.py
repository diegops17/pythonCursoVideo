"""Faça um script que leia o nome e peso de vparias pessoas, guardando tudo em uma lista, no final mostre:
A-Quantas pessoas foram cadastradas; B-Uma listagem com as pessoas mais pesadas, C-Uma listagem com
as pessoas mais leves"""
pessoas = []
aux = []
maiorPeso = menorPeso = 0
while True:
    opcao = ' '
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = aux[1]
    else:
        if aux[1] > maiorPeso:
            maiorPeso = aux[1]
        if aux[1] < menorPeso:
            menorPeso = aux[1]
    pessoas.append(aux[:])
    aux.clear()

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N] '))[0].strip().upper()
    if opcao == 'N':
        break
print(pessoas)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'Com base no peso de {maiorPeso}Kg, as pessoas são ', end=' ')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nCom base no peso {menorPeso}Kg, as pessoas são ', end=' ')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end=' ')

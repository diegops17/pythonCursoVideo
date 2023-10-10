"""Faça um script onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista
já na posição correta de inserção sem usar o sort(), no final mostre a lista ordenada na tela"""
numeros = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print(f'{num}. Foi adicionado no final da lista')
    else:
        p = 0
        while p < len(numeros):
            if num <= numeros[p]:
                numeros.insert(p, num)
                print(f'{num}. Foi adicionado na posição {p} da lista')
                break
            p += 1
print(numeros)
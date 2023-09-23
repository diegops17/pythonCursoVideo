"""Faça um script que leia quatro valores pelo tecladoe guarde-s em uma tupla. No final mostre:
A quantas vezes apareceu o valor 9, B-Em que posição foi digitado o primeiro valor 3
C-Quantos foram os valores pares"""
numeros = (int(input(f'Digite o 1º número: ' )), int(input(f'Digite o 2º número: ' )),
           int(input(f'Digite o 3º número: ' )), int(input(f'Digite o 4º número: ' )))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')



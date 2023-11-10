'''Faça um script que tenha uma função chamada maior(), que receba vários parametros com valores inteiros
Analise todos os valores e dizer qual o maior
'''
def maior(*numeros):
    contador = maior = 0
    print('Analisando os valores passados...')
    for numero in numeros:
        print(numero, end=' ')
        contador += 1

        if contador == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    print(f'foram informados {contador} valores ao todo.', end=' \n')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(1)
maior(0)

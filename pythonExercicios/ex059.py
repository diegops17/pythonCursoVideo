"""059 Crie um script que leia dois valores e mostre um menu na tela
[1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa,
o programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
opcao = 0
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
while opcao != 5:
    opcao = int(
        input("""[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do Programa\nOpção: """))
    if opcao == 1:
        print(f'A soma de {num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'A soma de {num1} * {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'Primeiro número {num1} é maior')
        elif num2 > num1:
            print(f'Segundo número {num2} é maior')
        else:
            print(f'{num1} e {num2} são iguais!')
    elif opcao == 4:
        num1 = int(input('Informe um novo primeiro número: '))
        num2 = int(input('Informe um novo segundo número: '))
    elif opcao != 5:
        print('Opção inválida! Tente novamente')
    sleep(2)
print('Fim')
"""
037 Faça um script que leia um número inteiro qualquer e peça para o usuário escolher qual será a base conversão:
1 - para binário, 2 - para octal, 3 - para hexadecimal
"""
op = int(input('Conversor de números:\n[1] - para binário\n[2] - para octal'
               '\n[3] - para hexadecimal\nEscolha uma opção:  '))
numero = int(input('Informe um número inteiro: '))
if op == 1:
    binario = bin(numero)
    print(f'{numero} convertido para binário é: {binario}')
elif op == 2:
    octal = oct(numero)
    print(f'{numero} convertido para binário é: {octal}')
elif op == 3:
    hexadecimal = hex(numero)
    print(f'{numero} convertido para hexadecimal é: {hexadecimal}')
else:
    print('Opção inválida')
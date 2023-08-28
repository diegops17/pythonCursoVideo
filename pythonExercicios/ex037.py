"""037 Faça um script que leia um número inteiro qualquer e peça para o usuário escolher qual será a base conversão:
1 - para binário, 2 - para octal, 3 - para hexadecimal
"""
numero = int(input('Informe um número inteiro: '))
op = int(input('Conversor de números:\n[1] - para binário\n[2] - para octal'
               '\n[3] - para hexadecimal\nEscolha uma opção:  '))
if op == 1:
    dadoConvertido = bin(numero)
    #print(f'{numero} convertido para binário é: {binario[2:]}')
elif op == 2:
    dadoConvertido = oct(numero)
elif op == 3:
    dadoConvertido = hex(numero)
else:
    print('Opção inválida')
    exit()
print(f'{numero} convertido para binário é: {dadoConvertido}')

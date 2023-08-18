"""Faça um script que verifique se os lados digitados podem formar um triângulo"""
lado1 = float(input('Informe o primeiro lado: '))
lado2 = float(input('Informe o segundo lado: '))
lado3 = float(input('Informe o terceiro lado: '))
if((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado3 + lado1) > lado2):
    print('Os lados informados formam um triângulo')
else:
    print('Não é um triângulo')

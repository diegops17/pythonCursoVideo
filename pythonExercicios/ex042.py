"""Refaça o script dos triângulos, acrescentando o recursos de mostrar que tipo de triângulo será formado
-Equilatero: todos os lados iguais -Isóceles: dois lados iguais -Escaleno: todos os lados diferentes
"""
lado1 = float(input('Informe o primeiro lado do triângulo: '))
lado2 = float(input('Informe o segundo lado do triângulo: '))
lado3 = float(input('Informe o terceiro lado do triângulo: '))

if ((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado1 + lado3) > lado2):
    print('Formam um triâgulo', end=' ')
    if (lado1 == lado2) and (lado3 == lado2) and (lado1 == lado3):
        print(f'Os lados formam um triâgulo EQUILÁTERO')
    elif (lado1 == lado2) or (lado1 == lado3):
        print(f'Os lados formam um triâgulo ISÓCELES')
    else:
        print(f'Os lados formam um triâgulo ESCALENO')

else:
    print('Não formam um triâgulo')
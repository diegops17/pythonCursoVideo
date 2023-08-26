"""Faça um script que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:-abaixo de 18.5: abaixo do peso
-Entre 18.5 e 25: peso ideal -25 até 30: Sobrepeso -30 até 40: Obesidade -Acima de 40: Obesidade mórbida
"""
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe o sua altura: '))
imc = float(format(peso / (altura * altura), '.2f'))
if imc <= 18.4:
    print(f'IMC: {imc} - ABAIXO DO PESO')
elif (imc >= 18.5) and (imc <= 25):
    print(f'IMC: {imc} - PESO IDEAL')
elif (imc >= 26) and (imc <= 30):
    print(f'IMC: {imc} - SOBREPESO')
elif (imc >= 31) and (imc <= 40):
    print(f'IMC: {imc} - OBESIDADE')
else:
    print(f'IMC: {imc} - OBESIDADE MÓRBIDA')

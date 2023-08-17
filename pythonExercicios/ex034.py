"""Faça um script que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%"""
salario = float(input('Informe o salário R$ '))
if salario >= 1251:
    salario = salario + ((salario * 10) / 100)
    print(f'Aumento de 10% novo salário R$ {salario:.2f}')
else:
    salario = salario + ((salario * 15) / 100)
    print(f'Aumento de 15% novo salário R$ {salario:.2f}')
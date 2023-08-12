#Faça um script que leia o salário de um funcionario
#e mostre seu novo salario com 15% de aumento
PERCENTUAL = 15
salario = float(input('Informe o seu salário R$ '))
valorAumento = ((salario * PERCENTUAL) / 100)
novoSalario = salario + valorAumento
print(f'Ajuste de {PERCENTUAL}%\nEquivale a R$ {valorAumento:.2f}\nNovo salário reajustado {novoSalario:.2f} reais')
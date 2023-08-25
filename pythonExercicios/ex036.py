"""
Faça um script para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprétimo será negado
"""
valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
quantidadeAnosPagar = int(input('Informe a quantidade de ano que deseja pagar? '))
salario30 = ((salario * 30) / 100)
valorParcela = valorCasa / (quantidadeAnosPagar * 12)

if valorParcela > salario30:
    print('Empréstimo Negado!')
else:
    print('Emprestimo Aprovado!')
print(f'Valor mensal das parcelas R$ {valorParcela:.2f}')
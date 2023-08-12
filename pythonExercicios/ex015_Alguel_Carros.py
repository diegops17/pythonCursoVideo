#Faça um script que pergunte a quantiidade de km percorrido por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 reais por dia e R$0,15 por Km rodado
VALORDIA = 60
VALORKM = 0.15
kmPercorrido = float(input('Informe quantos Km percorreu: '))
diasAlugados = int(input('Informe quantos dias alugou o carro: '))
valorPagar = ((kmPercorrido * VALORKM) +(diasAlugados * VALORDIA))
print(f'O total a pagar é de R$ {valorPagar:.2f}')

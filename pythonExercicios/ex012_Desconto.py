#Faça um script que leia o valor de um produto e mostre
#seu novo valor com 5% de desconto
PERCETUAL = 5
valorProduto = float(input('Informe o valor do produto R$ '))
desconto = ((valorProduto * PERCETUAL) / 100)
novoValor = valorProduto - desconto
print(f'Desconto de {PERCETUAL}%\nEquivale a R$ {desconto:.2f}\nNovo valor R$ {novoValor:.2f} reais')
"""Faça um script que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-Á vista dinheiro/cheque: 10% de desconto -Á vista no cartão: 5% de desconto
-Em até 2X no cartão: preço normal -3X ou mais no cartão: 20% de juros
"""
valorProduto = float(input('Informe o valor do produto R$ '))
print('Escolha a Forma de Pagamento')
print(f'-'*40)
op = int(input('[1] - Á vista dinheiro/cheque\n[2] - Á vista no cartão\n[3] - 2X no cartão\n'
               '[4] - 3X ou mais no cartão\nInforme a opção: '))
print(f'-'*40)
if op == 1:
    totalPagar = valorProduto - ((valorProduto * 10) / 100)
elif op == 2:
    totalPagar = valorProduto - ((valorProduto * 5) / 100)
elif op == 3:
    totalPagar = valorProduto
    valorParcelas = totalPagar / 2
    print(f'Sua compra será parcelada em 2X de R$ {valorParcelas}')
elif op == 4:
    totalPagar = valorProduto + ((valorProduto * 20) / 100)
    quantidadeParcelas = int(input('Informe a quantidade de parcelas: '))
    valorParcelas = totalPagar / quantidadeParcelas
    print(f'Sua compra será parcelada em {quantidadeParcelas}X de R$ {valorParcelas}')
else:
    print('Opção Inválida!')
    exit()
print(f'Total a pagar R$ {totalPagar:.2f}')
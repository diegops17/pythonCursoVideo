"""Faça um script que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário
 vai continuar. No final, mostre: Qual é o total gasto na compra; Quantos produtos custam mais de 1000;
 Qual é o nome do produto mais barato"""
totalCompra = quantidadeProdutosMais1000 = cont = menorValor = 0
produtoMaisBarato = ''
while True:
    opcao = ''
    nomeProduto = str(input('Nome produto: '))
    valorProduto = float(input('Valor produto R$ '))

    totalCompra += valorProduto

    if valorProduto > 1000:
        quantidadeProdutosMais1000 += 1

    if cont == 0:
         menorValor = valorProduto
    else:
        if valorProduto < menorValor:
            produtoMaisBarato = nomeProduto
            menorValor = valorProduto

    while opcao != 'S':
        opcao = str(input('Quer continuar? [S/N] '))[0].upper().strip()

        if opcao == 'N':
            break
    cont += 1
    if opcao == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total da compra R$ {totalCompra}')
print(f'Foram {quantidadeProdutosMais1000} que custam mais de R$ 1.000 reais')
print(f'O produto mais barato é {produtoMaisBarato} que custa R$ {menorValor} reais')
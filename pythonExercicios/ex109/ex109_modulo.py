import moeda

preco = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, False)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')

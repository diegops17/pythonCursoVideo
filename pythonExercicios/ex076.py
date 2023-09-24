"""Faça um script que tenha uma tupla única com nomes de produtos e seus respectivos preços
na sequência, No final faça uma listagem de preços, organizando os dados ce forma tabular."""
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20,
            'Compasso', 9.90, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'-' * 40)
print(f"{'LISTAGEM DE PREÇOS':^35}")
print(f'-' * 40)
valor = 1
prod = 0
for cont in range(0, len(produtos)):
    print(f'{produtos[prod]} {"."*20} {produtos[valor]:.2f}')
    valor += 2
    prod += 2

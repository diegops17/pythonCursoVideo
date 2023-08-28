#Faça um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome = str(input('Informe o seu nome: ')).strip()
print('Olá,', nome, 'seja bem vindo cara!')
print('Olá, {} seja bem vindo cara!'.format(nome))
print(f'Olá, {nome} seja bem vindo cara!')


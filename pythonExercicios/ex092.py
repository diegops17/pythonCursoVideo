"""Crie um programa que leia nome, ano de nasciemnto, e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso o CTPS for diferente de zero o dicionário receberá também o ano de contratação
e o salário. Calcule e a crescente, além da idade, com quantos anos a pessoa vai se aposentar
"""
from datetime import date
anoAtual = date.today().year
cadastro = {}
cadastro['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = anoAtual - anoNascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário R$ '))
    idadeApontadoria = (anoAtual - cadastro['contratacao']) + cadastro['idade']
    cadastro['aposentadoria'] = idadeApontadoria
print('-=' * 30)
print(cadastro)
for i, v in cadastro.items():
    print(f'{i} tem o valor {v}')
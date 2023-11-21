"""Crie um script que tenha uma função chamada voto()que vai receber um parâmetro o ano de nasciemnto
de uma pessoa, retornando um valor literal indicando se uma pessoatem voto NEGADO, OPCIONAL e OBRIGATÓRIO"""
from datetime import date


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    resultado = ''
    if idade < 16:
        resultado = 'NÃO VOTA.'

    elif idade > 16 and idade < 65:
        resultado = 'OBRIGATÓRIO.'

    elif idade == 16 or idade > 65:
        resultado = 'VOTO OPCIONAL.'

    return f'Com {idade} anos: {resultado}'


anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(anoNascimento))

"""Faça um script que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: mirim -Até 14 anos: infantil -Até 19 anos: junior -Até 20 anos: Sênior -Acima: Master
"""
from datetime import date
anoNascimento = int(input('Informe o ano de nascimento: '))
idade = date.today().year - anoNascimento
if idade <= 9:
    print(f'Sua idade {idade} anos, categoria: MIRIM')
elif idade <= 14:
    print(f'Sua idade {idade} anos, categoria: INFANTIL')
elif idade <= 19:
    print(f'Sua idade {idade} anos, categoria: JÚNIOR')
else:
    print(f'Sua idade {idade} anos, categoria: MASTER')
"""
Faça um script que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar no serviço militar.
-Se é a hora de se alistar
-Se já passou do tempo do alistamento
O script deverá mostrar também o tempo que falta ou que passou do prazo
"""
from datetime import date
anoNascimento = int(input('Informe apenas o ano do seu nascimento: '))
idade = (date.today().year) - anoNascimento

if idade < 18:
    tempo = 18 - idade
    print(f'Você tem {idade} ano(s). Falta {tempo} ano(s) para você se alistar')
elif idade == 18:
    print(f'Você tem {idade} ano(s). Hora de se alistar')
else:
    tempo = idade - 18
    print(f'Você tem {idade} ano(s). Passou {tempo} ano(s) do perído de se alistar')
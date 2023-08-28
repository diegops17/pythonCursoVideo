"""Faça um script que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar no serviço militar. -Se é a hora de se alistar -Se já passou do tempo do alistamento
O script deverá mostrar também o tempo que falta ou que passou do prazo
"""
from datetime import date
sexo = str(input('Informe o sexo\n[F] - Feminino\n[M] - Masculino\nopção: ')).upper().strip()[0]
print(sexo)
if sexo == 'M':
    anoNascimento = int(input('Informe apenas o ano do seu nascimento: '))
    anoAtual = (date.today().year)
    idade = anoAtual - anoNascimento

    if idade < 18:
        tempo = 18 - idade
        anoAlistamento = anoAtual + tempo
        print(f'Você tem {idade} ano(s). Falta {tempo} ano(s) para você se alistar.', end=' ')
        print(f'Seu alistamento será em {anoAlistamento}')
    elif idade == 18:
        tempo = idade - 18
        print(f'Você tem {idade} ano(s). Hora de se alistar')
    else:
        tempo = idade - 18
        anoAlistamento = anoAtual - tempo
        print(f'Você tem {idade} ano(s). Passou {tempo} ano(s) do perído de se alistar.', end=' ')
        print(f'Você deveria ter se alistado em {anoAlistamento}')
elif sexo == 'F':
    print(f'O alistamento militar não é obrigatório!')
else:
    print('OPÇÃO INVÁLIDA!')
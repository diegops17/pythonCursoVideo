'''Faça um script que leia o nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
boletim = {}
boletim['nome'] = str(input('Informe o nome do aluno: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))

if boletim['media'] >= 7:
    boletim['situacao'] = 'Aprovado'
elif 5 <= boletim['media'] <= 6.9:
    boletim['situacao'] = 'Recuperação'
else:
    boletim['situacao'] = 'Reprovado'

print(boletim)
for i, v in boletim.items():
    print(f'{i.capitalize()} é igual a {v}')

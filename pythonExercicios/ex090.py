'''Faça um script que leia o nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
boletim = {}
nomeAluno = str(input('Informe o nome do aluno: '))
media = float(input(f'Média de {nomeAluno}: '))
boletim['nome'] = nomeAluno
boletim['media'] = media

if media >= 7:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'

print(boletim)
for i, v in boletim.items():
    print(f'{i.capitalize()} é igual a {v}')

'''Faça um script que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta
No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualemnte'''
boletim = []
cont = media = 0
while True:
    opcao = ' '
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    boletim.insert(cont, [nome, [nota1, nota2]])
    cont += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] '))[0].strip().upper()
    if opcao == 'N':
        break
#print(boletim)
print(f'-='*30)
print('No. Nome     Média')
print(f'-'*30)
for indice, valor in enumerate(boletim):
    media = ((valor[1][0] + valor[1][1]) / len(valor[1]))
    print(f'{indice}  {valor[0]:^8}     {media}')
print(f'-'*30)
opcao2 = ''
while True:
    opcao2 = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    print(f'-' * 30)
    for indice, valor in enumerate(boletim):
        if opcao2 == indice:
            print(f'Notas de {valor[0]} são {valor[1]}')
    print(f'-' * 30)
    if opcao2 == 999:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

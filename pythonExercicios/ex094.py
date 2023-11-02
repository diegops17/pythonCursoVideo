'''Faça um script que leia o nome, sexo de várias pessoas guardando os dados  de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final mostre
A-Quantas pessoas foram cadastradas; B - A média de idade do grupo; C - Uma lista com todas as mulheres
D - Uma lista com todas as pessoas com idade acima da média'''
pessoa = {}
pessoas = []
mulheres = []
pessoasAcimaMedia = []
mediaIdade = somaIdades = 0
while True:
    opcao = ' '
    sexo = ' '
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: '))[0].upper().strip()
        if sexo not in 'MF':
            print('ERRO! Digite M ou F')
        else:
            pessoa['sexo'] = sexo

    pessoas.append(pessoa.copy())

    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]? '))[0].upper().strip()
        if sexo not in 'SN':
            print('ERRO! Digite S ou N')
    if opcao == 'N':
        break
print('-=' * 20)
print(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
for p in pessoas:
    somaIdades += p['idade']
    mediaIdade = somaIdades / len(pessoas)

    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
print(f'- A média de idade é de {mediaIdade:.2f} anos.')
print(f'- As mulheres cadastradas forma: {mulheres}')
print(f'- Lista das pessoas que estão acima da média:')
for i in pessoas:
    if i['idade'] > mediaIdade:
        print(i)

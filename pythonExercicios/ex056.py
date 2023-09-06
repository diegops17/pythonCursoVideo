"""Faça um script que leia o nome, idade e sexo de quatro pessoas. No final do programa, Mostre:
A média de idade do grupo. Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos"""
mediaIdadeGrupo = 0
cont = 0
somaIdades = 0
contMulheresMenor20 = 0
homemMaisVelho = ' '
idadeMaiorHomem = 0
for i in range(1, 4+1):
    print(f'-----{i}º Pessoa-----')
    nome = str(input(f'Nome: ')).upper().strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [F OU M]: '))[0].upper().strip()
    cont += 1
    somaIdades += idade
    mediaIdadeGrupo = somaIdades / cont
    if sexo == 'F' and idade < 20:
        contMulheresMenor20 += 1
    elif sexo == 'M':
        if i == 1:
            idadeMaiorHomem = idade
            homemMaisVelho = nome
        if idade > idadeMaiorHomem:
            homemMaisVelho = nome
            idadeMaiorHomem = idade
print(f'A média das idades do grupo é: {mediaIdadeGrupo} anos')
print(f'São {contMulheresMenor20} mulhere(s) com menos de 20 anos')
print(f'Homem mais velho: {homemMaisVelho} com {idadeMaiorHomem} anos')
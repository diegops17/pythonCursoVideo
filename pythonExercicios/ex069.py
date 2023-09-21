"""Faça um scripr que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
deverá perguntar se o usuário quer continuar. No final mostrar: Quantas pessoas tem mais de 18 anos
Quantos homens foram cadastrados. Quantas mulheres tem menos de 20 anos"""
totalPessoasMaior18 = contHomens = contMulheresMenor20 = 0
while True:
    opcao = sexo = ' '
    idade = int(input('idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] '))[0].upper().strip()

    if idade >= 18:
        totalPessoasMaior18 += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheresMenor20 += 1

    print('-'*30)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if opcao == 'N':
         break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {totalPessoasMaior18}')
print(f'Ao todo temos {contHomens} homens cadastrados')
print(f'Total de {contMulheresMenor20} mulher(es) com menos de 20 anos')
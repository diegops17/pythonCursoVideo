"""
Faça um script que leia duas notas de uum aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida: -Média abaixo de 5.0: Reprovado -Média entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado
"""
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = ((nota1 + nota2) / 2)
if media <= 4.9:
    print(f'Média: {media} Reprovado')
elif media >= 5 and media <= 6.9:
    print(f'Média: {media} está em Recuperação')
else:
    print(f'Média: {media} APROVADO!')
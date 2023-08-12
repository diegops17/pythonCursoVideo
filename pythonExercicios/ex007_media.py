#Faça um script que leia as duas notas de um aluno, calcule e mostre a média
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = ((nota1 + nota2) / 2)
print(f'A média obtida entre as notas {nota1} e {nota2} é {media:.1f}')
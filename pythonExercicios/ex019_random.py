"""Um professor quer sortear um dos alunos para apagar o quadro,
faça um script que ajude ele, lendo o nome deles e escrevendo o nome do escolhido"""
from random import choice
aluno1 = input('Informe o nome do 1º aluno: ')
aluno2 = input('Informe o nome do 2º aluno: ')
aluno3 = input('Informe o nome do 3º aluno: ')
aluno4 = input('Informe o nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = choice(alunos)
print(f'O aluno escolhido foi: {alunoEscolhido}')

"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""
import random
a1 = input('Informe o nome do 1º aluno: ')
a2 = input('Informe o nome do 2º aluno: ')
a3 = input('Informe o nome do 3º aluno: ')
a4 = input('Informe o nome do 4º aluno: ')
alunos = [a1, a2, a3, a4]
#ordemSorteio = random.sample(alunos, k=4)
#print(f'Sequência da apresentação: {ordemSorteio}')
random.shuffle(alunos)
print(f'Sequência da apresentação: {alunos}')
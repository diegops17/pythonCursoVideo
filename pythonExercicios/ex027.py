"""Faça um script que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente. EX Ana Maria de Souza primeiro = Ana último = Souza"""
nomeCompleto = str(input('Informe o seu nome completo: ')).strip().upper().split()
print(f'Primeiro nome: {nomeCompleto[0]}')
print(f'Último nome: {nomeCompleto[-1]}')
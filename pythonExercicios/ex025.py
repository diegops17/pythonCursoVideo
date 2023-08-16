"""Crie um script que leia o nome de uma pessoa e de diga se  ela tem SILVA NO NOME"""
nome = str(input('Digite o seu nome completo: ')).strip().upper()
print(f'Tem Silva no nome: {"SILVA" in nome}')

"""Faça um script que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas
O nome com todas minusculas; Quantas letras ao todo (sem considerar espaços); Quantas letras tem o primeiro nome"""
nome = str(input('Informe o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(f"O nome informado tem: {len(nome.replace(' ',''))} letras")
#print(f"O nome informado tem: {len(nome) - nome.count(' ')} letras")
print(f'Primeiro nome tem: {len(nome.split()[0])} letras')

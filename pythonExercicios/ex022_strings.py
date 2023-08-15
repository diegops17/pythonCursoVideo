"""Faça um script que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas minusculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome"""

nome = str(input('Informe o seu nome completo: '))
primeiroNome = nome.split()
print(nome.upper())
print(nome.lower())
print(f"O nome informado tem: {len(nome.replace(' ','').strip())} letras")
print(f'Primeiro nome tem: {len(primeiroNome[0])} letras')

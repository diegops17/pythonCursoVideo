"""Crie um script que leia o nome de uma cidade e de diga se ela começa ou não com o nome SANTO"""
cidade = str(input('Informe o nome da cidade: ')).strip().upper().split()
print(f'A cidade começa com Santo? {"SANTO" in cidade[0]}')

""" Faça um script que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A; Em que posição ela aparece a primeira vez ;Em que posição ela aparece a última vez"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Quantas vezes aparece a letra A? {frase.count("A")}')
print(f'Em que posição aparece a letra A pela primeira vez? {frase.find("A")}')
print(f'Em que posição aparece a letra A pela última vez? {frase.rfind("A")}')

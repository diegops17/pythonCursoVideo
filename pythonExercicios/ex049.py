"""Faça um script que refaça o ex 00, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for"""
num = int(input('Informe um número inteiro: '))
print('-'*5,f'TABUADA DE {num}','-'*5)
#print(f'{num:-^10}')
for n in range(1, 10+1):
    print(f'{num} X {n:2} = {num * n}')
print('-'*20)

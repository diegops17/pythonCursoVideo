'''Faça um script que tenha uma função chamada area(), que receba as as dimensões de um terreo
retangular (largura e comprimento) e mostre à área do terreno'''
print('Controle de Terrenos')
print('-' * 30)
def area(l, c):
    area = l * c
    print(f'A área de um térreno {l} X {c} é de {area}m²')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

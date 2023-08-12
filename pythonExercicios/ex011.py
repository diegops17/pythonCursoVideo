#Faça um script que leia a altura e largura de uma parede
#calcule a sua área e a quantidade de tinta necessária para pinta-la
#Sabendo que cada litro de tinta pinta uma área de 2m².
altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
TINTA = 2
area = altura * largura
quantidadeTinta = area / TINTA
print(f'A parade com {altura} X {largura} equivale a {area}m² é necessário {quantidadeTinta}l de tinta para pintá-la')

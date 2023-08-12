#Faça um script que leia um valor em metros e o exiba
#convertido em centimetros e milimetros
metros = float(input('Informe a quantidade em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'{metros}m equivale a\n{centimetros:.0f}cm\n{milimetros:.0f}mm')

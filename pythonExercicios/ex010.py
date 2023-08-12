#Faça um script que leia quanto dinheiro a pessoa tem
#e mostre quantos Dólares ela pode comprar
DOLAR = 4.89
real = float(input('Informe quantos reais você tem R$ '))
valorConvertido = real / DOLAR
print(f'Com R$ {real} Reais você pode comprar US$ {valorConvertido:.2f} Dólares')

#Faça um script que leia um número e mostre o seu dobro, triplo e a raiz quadradra
num = int(input('Informe um número inteiro: '))
dobro = num * 2
triplo = num * 3
raizQuadrada = pow(num, (1/2))
#raizQuadrada = num ** (1/2)
print(f'Analisando o número: {num}\nDobro: {dobro}\nTriplo: {triplo}\nRaiz Quadrada: {raizQuadrada:.2f}')

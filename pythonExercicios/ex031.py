"""Faça um script que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longes"""
distanciaViagem = float(input('Informe a distância da viagem em Km: '))
if distanciaViagem <= 200:
    valorKm = 0.50
    valorPassagem = valorKm * distanciaViagem
    print(f'R$ {valorKm} por Km\nValor passagem R$ {valorPassagem:.2f}')
else:
    valorKm = 0.45
    valorPassagem = valorKm * distanciaViagem
    print(f'R$ {valorKm} por Km\nValor passagem R$ {valorPassagem:.2f}')
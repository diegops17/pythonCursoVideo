"""Faça um script que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite"""
velocidadeCarro = int(input('Informe a velocidade do carro: '))
VALOR_MULTA = 7
LIMITE_VELOCIDADE = 80
if velocidadeCarro > LIMITE_VELOCIDADE:
    velocidadeAcima = velocidadeCarro - LIMITE_VELOCIDADE
    multaPagar = velocidadeAcima * VALOR_MULTA
    print(f'Você está {velocidadeAcima}Km acima do limite, multa aplicada R$ {multaPagar:.2f}')
else:
    print('Parabéns você está na velocidade correta!')

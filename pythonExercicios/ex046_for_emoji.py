"""Faça um script que mostre uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre elas"""
from time import sleep
from emoji import emojize
for cont in range(10, 0-1, -1):
    print(cont)
    sleep(1)
print(emojize('FELIZ ANO NOVO!!! :sparkler:'))

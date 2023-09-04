"""Faça um script que calcule a soma entre todos os números impares que são multiplo
de três e que se encontram no intervalo de 1 até 500"""
soma = 0
for num in range(1, 500):
    if num % 2 != 0:
        if num % 3 == 0:
            soma += num
print(f'a soma dos números ímapres múltimpls de 3 é: {soma}')

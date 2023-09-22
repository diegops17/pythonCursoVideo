"""Faça uma tupla com 20 primeiros colocados no brasilerão, na ordem atual de colocação. Depois mostre:
A-Apenas os 5 primeiros, B-Os últimos 4 colocados, C-Uma lista em ordem alfabética,
D-Em que posição está o time da Corinthians"""
times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Flamengo', 'Fortaleza',
         'Atlético-MG', 'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo', 'Corinthians', 'Goiás', 'Bahia',
         'Santos', 'Vasco', 'América-MG', 'Coritiba')
print(f'Lista dos times do Brasileirão série A 2023: {times}')
print(f'Os cinco primeiros são: {times[:5]}')
print(f'Os quatro últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
time = str(input('Informe um time para saber a posição: ')).strip().upper()
ti = ' '
while time != ti:
    time = str(input('Opção incorreta!, Informe um time válido para saber a posição: ')).strip().upper()
    for t in times:
        ti = t.upper()
        if ti.upper() == time:
            break
for i, v in enumerate(times):
    #if v == 'Chapecoense':
    #    print(f'O {v} está na {i + 1}º posição')
    if v.upper() == time:
        print(f'O {v} está na {i + 1}º posição')
def notas(*num, situacao=False):
    dicionario = {}
    #maior = menor = soma = media = contador = 0
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['media'] = sum(num) / len(num)

    '''for n in num:
        soma += n

        if contador == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        contador += 1 
    dicionario['maior'] = maior
    dicionario['menor'] = menor

    if num == 0:
        num = 1
    media = soma / len(num)'''


    if dicionario['media'] <= 4:
        sit = 'RUIM'
    elif dicionario['media'] <= 6.5:
        sit = 'RAZOAVEL'
    else:
        sit = 'BOA'
    dicionario['media'] = f'{dicionario["media"]:.1f}'
    if situacao == True:
        dicionario['situacao'] = sit

    return dicionario


print(notas(8, 1, 3, 17, 6, situacao=True))
print(notas(8, 1, situacao=True))
print(notas(3, 1, 0.2, situacao=True))
print(notas(1, 3.2, 4.2, 5.7))


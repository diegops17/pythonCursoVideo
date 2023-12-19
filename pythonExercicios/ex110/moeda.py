def aumentar(num = 0, porcetagem = 0, mostrar = False):
    res = num + ((num * porcetagem) / 100)
    return res if mostrar is False else moeda(res)

def diminuir(num = 0, porcetagem = 0, mostrar = False):
    res = num - ((num * porcetagem) / 100)
    if mostrar == True:
        return moeda(res)
    else:
        return res


def dobro(num = 0, mostrar = False):
    res = num * 2
    if mostrar == True:
        return moeda(res)
    else:
        return res


def metade(num = 0, mostrar = False):
    res = num / 2
    if mostrar == True:
        return moeda(res)
    else:
        return res


def moeda(num = 0, mostrar = False):
    res = f'R$ {num:.2f}'.replace('.',',')
    return res

def resumo(num = 0, aumento = 1, reducao = 1):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço: {dobro(num, True)}')
    print(f'Metade do preço: {metade(num, True)}')
    print(f'{aumento}% de aumento {aumentar(num, aumento, True)}')
    print(f'{reducao}% de redução {diminuir(num, reducao, True)}')
    print('-'*30)
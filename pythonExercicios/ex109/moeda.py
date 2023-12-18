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


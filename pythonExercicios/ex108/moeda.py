def aumentar(num = 0, porcetagem = 0):
    res = num + ((num * porcetagem) / 100)
    return res

def diminuir(num = 0, porcetagem = 0):
    res = num - ((num * porcetagem) / 100)
    return res

def dobro(num = 0):
    res = num * 2
    return res

def metade(num = 0):
    res = num / 2
    return res

def moeda(num = 0):
    res = f'R$ {num:.2f}'.replace('.',',')
    return res


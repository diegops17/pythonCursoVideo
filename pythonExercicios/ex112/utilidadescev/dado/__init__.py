def leiaDinheiro(msg):
    flag = False
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31;40mERRO: {n} é um preço inválido!\033[m')
        else:
            flag = True
            return float(n)
        if flag:
            break    

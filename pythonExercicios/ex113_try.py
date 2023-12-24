def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31;40mERRO! Digite um número inteiro válido\033[m')
            continue
        else:
            return n    

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31;40mERRO! Digite um número inteiro válido\033[m')
            continue
        else:
            return n  

n1 = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
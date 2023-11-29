def leiaint(num):
    while True:
        if num.isnumeric():
            return num
            break
        else:
            print('Erro digite um número inteiro válido')
            num = leiaint(input('Digite um número: '))


num = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {num}')

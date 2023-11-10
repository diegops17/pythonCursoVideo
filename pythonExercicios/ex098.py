'''Faça um scr que tenha uma função chamada contador, qye recebe três parametros:
inicio, fim e passo e realiza a contagem, o programa tem que realizar três contagens
A-De 1 até 10, de um 1 em 1, B - de 10 até 0, de 2 em e, C - Uma contagem personalizada'''
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for n in range(inicio, fim, passo):
        print(f'{n}', end=' ')
    print('FIM!', end='\n')
    print('-=' * 20)

contador(1, 10, 1)
contador(10, -1, -2)

print('Agora é sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
"""Crie um script que tenha uma função fatorial() que recebe dois parâmetros: o primeiro que indique
o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de calculo fatorial"""


def fatorial(num, show=False):
    """
    ->Calcula o fatorial de um número.
    :param num: Número a ser calculado.
    :param show: opcional. Mostra ou não o cálculo.
    :return: O valor de fatorial de um número n.
    """
    fat = 1
    for n in range(num, 0, -1):
        fat *= n
        if show == True:
            print(n, end=' ')
            print('=' if (n == 1) else 'X', end=' ')
    print(fat)


#help(fatorial)
fatorial(5, True)
fatorial(5)


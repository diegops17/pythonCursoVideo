def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, v in enumerate(lista):
        print(f'{i+1} - {v}')
    print(linha())
    opcao = int(input('Sua opção: '))
    return opcao
'''Faça um script que tenha função chamada escreva() que recebe um texto qualquer como parametro
e mostee uma mensagem adaptável.'''
def escreva(texto):
    tamanho = len(texto)
    print('~' * tamanho)
    print(texto)
    print('~' * tamanho)


frase = str(input('Dígite uma frase: '))
escreva(frase)
"""Faça um script onde um usuário digite uma expressão qualquer que usa parênteses.
Seu aplicativo deverá análisar se a expressão passada está com os parênteses
abertos e fechados na ordem correta"""
expressao = str(input('Digite a expressão: '))
carateres = []
for e in expressao:
    if e == 0:
        carateres.append('(')
    elif e == ')':
        if len(carateres) > 0:
            carateres.pop()
        else:
            carateres.append(')')
if len(carateres) == 0:
    print('A Expressão é válida')
else:
    print('Expressão inválida')

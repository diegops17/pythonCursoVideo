"""Crie um script que tenha uma tupla com várias palavras (não usar acesntos). Depois disso,
você deve mostrar, para cada palavra, quais são suas vogais."""
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado','programador', 'futuro', 'diego')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for x in p:
        if x in 'aeiou':
            print(f'{x}', end=' ')

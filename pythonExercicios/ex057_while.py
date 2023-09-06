"""Faça um script que leia o sexo de uma pessoa, mas só aceite os fvalores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o sexo [M/F]: '))[0].upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Informação incorreta, digíte novamente!')
print('Fim')
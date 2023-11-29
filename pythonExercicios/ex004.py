"""Faça um script que leia algo pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações possíveis sobre ele."""
captura = input('Digite algo: ')
print(type(captura))
print(f'É númerico? {captura.isnumeric()}')
print(f'É letra? {captura.isalpha()}')
print(f'É número? {captura.isalnum()}')
print(f'É digito? {captura.isdigit()}')
print(f'É decimal? {captura.isdecimal()}')
print(f'É ? {captura.isidentifier()}')
print(f'Começa com minúsculo ? {captura.islower()}')
print(f'Começa com maiúsculo ? {captura.isupper()}')
print(f'É ? {captura.isprintable()}')
print(f'É ? {captura.isspace()}')
print(f'É ? {captura.istitle()}')
print(f'É ? {captura.isascii()}')





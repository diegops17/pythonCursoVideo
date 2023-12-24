import requests

URL = 'https://pudim.com.br/'

try:
    retorno = requests.get(URL).status_code
    if retorno == 200:
        print('Consegui acessar o site pudim')
except:
    print('O site pudim não está acessivel no momento.')

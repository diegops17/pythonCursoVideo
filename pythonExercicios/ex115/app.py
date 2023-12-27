from lib.visual import *
from lib.arquivo import *
from time import sleep

arquivo = 'base_dados.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

#cabecalho('SISTEMA DE ARQUIVO')
while True:
    opcao = menu(['LISTAR USUÁRIOS', 'CADASTRAR USUÁRIO', 'SAIR'])

    if opcao == 1:
        ler_arquivo(arquivo)
    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadatrar(arquivo, nome, idade)
    elif opcao == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        cabecalho('Erro, digite uma opção válida!')
    sleep(2)


from lib.visual import *

def arquivo_existe(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('ERRO, Não foi possível criar arquivo')
    else:
        return print(f'Arquivo {nome_arquivo} criado com sucesso.')


def ler_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadatrar(nome_arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Erro ao tentar abrir arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n') 
        except:
            print('Erro ao tenatar salvar dados no aruivo .txt')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
        



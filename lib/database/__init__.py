# -*- coding: UTF-8 -*-
from EstacionaMentos.lib.interface import *
from datetime import datetime

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
#PRONTO

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
#PRONTO


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        dados = []
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            dados.append(dado)
        a.close()
        return dados
#PRONTO


def cadastrar(arq, plac='desconhecida'):
    chegada = datetime.now()
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{plac};{chegada}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Novo registro da placa {plac} adicionada às {chegada.strftime("%H-%M")}')
            a.close()
#PRONTO



def busca(lista, valor):
    for i in range(len(lista)):
        if lista[i][0] == valor:
            return lista[i][1]
    return None
#PRONTO

def baixa(arq, plac='desconhecida'):
    encerr = datetime.now()
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        dados = lerArquivo(arq)
        h_placa_chegou = busca(dados, plac) #tenho agora a hora que o carro chegou
        delta = encerr - datetime.fromisoformat(h_placa_chegou)
        tout = int((delta.total_seconds()) / 60)

        valor = 0
        if tout < 15:
            valor = 0
        elif tout < 60:
            valor = 2
        elif tout < 120:
            valor = 4
        elif tout >= 120:
            valor = 4 + (tout - 120) / 60
        a.close()
        return valor, tout
#PRONTO


def faturamento(arq, valor):
    saida = datetime.now()
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'R${valor};{saida}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            print(f'Valor {valor} adicionado ao total às {saida.strftime("%H-%M")}')
            a.close()



def valorArrec(baixas):
    try:
        a = open(baixas, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        dados = []
        soma = 0
        total = 0
        for linha in a:
            dado = linha.split(';')
            for n in dado[0]:
                if n.isdigit():
                    total += int(n)

        a.close()
        return total
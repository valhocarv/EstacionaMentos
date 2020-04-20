# -*- coding: UTF-8 -*-
def linha(tam=50):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido')
            continue
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'{i} - {item}')
        i += 1
    print(linha())
    opt = leiaInt('Sua Opção: ')
    return opt
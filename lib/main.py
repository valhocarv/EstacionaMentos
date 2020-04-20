# -*- coding: UTF-8 -*-
from datetime import datetime
from time import sleep

from EstacionaMentos.lib.database import *

data_hoje = datetime.now()
data_hoje_br = data_hoje.strftime('%d-%m-%Y')

arq = f'Base_de_Dados-EstacionaMentos_{data_hoje_br}.txt'
baixas = f'Arrecadacao-EstacionaMentos{data_hoje_br}.txt'


if not arquivoExiste(arq):
    print('Base de Dados não encontrada')
    criarArquivo(arq)

if not arquivoExiste(baixas):
    print('Arquivo de baixas não encontrado')
    criarArquivo(baixas)

cabeçalho('Bem vindo ao EstacionaMentos System')

while True:
    resposta = menu(['Adicionar carro ao estacionamento', 'Baixa por saída (Tempo e Valor)','Analisar todo o valor arrecadado', 'Fechar Sistema'])
    #add carro
    if resposta == 1:
        cabeçalho('NOVA ENTRADA')
        placa = str(input('Placa: '))
        cadastrar(arq, placa)

    #baixa do carro
    elif resposta == 2:
        cabeçalho('BAIXA (TEMPO E VALOR)')
        placa = str(input('Placa: '))
        valor, tout = baixa(arq, placa)
        print(f"""{linha()}\n RECIBO:
Placa: {placa}
Tempo: {tout}
Valor a ser pago: R${valor}
{linha()}
        """)
        if int(input('Qualquer valor, caso não seja pago digite 0: ')) != 0:
            faturamento(baixas, valor)


    #entrega o valor arrecadado no dia
    elif resposta == 3:
        cabeçalho('ARRECADAÇÃO TOTAL DO DIA')
        total = valorArrec(baixas)
        print(linha())
        print(f'Faturamento TOTAL do dia até o momento: R${total},00'.center(50))
        print(linha())

    #fecha o sistema
    elif resposta == 4:
        print('Saindo do sistema!')
        break
    else:
        print('ERRO: por favor, digite uma opção válida')
    sleep(1.5)

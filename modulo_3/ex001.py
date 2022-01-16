"""
    Neste exercício você deve criar um programa que abra o arquivo
    "alunos.csv" e imprima o conteúdo do arquivo linha a linha.

    Note que esse é o primeiro exercício de uma sequência, então o seu código
    pode ser reaproveitado nos exercícios seguintes. Dito isso, a recomendação é
    usar a biblioteca CSV para ler o arquivo mesmo que não seja realmente
    necessário para esse primeiro item.
"""

import csv
import sys


def ler_csv(local_arq, delimit=','):
    local_arq = local_arq.strip()

    if '.csv' not in local_arq.lower():
        sys.exit('O arquivo não é um CSV!')

    conteudo = []

    try:
        with open(local_arq, 'r', encoding='utf-8') as arq:
            reader = csv.reader(arq, delimiter=delimit)

            for linha in reader:
                conteudo.append(linha)

    except FileNotFoundError:
        nome_arq = local_arq.split('/')[-1]
        sys.exit(f'Arquivo {nome_arq} não encontrado!')

    return conteudo

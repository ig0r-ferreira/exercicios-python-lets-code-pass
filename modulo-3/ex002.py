"""
    Para o segundo exercício, você deve criar um programa que realize uma
    cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado
    "alunos_copia.csv".

    Novamente, aqui você também não precisa utilizar a biblioteca CSV mas se
    usar, seu código pode ser reutilizado na próxima questão sem muitas
    modificações.
"""

import csv
from ex001 import ler_csv


def copiar_csv(local_arq, nome_copia='default'):
    local_arq = local_arq.strip()
    nome_copia = nome_copia.strip()

    nome_arq = local_arq.split('/')[-1]

    if nome_copia == 'default':
        nome_copia = nome_arq[:-4] + '_copia'
    else:
        nome_copia = nome_copia.split('.')[0]

    local_copia = local_arq.replace(nome_arq[:-4], nome_copia)

    conteudo = ler_csv(local_arq)

    with open(local_copia, 'w', encoding='utf-8', newline='') as copia_arq:
        writer = csv.writer(copia_arq)
        writer.writerows(conteudo)

    return local_copia
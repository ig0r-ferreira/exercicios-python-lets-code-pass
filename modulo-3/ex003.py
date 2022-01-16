"""
    Finalmente chegamos ao último exercício dessa sequência relacionada à
    manipulação de arquivos.

    Neste exercício você deve criar um novo arquivo chamado
    "alunos_media.csv". Esse novo arquivo é uma cópia de "alunos.csv" porém
    com uma coluna a mais chamada "Média" que vai abrigar os valores das
    médias das provas de cada aluno da lista.

    Se você utilizou a biblioteca CSV para realizar os dois primeiros exercícios,
    muito será reaproveitado aqui. A biblioteca CSV permite a interpretação de
    cada linha como listas, que são fáceis de manipular.
"""

import csv

from ex002 import copiar_csv, ler_csv

local_arq = 'alunos.csv'
nome_copia = 'alunos_media.csv'

local_copia = copiar_csv(local_arq, nome_copia)
conteudo = ler_csv(local_copia)

colunas_notas = []

for linha in range(0, len(conteudo)):
    if linha == 0:
        conteudo[linha].append('Media')
        colunas_notas = [index for index, coluna in enumerate(conteudo[linha]) if 'Prova' in coluna]
        continue

    soma = media = 0

    for coluna in colunas_notas:
        soma += float(conteudo[linha][coluna])

    media = soma / len(colunas_notas)
    media = '{:.1f}'.format(media)

    conteudo[linha].append(media)

with open(local_copia, 'w', encoding='utf-8', newline='') as copia_arq:
    writer = csv.writer(copia_arq)
    writer.writerows(conteudo)

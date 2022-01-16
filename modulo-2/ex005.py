"""
    Imprima as chaves seguidas dos seus valores para dicionário criado no
    exercício anterior.

    Exemplo:
        Janeiro - 31
        Fevereiro - 28
        Março - 31
        Etc...
"""


from ex004 import duracao_meses

for mes, dias in duracao_meses().items():
    print(mes + ' - ' + str(dias))

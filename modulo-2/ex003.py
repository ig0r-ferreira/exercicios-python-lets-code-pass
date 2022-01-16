"""
    Faça uma função que recebe duas listas e retorna a soma item a item dessas
    listas.

    Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
    retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""


def somar_listas(lista1, lista2):
    nova_lista = []
    tamanho_lista1 = len(lista1)
    tamanho_lista2 = len(lista2)

    # Se o tamanho da lista1 for maior que o da lista2 incrementa a lista2 com zeros
    # até atingir o tamanho da lista1
    if tamanho_lista1 > tamanho_lista2:
        lista2 = lista2 + [0] * (tamanho_lista1 - tamanho_lista2)
    # Se o tamanho da lista1 for menor que o da lista2 incrementa a lista1 com zeros
    # até atingir o tamanho da lista2
    elif tamanho_lista1 < tamanho_lista2:
        lista1 = lista1 + [0] * (tamanho_lista2 - tamanho_lista1)
        tamanho_lista1 = len(lista1)

    for i in range(tamanho_lista1):
        nova_lista.append(lista1[i] + lista2[i])

    return nova_lista


lista1 = [1, 4, 3, 8, 7]
lista2 = [3, 5, 1]

print(somar_listas(lista1, lista2))

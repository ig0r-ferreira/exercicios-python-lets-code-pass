"""
    Faça uma função que recebe duas listas e retorna a soma item a item dessas
    listas.

    Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
    retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""


def somar_listas(l1, l2):
    nova_lista = []
    tamanho_l1 = len(l1)
    tamanho_l2 = len(l2)

    # Se o tamanho da lista1 for maior que o da lista2 incrementa a lista2 com zeros
    # até atingir o tamanho da lista1
    if tamanho_l1 > tamanho_l2:
        l2 = l2 + [0] * (tamanho_l1 - tamanho_l2)
    # Se o tamanho da lista1 for menor que o da lista2 incrementa a lista1 com zeros
    # até atingir o tamanho da lista2
    elif tamanho_l1 < tamanho_l2:
        l1 = l1 + [0] * (tamanho_l2 - tamanho_l1)
        tamanho_l1 = len(l1)

    for i in range(tamanho_l1):
        nova_lista.append(l1[i] + l2[i])

    return nova_lista


lista1 = [1, 4, 3, 8, 7]
lista2 = [3, 5, 1]

print(somar_listas(lista1, lista2))

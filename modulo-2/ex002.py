"""
    Faça um programa que peça para o usuário digitar uma palavra e imprima
    cada letra em uma linha.
"""

while True:
    palavra = input('Digite uma palavra: ').strip()

    if palavra.isalpha():
        break

    print('\033[1;31mErro: Palavra inválida! Tente novamente.\033[m')

for letra in palavra:
    print(letra)

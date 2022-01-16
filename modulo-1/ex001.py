"""
    Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
    programa deve imprimir a mensagem “O novo valor é [valor]”
"""


while True:
    try:
        valor = float(input('\nDigite um valor: R$ ').strip())
    except ValueError:
        print('Valor inválido! Tente novamente.')
    else:
        print(f'O novo valor é R$ {valor * 0.85:.2f}.')
        break

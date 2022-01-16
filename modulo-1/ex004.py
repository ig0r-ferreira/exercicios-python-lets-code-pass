"""
    Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
"""


print(f'\n\033[1m{" Tabuada do 9 ":-^30}\033[m')

for i in range(1, 11):
    print(f'{f"9 x {i:>2} = {9 * i:>2}":^30}')

print('\033[1m' + ('-' * 30) + '\033[m')

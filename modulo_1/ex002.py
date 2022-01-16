"""
    Faça um programa que leia a validade das informações:
      a. Idade: entre 0 e 150;
      b. Salário: maior que 0;
      c. Sexo: M, F ou Outro;

    O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""

abre_negrito = '\033[31;1m'
fecha_negrito = '\033[m'


while True:
    try:
        idade = int(input('Informe a sua idade: ').strip())
    except ValueError:
        print(f'{abre_negrito}Idade inválida! Tente novamente.{fecha_negrito}')
    else:
        if 0 < idade < 150:
            break
        else:
            print(f'{abre_negrito}Idade inválida! Tente novamente.{fecha_negrito}')

while True:
    try:
        salario = float(input('Informe o seu salário: R$ ').strip())
    except ValueError:
        print(f'{abre_negrito}Salário inválido! Tente novamente.{fecha_negrito}')
    else:
        if salario > 0:
            break
        else:
            print(f'{abre_negrito}Salário inválido! Tente novamente.{fecha_negrito}')

while True:
    try:
        sexo = input(f'Informe o seu sexo {abre_negrito}'
                     f'(M - Masculino, F - Feminino, O - Outro){fecha_negrito}: ').strip().upper()
    except ValueError:
        print(f'{abre_negrito}Sexo inválido! Tente novamente.{fecha_negrito}')
    else:
        if sexo == 'M' or sexo == 'F' or sexo == 'O':
            break
        else:
            print(f'{abre_negrito}Sexo inválido! Tente novamente.{fecha_negrito}')

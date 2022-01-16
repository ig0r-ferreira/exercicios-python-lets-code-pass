"""
Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:

  a. Mora perto da vítima?
  b. Já trabalhou com a vítima?
  c. Telefonou para a vítima?
  d. Esteve no local do crime?
  e. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.
"""


print(f'\n\033[1m{" PROCESSO INTERROGATÓRIO ":=^50}\033[m')

while True:
    try:
        total_interrogatorios = int(input('\nQuantas pessoas serão interrogadas? ').strip())
    except ValueError:
        print('\033[1;31mErro: Informe um número inteiro!\033[m')
    else:
        break


perguntas = [
    'Mora perto da vítima?',
    'Já trabalhou com a vítima?',
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Devia para a vítima?'
]


for i in range(0, total_interrogatorios):

    questionario = []

    print(f'\n\033[1m{str(i + 1) + "º INTERROGADO"}\033[m')

    while True:
        interrogado = input('\nNome: ').strip().upper()

        if not interrogado.replace(' ', '').isalpha():
            print('\033[31;1mErro: Nome inválido! Tente novamente.\033[m')
        else:
            break

    print()

    for pergunta in perguntas:
        while True:
            resposta = input('=> ' + pergunta + ' [S/N]: ').upper()
            if resposta == 'S' or resposta == 'N':
                break
            else:
                print('\033[31;1mErro: Resposta inválida! Tente novamente.\033[m')

        questionario.append({
            'pergunta': pergunta,
            'resposta': resposta
        })

    pontos = len([q for q in questionario if q['resposta'] == 'S'])

    if pontos == 5:
        resultado = 'ASSASSINO'
    elif 5 > pontos > 2:
        resultado = 'CÚMPLICE'
    elif pontos == 2:
        resultado = 'SUSPEITO COMUM'
    else:
        resultado = 'SEM ENVOLVIMENTO'

    print(f'\n\033[1m'
          f'NOME DO INTERROGADO: {interrogado}\n'
          f'RESULTADO DA ANÁLISE: {resultado}!'
          f'\033[m')

print(f'\n\033[1m{" FIM DO INTERROGATÓRIO ":=^50}\033[m')

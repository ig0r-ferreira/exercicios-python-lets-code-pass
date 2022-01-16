"""
      Faça um programa que olhe todos os itens de uma lista e diga quantos deles
      são pares.
"""


numeros = list(range(10))

pares = [num for num in numeros if num % 2 == 0]

print(f'Lista: {numeros}\n'
      f'Há {len(pares)} numéros pares na lista.')

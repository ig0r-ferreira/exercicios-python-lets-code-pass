"""
    Crie um dicionário cujas chaves são os meses do ano e os valores são a
    duração (em dias) de cada mês.
"""


from calendar import monthrange
from datetime import date


def duracao_meses():
    meses_em_dias = {}
    meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', \
            'Setembro', 'Outubro', 'Novembro', 'Dezembro'

    ano_atual = date.today().year

    for cod_mes, mes in enumerate(meses):
        meses_em_dias[mes] = monthrange(ano_atual, cod_mes + 1)[1]

    return meses_em_dias

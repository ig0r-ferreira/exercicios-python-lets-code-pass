"""
    Você conhece Star Wars? Se trata, obviamente, da famosa saga espacial
    criada por George Lucas em 1977 e que deu origem a símbolos do cinema e
    da cultura pop com o imponente vilão Darth Vader ou o simpático robô
    R2-D2. A ideia desse exercício é justamente extrair informações do
    personagem Darth Vader através de uma API de Star Wars chamada SWAPI.

    Utilize a URL "https://swapi.dev/api/people/4/" para fazer a requisição dos
    dados de Darth Vader e extraia as informações "name" (nome), "height"
    (altura), "mass" (massa) e "birth_year" (ano de nascimento) e imprima cada
    dado em uma linha.

    Dica: caso não se lembre de como fazer isso, assista novamente a aula sobre
    API porque o exemplo da aula pode te ajudar.
"""

import requests

url = 'https://swapi.dev/api/people/4/'

try:
    resp = requests.get(url)
except requests.exceptions.RequestException:
    print(f'Não foi possível acessar o site {url}.')
else:
    if resp.status_code == 200:
        darth_vader = resp.json()
        print(f'Nome: {darth_vader["name"]}')
        print(f'Altura: {darth_vader["height"]}')
        print(f'Massa: {darth_vader["mass"]}')
        print(f'Ano de nascimento: {darth_vader["birth_year"]}')
    else:
        print(f'Não foi possível acessar o site {url}.')

"""
Em 2019 surgiram os primeiros casos de COVID-19 que se alastrou pelo
mundo resultando numa pandemia. A proposta deste exercício é utilizar
uma API com informações de COVID-19 do mundo todo desde o início da
proliferação e descobrir que dia o Brasil confirmou o primeiro caso de
Coronavírus.

Para fazer isso, utilize a URL "https://api.covid19api.com/country/brazil" em seu
código. Ela retorna uma lista de dicionários, onde cada dicionário traz
informações através das chaves:

"ID", "Country", "CountryCode", "Province", "City",
"CityCode","Lat","Lon","Confirmed","Deaths", "Recovered", "Active" e "Date".

Utilize essas informações e retorne a data em que o Brasil confirmou o
primeiro caso de COVID.
"""

import requests
from datetime import datetime

url = 'https://api.covid19api.com/country/brazil'

try:
    resp = requests.get(url)
except requests.exceptions.RequestException:
    print(f'Não foi possível acessar o site {url}.')
else:
    if resp.status_code == 200:
        dados_covid = resp.json()
        dados_covid = sorted(dados_covid, key=lambda reg: reg['Date'])

        caso_1 = next(reg for reg in dados_covid if int(reg['Confirmed']) > 0)
        data_caso_1 = caso_1['Date']
        data_caso_1 = datetime.strptime(data_caso_1, '%Y-%m-%dT%H:%M:%SZ').date().strftime('%d/%m/%Y')

        print(f'O primeiro caso de Covid confirmado no Brasil foi em {data_caso_1}.')
    else:
        print(f'Não foi possível acessar o site {url}.')

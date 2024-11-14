import requests

url = "https://restcountries.com/v3.1/name/russia"

response = requests.get(url)

data = response.json()

country = data[0]
country_name = country['name']['common']
capital = country.get('capital')[0]
population = country.get('population')
area = country.get('area')
languages = ", ".join(country['languages'].values())
currencies = list(country.get('currencies', {}).values())
currencies = currencies[0]['name']
flag_url = country['flags']['png']

html_content = f"""
<html>
  <head>
    <title>Информация о стране: {country_name}</title>
  </head>
  <body>
    <h1>{country_name}</h1>
    <p><strong>Столица:</strong> {capital}</p>
    <p><strong>Население:</strong> {population}</p>
    <p><strong>Площадь:</strong> {area} км²</p>
    <p><strong>Языки:</strong> {languages}</p>
    <p><strong>Валюта:</strong> {currencies}</p>
    <img src="{flag_url}" alt="Флаг {country_name}" width="200">
  </body>
</html>
"""

with open("six_task.html", "w", encoding="utf-8") as f:
    f.write(html_content)


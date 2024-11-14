import requests

def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    return response.json()


def extract_country_info(data):
    country = data[0]
    country_name = country['name']['common']
    capital = country.get('capital')[0]
    population = country.get('population')
    area = country.get('area')
    languages = ", ".join(country['languages'].values())
    currencies = list(country.get('currencies', {}).values())
    currencies = currencies[0]['name']
    flag_url = country['flags']['png']

    return country_name, capital, population, area, languages, currencies, flag_url


def generate_html(country_name, capital, population, area, languages, currencies, flag_url):
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
    return html_content


def save_html_to_file(file_name, html_content):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_content)

country_name = "russia"
output_file = "six_task.html"

country_data = get_country_data(country_name)
country_name, capital, population, area, languages, currencies, flag_url = extract_country_info(country_data)
html_content = generate_html(country_name, capital, population, area, languages, currencies, flag_url)
save_html_to_file(output_file, html_content)



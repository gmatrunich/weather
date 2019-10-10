import requests

CITIES = ['Лондон', 'Шереметьево', 'Череповец']
URL_TEMPLATE = 'http://wttr.in/{}'
PAYLOAD = {'nTqmF': '', 'lang': 'ru'}


def weather_in_the_city(city):
    url = URL_TEMPLATE.format(city)
    response = requests.get(url, params=PAYLOAD)
    response.raise_for_status()
    return print(response.text)


try:
    for city in CITIES:
        weather_in_the_city(city)
except requests.exceptions.HTTPError as error:
    exit("Запрос к серверу завершился неудачно\n{0}".format(error))

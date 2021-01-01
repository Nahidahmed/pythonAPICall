import requests
import json


# call a simple API and extract few fields from the JSON response
def simpleApiCall():
    baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
    parameters = {'upc': '885909950805'}
    response = requests.get(baseUrl, params=parameters)

    content = response.content
    info = json.loads(content)
    item = info['items']
    iteminfo = item[0]
    title = iteminfo['title']
    brand = iteminfo['brand']

    print(f'Title: {title}')
    print(f'Brand: {brand}')


def openweather():
    baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
    parameters = {'q': 'Hyderabad,India', 'appid': 'e4daffc0cb3ee4610fee9d74427c51fb'}
    response = requests.get(baseUrl, params=parameters)
    content = response.content
    info = json.loads(content)
    print(info)

openweather()

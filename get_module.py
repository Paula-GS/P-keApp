import requests
import json


def get_info(url):
    return json.loads(requests.get(url).text) #este agarra la información y la trae toda de una vez

if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon/charmander'
    print(get_info(url))

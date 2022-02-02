import sys
import json
import requests
import poke_validation as pv
from get_module import get_info
import random


#valida el nombre ingresado por el ususario
name = input("Introduzca el nombre del Pokémon a procesar: ")

name = pv.validate(name)

# Extrae el número del Pókemon
url_base = f"https://pokeapi.co/api/v2/pokemon/{name}"

data_base = get_info(url_base)

id_n = data_base["id"]

#print(id_n)


stats = data_base["stats"]

indicadores = []
for item in stats:
    indicadores.append(item["base_stat"])

print(indicadores)


"""
pok_hp, ataque, defensa, sp_ataque, sp_defensa, velocidad = indicadores

pok_img = data_base['sprites']['front_default']

#print(pok_ve)

url_previa = f"https://pokeapi.co/api/v2/pokemon-species/{nombre}"

data_etapa_previa = get_info(url_previa)

#print(data_etapa_previa['evolves_from_species'])

pok_etapa_previa = data_etapa_previa['evolves_from_species']
if pok_etapa_previa is not None:
    pok_etapa_previa = pok_etapa_previa["name"]
else:
    pok_etapa_previa = ""

#print(pok_etapa_previa)

tipos_lista = data_base["types"]

tipos = []
for item in tipos_lista:
    tipos.append(item["type"]["name"])

### Procesamiento del comentario sobre el pokemon en español

comentarios = data_etapa_previa["flavor_text_entries"]
"""

"""
filtro = {k:v for k,v in diccionario.items() if v > umbral}

filtro = {}
for k,v in diccionario.items():
	if v > umbral:
		filtro[k] = v
"""

"""
filtro = [item["flavor_text"].replace("\n"," ") for item in comentarios if item["language"]["name"] == 'es']

pok_comentario = random.choice(filtro)

#print(pok_comentario)
"""
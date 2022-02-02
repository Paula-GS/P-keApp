import sys
import json
import requests
import poke_validation as pv
from get_module import get_info
import random

#INGRESA EL NOMBRE DEL POKÉMON
name = input("Introduzca el nombre del pokémon a procesar: ") #el que ingresa el usuario, no necesariamente bien escrito

name = pv.validate(name) #el que regresa, que sí está bien escrito

#print(name)

#TRAE TODA LA INFORMACIÓN DISPONIBLE
url_base = f"https://pokeapi.co/api/v2/pokemon/{name}"

data_base = get_info(url_base)

id_n = data_base["id"] #aquí estoy llamando el punto específico de la información que necesito

stats = data_base["stats"] #elige todo el item stats y lo trae. 

indicadores = []  #recuerda que los corchetes te dicen que es una lista
for item in stats: #esto recorre la lista, tomando cada pedazo en una iteración.
    indicadores.append(item["base_stat"]) #en cada elemento se consulta el base stat

#print(indicadores)

pok_hp, ataque, defensa, sp_ataque, sp_defensa, velocidad = indicadores #asigna cada elemento a su equivalente en la lista extraída de la api

img_url = data_base["sprites"]["other"]["official-artwork"]["front_default"]  #pide la imagen


#INFO ETAPA PREVIA
url_eprevia = f"https://pokeapi.co/api/v2/pokemon-species/{id_n}" #que no se te olvide la f, otherwise va a crashear feo

data_eprevia = get_info(url_eprevia)

etapa_previa = data_eprevia["evolves_from_species"] #toma la lista
if etapa_previa is not None:
    etapa_previa = etapa_previa["name"] #si existe nombre lo indica
else:
    etapa_previa = "Este pokémon no tiene una etapa previa" #si no lo tiene, imprime el mensaje

#AGREGAMOS EL TIPO DE POKÉMON
tipos_lista = data_base["types"]

tipos = []
for item in tipos_lista:
    tipos.append(item["type"]["name"])

#print(tipos)

#COMENTARIO ALEATORIO DEL POKEMON EN ESPAÑOL
comentarios = data_eprevia["flavor_text_entries"] #trae todos los comentarios en todos los idiomas

filtro = [item["flavor_text"].replace("\n", " ") for item in comentarios if item["language"]["name"] == "es"] #trae solo los comentarops en español, sacando los saltos de línea

p_comentario = random.choice(filtro) #toma un comentario y lo elige para ser impreso

#EFECTIVO CONTRA
url_damage = f"https://pokeapi.co/api/v2/type/fire/"
data_damage = get_info(url_damage)


super_efectivo = data_damage["damage_relations"]["double_damage_from"] #aquí vas, llegas a extraer esta información pero no puedes seguir más alla

print(super_efectivo)

'''
stats = data_base["stats"] #elige todo el item stats y lo trae. 

indicadores = []  #recuerda que los corchetes te dicen que es una lista
for item in stats: #esto recorre la lista, tomando cada pedazo en una iteración.
    indicadores.append(item["base_stat"]) #en cada elemento se consulta el base stat

'''

def traduccion(lista): #span
    diccionario_ing_es = {
      "normal": "Normal", "fire": "Fuego", "flying": "Volador",
      "steel": "Acero", "water": "Agua", "electric": "Eléctrico",
      "grass": "Planta", "ice": "Hielo", "fighting": "Lucha",
      "poison": "Veneno", "ground": "Tierra", "psychic": "Psíquico",
      "bug": "Bicho", "rock": "Roca", "ghost": "Fantasma",
      "dragon": "Dragón", "dark": "Siniestro", "steel": "Acero",
      "fairy": "Hada" }

    span_str = ""
    for item in lista:
        item_es = diccionario_ing_es.get(item)
        span_str = span_str + f'<span class=" {item}">{item_es}</span>'
    return span_str

span_tipo = (traduccion(tipos))
#print(traduccion(tipos))

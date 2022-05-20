import sys
import json
import requests
from get_module import get_info
import random

#TRAE TODA LA INFORMACIÓN DISPONIBLE
def Nombre(name):
    url_base = f"https://pokeapi.co/api/v2/pokemon/{name}"
    return get_info(url_base)

#STATS

def name(data_base):
    respuesta = data_base["name"]
    return respuesta

def id_n(data_base):
    respuesta = str(data_base["id"])
    return respuesta

def hp(data_base):
    respuesta = data_base["stats"][0]["base_stat"]
    return respuesta

def ataque(data_base):
    respuesta = data_base["stats"][1]["base_stat"]
    return respuesta

def defensa(data_base):
    respuesta = data_base["stats"][2]["base_stat"]
    return respuesta

def sp_ataque(data_base):
    respuesta = data_base["stats"][3]["base_stat"]
    return respuesta

def sp_defensa(data_base):
    respuesta = data_base["stats"][4]["base_stat"]
    return respuesta

def velocidad(data_base):
    respuesta = data_base["stats"][5]["base_stat"]
    return respuesta

def img_url(data_base):
    respuesta = data_base["sprites"]["other"]["official-artwork"]["front_default"]
    return respuesta

#AGREGAMOS EL TIPO DE POKÉMON
def tipos_url(data_base):
    tipos = []
    for item in data_base["types"]:
        tipos.append(item["type"]["url"])
    respuesta = tipos
    return respuesta

def tipos_nombre(data_base):
    trads = []
    for item in data_base["types"]:
        trads.append(item["type"]["name"])
    respuesta = trads
    return respuesta

#TALLA Y PESO
def talla(data_base):
    respuesta = (data_base["height"])/10
    return respuesta

def peso(data_base):
    respuesta = (data_base["weight"])/10
    return respuesta

#INFO ETAPA PREVIA
def Species(id_n):
    url_base = f"https://pokeapi.co/api/v2/pokemon-species/{id_n}" 
    return get_info(url_base)


def etapa_previa(data_species):
    etapa_previa = data_species["evolves_from_species"] #toma la lista
    if etapa_previa is not None:
        etapa_previa = etapa_previa["name"].capitalize() #si existe nombre lo indica
    else:
        etapa_previa = "Este pokémon no tiene una etapa previa" #si no lo tiene, imprime el mensaje
    return etapa_previa

#TIPO ESPECIAL
def baby(data_species):
    baby = data_species["is_baby"]
    if baby == True:
        baybee = '<span class="label other">Bebé</span>'
    else: 
        baybee = ""
    return baybee

def legendary(data_species):
    legendary = data_species["is_legendary"]
    if legendary == True:
        legend = '<span class="label other">Legendario</span>'
    else: 
        legend = ""
    return legend

def mythical(data_species): 
    mythical = data_species["is_mythical"]
    if mythical == True:
        myth = '<span class="label other">Mítico</span>'
    else: 
        myth = ""
    return myth


#COMENTARIO ALEATORIO DEL POKEMON EN ESPAÑOL
def comentarios(data_species):
    comentarios = data_species["flavor_text_entries"] 
    filtro = [item["flavor_text"].replace("\n", " ") for item in comentarios if item["language"]["name"] == "es"]
    p_comentario = random.choice(filtro)
    return p_comentario



if __name__ == '__main__':
    data_base = Nombre("charizard")
    print(id_n(data_base))
    print(name(data_base))
    print(hp(data_base))
    print(ataque(data_base))
    print(defensa(data_base))
    print(sp_ataque(data_base))
    print(sp_defensa(data_base))
    print(velocidad(data_base))
    print(tipos_url(data_base))
    print(tipos_nombre(data_base))
    print(peso(data_base))
    print(talla(data_base))
    data_species = Species(id_n(data_base))
    print(etapa_previa(data_species))
    print(baby(data_species))
    print(legendary(data_species))
    print(mythical(data_species))
    print(comentarios(data_species))

import sys
import json
import requests
import poke_validation as pv
from get_module import get_info
from informacion_condensada import Nombre, tipos_url, tipos_nombre


def Damage(data_base):
    data_danho = []
    for item in tipos_url(data_base):
        data_danho.append(get_info(item))
    return data_danho

#Efectivo contra
def efectivo_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["double_damage_to"]
        efectivo_contra = {elemento['name'] for elemento in danho} #al crear un set por comprehension no se necesita defirnir antes
    return efectivo_contra


#Debil contra
def debil_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["double_damage_from"]
        debil_contra = {elemento['name'] for elemento in danho} #al crear un set por comprehension no se necesita defirnir antes
    return debil_contra

#Resistente contra
def resistente_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["half_damage_from"]
        resistente_contra = {elemento['name'] for elemento in danho}
    return resistente_contra

#Poco eficaz contra
def peficaz_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["half_damage_to"]
        peficaz_contra = {elemento['name'] for elemento in danho}
    return peficaz_contra


#Inmune contra
def inmune_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["no_damage_from"]
        inmune_contra = {elemento['name'] for elemento in danho}
    return inmune_contra


#Inefectivo contra 
def inefectivo_contra(biblio_tipos):
    danho = []
    for item in biblio_tipos:
        danho += item["damage_relations"]["no_damage_to"]
        inefectivo_contra = {elemento['name'] for elemento in danho}
    return inefectivo_contra


if __name__ == '__main__':
    data_base = Nombre("pikachu")
    biblio_tipos = Damage(data_base)
    print(efectivo_contra(biblio_tipos))
    print(debil_contra(biblio_tipos))
    print(resistente_contra(biblio_tipos))
    print(poco_eficaz_contra(biblio_tipos))
    print(inmune_contra(biblio_tipos))
    print(inefectivo_contra(biblio_tipos))

from damage import *
from informacion_condensada import tipos_nombre


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
        item_es = diccionario_ing_es[item]
        span_str = span_str + f'<span class="label {item}">{item_es}</span>'
    return span_str
 

def span_tipo(data_base):
    span_tipo = (traduccion(tipos_nombre(data_base)))
    return span_tipo

def span_efectivo(biblio_tipos):
    span_efectivo = (traduccion(efectivo_contra(biblio_tipos)))
    return span_efectivo

def span_debil(biblio_tipos):
    span_debil = (traduccion(debil_contra(biblio_tipos)))
    return span_debil

def span_resistente(biblio_tipos):
    span_resistente = (traduccion(resistente_contra(biblio_tipos)))
    return span_resistente

def span_peficaz(biblio_tipos):
    span_peficaz = (traduccion(peficaz_contra(biblio_tipos)))
    return span_peficaz

def span_inmune(biblio_tipos):
    span_inmune = (traduccion(inmune_contra(biblio_tipos)))
    return span_inmune

def span_ineficaz(biblio_tipos):
    span_ineficaz = (traduccion(inefectivo_contra(biblio_tipos)))
    return span_ineficaz

if __name__ == '__main__':
    data_base = Nombre("charizard")
    biblio_tipos = Damage(data_base)
    print(span_tipo(data_base))
    print(span_efectivo(biblio_tipos))
    print(span_debil(biblio_tipos))
    print(span_resistente(biblio_tipos))
    print(span_peficaz(biblio_tipos))
    print(span_inmune(biblio_tipos))
    print(span_ineficaz(biblio_tipos))
  
import webbrowser
import os
import time
from build_pokemon_html import crea_pokedex
from informacion_condensada import name

def show_pics(html, nombre):
    with open(f'{nombre}.html','w', encoding="utf-8") as f:
        f.write(html)
    print('La información de la Poke-Dex se mostrará en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')

if __name__ == '__main__':
    nombre = "mew"
    html = crea_pokedex(nombre)
    show_pics(html, nombre) 
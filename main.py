from validar import confirmar
from time import sleep
import poke_validation as pv
import show as sp
import data as d
import build_pokemon_html as bp

name = ""
opcion = 1
while opcion == 1:
    opcion = input("""¡Bienvenido a la Poké-Dex! 
Yo soy el Profesor Oak y he dedicado mi existencia al estudio de estas
maravillosas criaturas llamadas Pokémon y a difundir lo que he aprendido.
Para algunas personas estas criaturas son mascotas, mientras que otros
los usan para pelear deportivamente.
Dime ¿Te gustaría investigar más de los POKÉMON?

1. ¡Claro que sí, vamos!
0. Por ahora no, gracias.

    """)
    opcion = int(confirmar(["1", "0"], opcion)) #valida que el número ingresado sea correcto


    if opcion == 1:
        #INGRESA EL NOMBRE DEL POKÉMON
        name = input(d.intro)
        name = pv.validate(name) #el que regresa, que sí está bien escrito
        html = bp.crea_pokedex(name)
        sp.show_pics(html, name) 
              
    else:
        print("Gracias por visitarnos. Nos vemos una próxima oprtunidad")
        sleep(3)
        exit()

        
with open("pokemon_list.txt", "r") as f: #abre la lista de nombresd de pokémons 
    pokemon_lista = f.readlines()  #lo lee línea por línea y lo guarda 
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista] #saca el salto de línea que hay en la lista 
import data as d

def validate(name, p_l = pokemon_lista, mensaje = d.validacion_pokemon()): #esto hace que retorne el mensaje de data.py, que es imprimir una línea
    if name =='codigo-cero': #esto hace que agarre el nombre código cero y lo "traduzca"
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).lower() #cambia las posibles mayúsculas que puedan ingresar

    return name

if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))

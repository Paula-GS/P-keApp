def confirmar(opciones, eleccion):
    while eleccion not in opciones:
        eleccion = input("Has ingresado una opción no válida, por favor ingresa una de las opciones del menú: ")

    return eleccion

if __name__ == '__main__':
    opciones = ["1", "0"]
    eleccion = input("Escoja una opción: ")
    confirmar(opciones, eleccion)
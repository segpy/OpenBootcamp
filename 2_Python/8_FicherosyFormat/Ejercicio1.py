def Main():
    crearFichero()
    modificarFichero()


def crearFichero():
    fichero = open("fichero.txt", "w")
    fichero.write("Primera linea\n")
    fichero.close()

def modificarFichero():
    fichero = open("fichero.txt", "a")

    lista = ['Nueva linea', 'Nueva linea 2', 'Nueva linea 3']
    for linea in lista:
        if not linea == '\n':
            linea += '\n'
        fichero.write(linea)
    fichero.close()


if __name__ == '__main__':
    Main()
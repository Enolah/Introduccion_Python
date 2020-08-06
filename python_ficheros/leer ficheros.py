# Crea un programa que lea el mismo fichero de temperaturas y calcula la temperatura máxima y mínima del periodo.

def lee_temperaturas():
    """ Lee las temperaturas del fichero y las devuelve en una lista
    """
    temperaturas = []
    fichero = open("temperaturas.txt")
    for linea in fichero:
        valor = float(linea)  # convertir de cadena a número
        temperaturas.append(valor)

    fichero.close()
    return temperaturas


def calcula_media(temperaturas):
    """ Calcula la media de las temperaturas
    """
    suma = 0
    for valor in temperaturas:
        suma = suma + valor

    return suma / len(temperaturas)


# Programa
temperaturas = lee_temperaturas()
media = calcula_media(temperaturas)


print("Temperaturas:", temperaturas)
print("Temperatura media:", media)


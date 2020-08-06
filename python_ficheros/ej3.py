# Escribe una función que lea los números del fichero multiplos.txt y los devuelva en una lista de enteros.

def lee_numeros(nombre_fichero):
    """ Lee números del fichero que recibe como parámetro y los
    devuelve como una lista.
    """
    lista = []
    with open(nombre_fichero) as fichero:
        for linea in fichero:
            lista.append(int(linea))  # convertir a entero
    return lista

# Programa
lista = lee_numeros("multiplos.txt")
print(lista)
# Crea una función reciba una lista de números y devuelva cuántos de ellos son positivos.

lista = [i + 1 for i in range(-5, 15)]


def positivo(lista):
    """recibe una lista y devuelve cuantos positivos hay"""
    cont = 0
    for x in lista:
        if x >= 0:
            cont = cont + 1
        else:
            cont = cont

    return cont


print(lista)
print(positivo(lista))
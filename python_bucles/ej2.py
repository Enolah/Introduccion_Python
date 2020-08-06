# Escribe un programa que dada una lista elimine todos los elementos duplicados.
# No nos importa el orden en el que aparezcan los elementos en la lista final.

# creamos una lista con lo que quiera el usuario
lista=[input("introduce un numero o palabra: ") for x in range(0,10)]

# convertimos la lista en un conjunto y asi eliminamos los repetidos
conjunto= set(lista)

# lo volvemos a pasar a una lista para mostrarlo por pantalla
sin_repetir= list(conjunto)
print("Lista sin valores repetidos: ", sin_repetir)
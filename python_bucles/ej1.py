# Escribe un programa que clasifique los elementos de una lista en positivos y negativos. Los elementos positivos
# deben añadirse a una lista y los negativos a otra. Si la lista original contiene ceros, se deben ignorar.

# lista original
lista=[7,6,-9,234,-4,0,-7]
# creacion de las otras listas
positivos=[]
negativos=[]

# clasificacion

for x in lista:
    if x>0:
        positivos.append(x)
    elif x<0:
        negativos.append(x)

print("Positivos: ", positivos)
print("Negativos: ", negativos)
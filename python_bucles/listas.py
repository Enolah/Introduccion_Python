# Crea un programa que realice los siguientes pasos imprimiendo la lista tras cada uno de ellos:
# pida 5 palabras al usuario y las almacene en una lista.
# pida al usuario un nuevo elemento y lo añada al final de la lista
# pida al usuario una posición y elimine el elemento en esa posición.
# Si la posición no es válida se deben seguir pidiendo posiciones hasta que se introduzca una posición válida.

print("Primer paso:")
lista=[input("Introduzca una palabra: ") for i in range(0,5)]
print("Imprimir lista: ",lista)
print()

print("Segundo paso:")
palabra=input("Introduzca otra palabra: ")
lista.append(palabra)
print("Imprimir lista: ",lista)
print()

print("Tercer paso:")
num= int(input("Introduzca una posicion para eliminarla: "))
while num<0 or num>= len(lista):
    num = int(input("Introduzca una posicion para eliminarla: "))
del lista[num]
print("Imprimir lista: ",lista)
print()
# Escribe un programa que almacene las notas obtenidas por cada alumno en clase.
# El profesor introducirá cada vez el nombre de un alumno y una de sus notas.
# Al final del programa se mostrarán las notas obtenidas por cada uno de los alumnos.

# Vamos a representar las notas como un diccionario de listas
# La clave del diccionario será el nombre del alumno
# El valor del diccionario será la lista de notas de ese alumno
notas_clase = {}

nombre = input("Nombre del alumno ('fin' para terminar):")
while nombre != 'fin':
    nota = float(input("Nota:"))

    # ¿El alumno ya exitía?
    if nombre in notas_clase:
        # Recuperar la lista de notas del alumno
        notas_alumno = notas_clase[nombre]
        # Añadir la nueva nota al final de la lista
        notas_alumno.append(nota)
    else:
        # El alumno no existía: añadirlo
        # Creamos una lista con la única nota que tenemos
        notas_alumno = [ nota ]
        # Asociamos la lista de notas con el nuevo alumno
        notas_clase[nombre] = notas_alumno

    # Pedir siguiente nombre
    nombre = input("Nombre del alumno ('fin' para terminar):")

# Mostrar las notas por alumno
for nombre, notas_alumno in notas_clase.items():
    print(nombre, ":", notas_alumno)
# Escribe un programa que calcule la nota media de un alumno dadas las notas de sus dos exámenes parciales.
# El alumno estará suspenso si no ha aprobado ambos parciales.

exam1= float(input("Nota parcial 1: "))
exam2= float(input("Nota parcial 2: "))

if exam1 < 5 or exam2<5:
    print("Estas suspenso")
else:
    print("Enhorabuena usted ha aprobado!!")
    print("La nota media es de ", (exam1+exam2)/2)





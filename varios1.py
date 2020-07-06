#Escribe un programa que calcule el volumen de un cono a partir del radio de la base y su altura.
# Usa la siguiente fórmula: volumen = pi * radio * radio * altura / 3
# Solicita los valores de radio y altura al usuario. Recuerda que el valor aproximado de pi es 3.14159.
print("--- Ejercicio 1 ---")
print()
pi= 3.14159
radio= float(input("Introduce el radio de la base del cono: "))
altura= float(input("Introduce la altura del cono: "))
volumen = pi * radio * radio * altura / 3
print("El volumen del cono es de ", volumen, "cm3")
print()

#Escribe un programa que calcule la nota final de un alumno a partir de las
# calificaciones de los 3 exámenes parciales que ha realizado,
# teniendo en cuenta que el primer examen parcial vale un 20% ,
# el segundo un 30% y el último un 50% de la nota final.
print("--- Ejercicio 2 ---")
print()
exa1= 0.2*float(input("Nota del primer parcial: "))
exa2= 0.3*float(input("Nota del segundo parcial: "))
exa3= 0.5*float(input("Nota del tercer parcial: "))

print("La nota final es de un ", exa1+exa2+exa3)
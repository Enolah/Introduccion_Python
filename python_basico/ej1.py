# Escribe un programa que calcule el volumen de un cono a partir del radio de la base y su altura.
# Usa la siguiente fórmula: volumen = pi * radio * radio * altura / 3
# Solicita los valores de radio y altura al usuario. Recuerda que el valor aproximado de pi es 3.14159.
print("--- Ejercicio 1 ---")
print()
pi = 3.14159
radio = float(input("Introduce el radio de la base del cono: "))
altura = float(input("Introduce la altura del cono: "))
volumen = pi * radio * radio * altura / 3
print("El volumen del cono es de ", volumen, "cm3")
print()
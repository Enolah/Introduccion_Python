# Haz un programa que pida al usuario su nombre y escriba el número de las letras que contiene
print("--- Ejercicio 1 ---")
print()
nombre = input("Introduce tu nombre: ")
print(nombre.capitalize(), " tiene ", len(nombre), " letras")
print()

# Haz un programa que pida la longitud de un lado de un cuadrado e imprima su
# perimetro y su area
print("--- Ejercicio 2 ---")
print()
longitud = float(input("Introduce la longitud de un lado de un cuadrado: "))
print("El cuadrado tiene un perimetro de", longitud * 4, "cm y un area de ", longitud ** 2, "cm2.")

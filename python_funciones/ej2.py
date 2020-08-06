# Crea un programa que imprima tablas de multiplicar de números. El programa debe tener las siguientes funciones: Una
# función imprime_tabla_multiplicar que recibe como parámetro un número e imprime su tabla de multiplicar. Por
# ejemplo, si recibe el 7 debe imprimir: 7 * 1 = 7, 7 * 2 = 14, …, 7 * 10 = 70 cada uno en una línea. Una función
# pide_datos que pide al usuario la tabla de multiplicar que desea ver y devuelve dicho valor. Si el número
# introducido es negativo o mayor que 10, volverá a preguntar al usuario hasta que introduzca un valor correcto.

def imprime_tabla_multiplicar(num):
    print("La tabla de multiplicar del ", num, " es: ")
    print()

    for i in range(1, 10 + 1):
        print(num, " * ", i, " = ", num * i)

def pide_datos():
    num= int(input("Introduce un numero (0 para terminar): "))
    while num<0 or num>10:
        num= int(input("Introduce un numero: "))

    return num

n = pide_datos()
while (n != 0):
    imprime_tabla_multiplicar(n)
    n = pide_datos()



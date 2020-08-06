# for variable in range(inicio, fin):
#    <instrucciones_del_bucle>
# <resto_del_programa>

# Escribe un programa que imprima la tabla de multiplicar de un número introducido por el usuario usando una
# instrucción for. Por ejemplo, si el usuario introduce el 7, el programa debe imprimir la tabla del 7.

num= int(input("Introduce un numero: "))
print("La tabla de multiplicar del ",num, " es: ")
print()

for i in range(1, 10+1):
    print(num, " por ", i, " es ", num*i)
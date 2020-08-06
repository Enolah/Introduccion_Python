# while <condición>:
#    <instrucciones_dentro_del_while>
# <resto_del_programa>

# Escribe un programa que pida palabras al usuario hasta que introduzca alguna que comience por la letra a (mayúscula
# o minúscula). Antes de finalizar, el programa indicará el número total de palabras introducidas.

cont=1
palabra= input("Introduce una palabra: ")

while not palabra.startswith("a"):
    cont= cont+1
    palabra= input("Introduce una palabra: ")

print("Usted ha realizado ", cont, " intentos para acertar.")
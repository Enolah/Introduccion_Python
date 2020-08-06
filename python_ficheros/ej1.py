# Escribe un programa que lea nombres de personas del fichero nombres.txt
# e imprima por consola sólo aquellos que empiezan por una vocal.

fichero = open("nombres.txt")

for linea in fichero:
    if (linea.lower().startswith("a") or
            linea.lower().startswith("e") or
            linea.lower().startswith("i") or
            linea.lower().startswith("o") or
            linea.lower().startswith("u")):
        print(linea.strip())

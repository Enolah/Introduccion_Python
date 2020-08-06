# Escribe en un fichero los múltiplos de 5 menores que 100.

with open("multiplos5.txt","w") as fichero:
    for x in range(0,100,5):
        fichero.write(str(x)+"\n")
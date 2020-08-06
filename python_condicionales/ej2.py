# Casi todo el mundo piensa que los años bisiestos son los divisibles por 4 (por ejemplo 1988, 1992 y 1996 son años
#  bisiestos). Pero existe una excepción a esa regla: los años divisibles por 100 sólo son bisiestos sin además son
#  divisibles por 400. Por ese motivo el año 1600 es bisiesto pero el 1700 no lo es. Haz un programa que pida un año
#  al usuario y diga si es bisiesto o no.

año= int(input("Introduce un año: "))
# calcular si es bisiesto

if año%100==0 and not año%400==0:
    print("Lo sentimos, el año ", año, " no es bisiesto.")
elif año%4 ==0:
    print("El año ", año, " es bisiesto.")
else:
    print("Lo sentimos, el año ", año, " no es bisiesto.")

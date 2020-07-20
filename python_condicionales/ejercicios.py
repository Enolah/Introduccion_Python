# Escribe un programa que calcule la nota media de un alumno dadas las notas de sus dos exámenes parciales.
# El alumno estará suspenso si no ha aprobado ambos parciales.

exam1= float(input("Nota parcial 1: "))
exam2= float(input("Nota parcial 2: "))

if exam1 < 5 or exam2<5:
    print("Estas suspenso")
else:
    print("Enhorabuena usted ha aprobado!!")
    print("La nota media es de ", (exam1+exam2)/2)


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


# Escribe un programa que pregunte al usuario un nombre de mes y escriba el número de días que tiene.
# El nombre del mes puede estar escrito en mayúsculas o minúsculas.
# Consideraremos que el año no es bisiesto y por tanto febrero siempre tiene 28 días.
# Si el usuario introduce un mes que no existe el programa mostrará un mensaje indicando que no conoce ese mes.

# preguntamos al usuario un mes
mes = input("Introduce el nombre del mes: ").lower()
# Averiguamos cuantos dias tiene dicho mes

if mes== "enero" or mes== "marzo" or mes=="mayo" or mes=="julio" \
        or mes=="agosto" or mes=="octubre" or mes=="diciembre":
    print(mes.capitalize(), " tiene 31 dias.")
elif mes== "abril" or mes=="junio" or mes=="septiembre" or mes=="noviembre":
    print(mes.capitalize(), " tiene 30 dias.")
elif mes== "febrero":
    print(mes.capitalize()," tiene 28 dias.")
else:
    print("El mes introducido no es correcto.")
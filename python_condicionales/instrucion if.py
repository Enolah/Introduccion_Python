# Al final del archivo se encuentra unas notas, con la estructura de los condicionales.
# Escribe un programa que pida dos números enteros al usuario y a continuación imprima el menor.

num1= int(input("Introduce un numero entero: "))
num2= int(input("Introduce otro numero entero: "))

if num1 <= num2:
    print ("El numero menor es: ", num1)
else:
    print("El numero menor es: ", num2)

# Escribe un programa que pida al usuario el nombre de un país europeo y a continuación escriba su población según la
# siguiente tabla.

pais= input("Elige uno de estos 5 paises (España, Francia, Portugal, Alemania, Reino Unido): ")
if pais.capitalize() == "España":
    print("46M")
elif pais.capitalize()== "Francia":
    print("64M")
elif pais.capitalize()== "Portugal":
    print("10M")
elif pais.capitalize() == "Alemania":
    print("81M")
elif pais.capitalize() == "Reino":
    print("65M")
else :
    print("Ese pais no existe en la tabla")


# NOTAS:

# condicional IF en su version sencilla:
# if <condición>:
#   <instrucciones_dentro_del_if>
# <resto_del_programa>

# condicional IF-ELSE:
# if condición:
#    <instrucciones_parte_if>
# else:
#   <instrucciones_parte_else>
# <resto_del_programa>

# condicional IF-ELIF-ELSE
# if <condición A>:
#    <instrucciones_parte_A>
# elif <condición B>:
#    <instrucciones_parte_B>
# elif <condicion C>:
#    <instrucciones_parte_C>
# else:
#    <instrucciones_parte_else>
# <resto_del_programa>

#Escribe un programa que pida al usuario el valor del radio y a continuación imprima la longitud de la circunferencia
# y el área del círculo asociados.

#pedimos datos al usuario
pi= 3.14159
print("Calcula la longitud de la circunferencia y el area del circulo.")
radio=float(input("Introduce su radio: "))

#hacemos el calculo
longitud = 2 * pi * radio
area = pi * radio * radio

#mostramos por pantalla
print("La longitud de la circunferencia es de",longitud,"cm y el area del circulo es de",area, "cm2")
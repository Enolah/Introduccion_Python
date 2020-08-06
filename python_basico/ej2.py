# Escribe un programa que calcule la nota final de un alumno a partir de las
# calificaciones de los 3 exámenes parciales que ha realizado,
# teniendo en cuenta que el primer examen parcial vale un 20% ,
# el segundo un 30% y el último un 50% de la nota final.
print("--- Ejercicio 2 ---")
print()
exa1 = 0.2 * float(input("Nota del primer parcial: "))
exa2 = 0.3 * float(input("Nota del segundo parcial: "))
exa3 = 0.5 * float(input("Nota del tercer parcial: "))

print("La nota final es de un ", exa1 + exa2 + exa3)
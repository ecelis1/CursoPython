"""
Practica 01: Calcular cociente y el Residuo de dos números enteros

Enunciado: halar el cociente y el residuo (resto) de dos números enteros.

Análisis: para la solución de este problema, se requiere que el
usuario ingrese dos números enteros y el sistema realice el
cálculo respectivo para hallar el cociente y residuo, para esto use
la siguiente expresión.
"""
print("Calcular cociente y el Residuo de dos números enteros")
# Entrada de Datos
a = int(input("Ingrese Dividendo: "))
b = int(input("Ingrese Divisor: "))

# Operaciones

# Resto
resto = a % b

# Cociente
cociente = a // b

print(f"El cociente es: {cociente}, el resto es: {resto}"  )
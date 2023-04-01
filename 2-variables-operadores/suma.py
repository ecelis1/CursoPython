print("Suma de dos numeros Enteros")
# Entrada de Datos
a = input("Ingrese Primer Numero: ")
b = input("Ingrese Segundo Numero: ")

# Operacion
suma=a+b

# Salida como string

print("El Resultado es: ",suma)
print("Se muestra de esta manera porque no esta como entero,\nlo que vamos a hacer es convertir las variables en enteros")

# Castear datos (Casting de datos)
a=int(a)
b=int(b)

suma = a+b

print(f"El Resultado es: ",suma)
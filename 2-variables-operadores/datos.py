# Muestra un msj de hola mundo
print('Hola Mundo')

# Definiendo Variables
nombre = "Emanuel Celis"
edad = 25
datos = nombre, edad

"""
Muestra la informacion del usuario
por pantalla
"""

print("Opcion 1: Tupla (Tuple ENG)")
print(datos)
print(type(datos))

print("Opcion 2: Print con Concatenacion")
print(nombre,edad)

print("Opcion 3: Print Normal")
print(nombre)
print(edad)

print("Opcion 4 Concatenar Cadena de Caracter con Variable con numero enteros")
print("Nombre: ", nombre)
print("Edad: ", edad)

print("Opcion 5: Formateo de informacion con f, porque tenemos caracteres especiales")
print(f"Nombre: , {nombre} \nEdad: {edad}")

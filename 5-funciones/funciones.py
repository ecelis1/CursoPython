
def saludar():
    global nombre
    nombre = 'Emanuel Celis'
    print('Hola desde la funcion saludar')
    print('hola',nombre)

saludar()
print('hola desde fuera de la funcion', nombre)
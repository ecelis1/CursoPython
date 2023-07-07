from io import open
from os import path

def leerArchivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt','r')

        #asi devuelve todo el archivo como esta escrito
        textos = archivo.read()

        #De esta manera devuelve el archivo, siendo que cada linea va a ser un elemento de una lista
        #textos = archivo.readlines()
        
        #De esta manera devuelve solo una linea de el archivo
        #textos = archivo.readline()

        archivo.close()
    
        print(textos)
    
    else:
        print('No existe el archivo')
    
def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write('Hola Perejiles')
    archivo.close()

def agregarDatos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt','a')
        archivo.write('\nHola Ema')
        archivo.close()
    
    
    else:
        print('No existe el archivo')

def modificarDatos():

    if path.isfile('texto.txt'):
        archivo = open('texto.txt','r+')
        texto = archivo.readlines()
        print(texto)
        texto[1]='Hola Emanuel Celis\n'
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
    
        print(texto)
    else:
        print('No existe el archivo')

def eliminarDatos():
    archivo=open('texto.txt','w')
    archivo.close()
#escribir_archivo()
#leerArchivo()
#agregarDatos()
#modificarDatos()
#eliminarDatos()
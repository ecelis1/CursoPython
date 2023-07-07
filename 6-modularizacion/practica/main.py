from figura import *
from vista import *

def main():
    bTrue = True

    while bTrue:
        Vista.MenuPrincipal()
        seleccion = Vista.seleccion()
        match (seleccion):
            case 1:
                base = Vista.ingresoFloat('Ingrese Base: ')
                altura = Vista.ingresoFloat('Ingrese Altura: ')
                r = Rectangulo(base,altura)
                ProbarFigura(r)

            case 2:
                radio = Vista.ingresoFloat(f'Ingrese Radio del {Figura.getNombre}: ')
                r = Circulo(radio)
                ProbarFigura(r)
            case 3: 
                break


#Al hacer esto, el interprete de python va a buscar un archivo que contenga esta instruccion para iniciar la ejecucion de este punto, entonces aqui vamos a ejecutar nuestra funcion main
if __name__ == '__main__':
    main()
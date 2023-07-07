class Vista():
    def MenuPrincipal():
        print('MENU PRINCIPAL\nAREA Y PERIMETRO DE FIGURAS GEOMETRICAS\n1.Rectangulo\n2.Circulo\n3.Salir')
    
    def seleccion():
        seleccion = int(input('Ingrese su seleccion: '))
        return seleccion
    
    def ingresoFloat(msg):
        valor = float(input(f'{msg}'))
        return valor

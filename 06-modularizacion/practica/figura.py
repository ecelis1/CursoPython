import math

class Figura():
    #Constructor
    def __init__(self,nombre) -> None:
        self._nombre = nombre

    #Getters
    def getNombre(self):
        return self._nombre
    
    #Setters
    def setNombre(self,xNombre):
        self._nombre = xNombre

    def __str__(self) -> str:
        return f'El nombre de la figura es: {self.getNombre}'
    
        
class Rectangulo(Figura):
    #Constructor
    def __init__(self,base,altura) -> None:
        self._nombre = __class__.__name__
        self._base = base
        self._altura = altura
    
    #Getters
    def getBase(self):
        return self._base
    def getAltura(self):
        return self._altura
    #Setters
    def setBase(self,xBase):
        self._base = xBase
    def setAltura(self,xAltura):
        self._altura = xAltura

    def __str__(self) -> str:
        return f'El nombre de la figura es: {self._nombre} [Base: {self._base}, Altura: {self._altura}]'

    def area(self):
        return self._base * self._altura
    def perimetro(self):
        return ((2 * self._base) + (2 * self._altura))    
    



class Circulo(Figura):
    #Constructor
    def __init__(self,radio) -> None:
        self._nombre = __class__.__name__
        self._radio = radio
    
    #Getters
    def getBase(self):
        return self._radio

    #Setters
    def setBase(self,xRadio):
        self._radio = xRadio
   

    def __str__(self) -> str:
        return f'El nombre de la figura es: {self._nombre} [Radio: {self._radio}]'

    def area(self):
        return (math.pi * (self._radio**2))
    def perimetro(self):
        return 2 * math.pi * self._radio  
    
def ProbarFigura(Figura):
    print(Figura)
    print(f'Area: {Figura.area()}')
    print(f'Perimetro: {Figura.perimetro()}')
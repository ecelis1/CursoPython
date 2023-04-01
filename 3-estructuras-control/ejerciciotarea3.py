#Inicializar
i=0
contnegat=0
contpositivo=0

#Entrada

ni=int(input("Ingrese numero inicial: "))
nf=int(input("Ingrese numero final: "))

#Operacion

i=ni+1

while i<nf:
    if i<0:
        contnegat+=1
    else:
        contpositivo+=1
    i+=1

#Salida
print(f"La cantidad de numeros positivos son {contpositivo} y negativos son {contnegat} numeros")
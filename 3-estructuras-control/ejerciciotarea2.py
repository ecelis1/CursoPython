#Inicializar
c=0
i=0

#Entrada

ni=int(input("Ingrese numero inicial: "))
nf=int(input("Ingrese numero final: "))

#Operacion
#Por ejemplo si pones 1 y 4, deberia dar 2, porque entre ese rango solo esta el 2 y el 3
i=ni+1

while i<nf:
    c+=1
    i+=1

#Salida
print(f"La cantidad que hay es: {c} numeros")
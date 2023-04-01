#Definir
listanum = [None]*6
may=0
men=0

#Operacion
for n in range (6):
    #Entrada
    listanum[n]=float(input(f"Ingrese numero {n+1}: "))
    if n==1:
        may=listanum[n]
        men=listanum[n]
    else:
        if listanum[n]>may:
            may=listanum[n]
        elif listanum[n]<men:
            men=listanum[n]

#Salida
print("Lista de numeros: ",listanum)
print(f"Numero mayor {may}, Numero menor: {men}")
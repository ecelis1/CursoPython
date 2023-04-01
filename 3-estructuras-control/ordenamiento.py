#Inicializar lista y constantes
cantnum=3
num = [None]*cantnum
#Entrada

for i in range(cantnum):
    num[i]= float(input(f"Ingrese un numero entero {i+1}: "))

#Operacion

for i in range(cantnum-1):
    for j in range(i+1,cantnum):
        if num[i] > num[j]:
            cambio = num [i]
            num[i]=num[j]
            num[j]=cambio
#Salida
for i in range(cantnum):
    print(num[i])
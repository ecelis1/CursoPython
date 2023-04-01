#Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos.

#Entrada
segundos = float(input("Ingrese Cantidad en Segundos : "))

#Operaciones
horas = round(segundos/3600)
minutos = round((segundos - (horas * 3600))/60)
segundos = round(segundos - ((horas * 3600) + (minutos * 60)))

#Salidas
print("="*12)
print("---QUEDAN---")
print(f"{horas}h:{minutos}m:{segundos}s")
print("="*12)
#Entrada

consumo=float(input("Ingrese el monto del consumo: $"))

while consumo<=0:
    print("Por favor ingrese un monto correcto")
    consumo=float(input("Ingrese el monto del consumo: $"))

#Operacion
total=0
montDescuento=0
impuesto=0

if consumo<=100:

    montDescuento=(consumo*0.10)
    impuesto=consumo*0.19
    total=(consumo+impuesto)-montDescuento
    #Salida
    print(f"Monto del descuento 10%: ${round(montDescuento,2)}")
    print(f"Monto del Impuesto: ${round(impuesto,2)}")
    print(f"Importe a Pagar: ${round(total,2)}")

else:
    montDescuento=(consumo*0.20)
    impuesto=consumo*0.19
    total=(consumo+impuesto)-montDescuento
    #Salida
    print(f"Monto del descuento 20%: ${round(montDescuento,2)}")
    print(f"Monto del Impuesto: ${round(impuesto,2)}")
    print(f"Importe a Pagar: ${round(total,2)}")

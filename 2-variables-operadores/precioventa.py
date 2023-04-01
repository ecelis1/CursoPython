import os
print("Calcular Precio de Venta")
# Entrada de Datos
print("="*26)
print("----REALIZAR UNA VENTA----")
print("="*26)
vVenta = float(input("Ingrese Precio de Venta: $"))


os.system("cls")
# Operaciones

igv=vVenta*0.18

pDeVenta = vVenta+igv

# Salida 
print("="*25)
print("----FACTURA DE VENTA----")
print("="*25)
print("Valor de la venta $",vVenta)
print("IGV: $",igv)
print("El precio de venta es: $",pDeVenta)
print("="*25)
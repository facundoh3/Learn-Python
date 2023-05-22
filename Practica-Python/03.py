# Empresa de transporte requiere guardar el nombre y recorido de cada conductor
# Para guardar esta informacion se utilizaran dos arrays
# NOMBRE = []
# KMS = []
# Se quiere generar una nueva lista ('total_kms') con los kilometros
# totales que realiza cada conductor.
# Lista de nombres de los conductores

total=[]
print(total)
camioneros = int(input("Ingrese el numero de camioneros a iterar"))

for camionero in range(camioneros):
    nombre_camionero= str(input("Ingresse el nombre del camionero "+ str(camionero)))  
    kilometros = int(input("Ingrese los kilometros recorridos del camionero "+str(camionero+1)))
    total.append((nombre_camionero,kilometros))
print(total)

for nombre,kilo in total:
    print(f"Camionero : {nombre} , {kilo} ")
# Queremos guardar la temperatura mínima y máxima de 5 días.
# Realiza un programa que de la siguiente información:

# La temperatura media de cada día
# Los días con menos temperatura

# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
# si no existe ningún día se muestra un mensaje de información.

temperaturas=[]
temperatura_media=[]
print(temperaturas)
for i in range(1,3):
    print("Ingrese las temperatura max y min del dia : "+str(i))
    temperatura_max=float(input())
    temperatura_min=float(input())
    temperaturas.append((temperatura_max,temperatura_min))
    temperatura_media= float(temperatura_min + temperatura_max)/2

print("Temperaturas registradas ",temperaturas)


for a in temperaturas:
    print(f"La temperatura media del dia {a} es : "+ str(temperatura_media))

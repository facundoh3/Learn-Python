# 1. Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua) en una lista
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

cursos=["Matematicas","Fisica","Quimica","Historia","Lengua"]
aprobadas=[]
desaprobadas=[]

#Almacenamos las notas en la lista de aprobadas 
for materia in cursos:
    nota = int(input("¿Cuanto sacaste en : "+ materia +"?"))
    if nota >= 7 :
        aprobadas.append(materia)
    else:
        desaprobadas.append(materia)

print(f"Las materias son: {cursos}")
print(f"Las materias aprobadas son: {aprobadas}")
print(f"Las materias desaprobadas son {desaprobadas}")

   
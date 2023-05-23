# La limpieza de archivos de datos iniciales es una tarea común en programación.
# Puede realizar la limpieza de preproinsulin-seq.txt mediante programación de varias
# formas, por ejemplo, con el uso de Bash, Python u otro lenguaje de programación de su elección.
# Pruebe utilizar expresiones regulares para eliminar mediante programación el archivo de ORIGIN,
# sus números, las dos barras diagonales (//), los espacios y los saltos de línea o los carros de retorno.
# También puede confirmar mediante programación que el archivo tiene 110 caracteres.



"""
with open('preproinsulin-seq.txt','r') as archivo:
    contenido = archivo.read()
    

print(contenido)

eliminar=["ORIGIN"," ","//"]

for i in eliminar :
    contenido= contenido.replace(i,' ')

print(contenido)

# 24 - 30 - 35 - 21
a = contenido[0:24]
b = contenido[24:54]
c = contenido[54:89]
d = contenido[89:110]

print(a)
print(b)
print(c)
print(d)

# contenido del archivo .txt


def create_file(filename):
    with open(filename, 'w') as file:
        file.write(a,b,c,d)


files = ["preproinsulin-seq-clean.txt",  "lsinsulin-seq-clean.txt",
         "binsulin-seq-clean.txt", "cinsulin-seq-clean.txt", "ainsulin-seq-clean.txt"]

# nombre de los archivos .txt
for file in files:
    create_file(file)
"""

# Abrir el archivo original
with open("preproinsulin-seq.txt", "r") as archivo:
    contenido = archivo.read()

eliminar=["ORIGIN"," ","//"]

for i in eliminar :
    contenido = contenido.replace(i, "")
    
with open("prueba.txt","w") as archivo_modificado:
    archivo_modificado.write(contenido)
    
print(contenido)
# Limpiar y guardar los aminoácidos en archivos separados
lsinsulin_seq = contenido[0:24]
binsulin_seq = contenido[24:54]
cinsulin_seq = contenido[54:89]
ainsulin_seq = contenido[89:110]

# Guardar en archivos separados
with open("lsinsulin-seq-clean.txt", "w") as archivo_ls:
    archivo_ls.write(lsinsulin_seq)

with open("binsulin-seq-clean.txt", "w") as archivo_bs:
    archivo_bs.write(binsulin_seq)

with open("cinsulin-seq-clean.txt", "w") as archivo_cs:
    archivo_cs.write(cinsulin_seq)

with open("ainsulin-seq-clean.txt", "w") as archivo_as:
    archivo_as.write(ainsulin_seq)
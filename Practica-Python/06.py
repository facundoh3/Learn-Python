# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

#frase_usuario= str(input("Ingrese una frase \n"))
#letra_usuario= str(input("Ingrese una letra \n"))
frase_usuario= "hola como estas "
letra_usuario='a'

#Enumerate muestra el indice y el o
for indice,i in enumerate(frase_usuario):
    if i == letra_usuario:
        print(f"Se encontro la letra {letra_usuario} en el indice : {indice} de la frase : {frase_usuario}")
    

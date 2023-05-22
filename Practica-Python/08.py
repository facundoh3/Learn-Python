# escribir un programa que almacene una clave en una vaniable,
# luego solicite al usuario "ingresar una clave" valida e imprimir
# "clave correcta" cuando se cumpla la validacion sea correcta.


clave ="hola"

intento_clave= str(input("Ingrese la clave\n"))

if intento_clave == clave:
    print("Clave correcta")
else:
    print("Clave incorrecta")
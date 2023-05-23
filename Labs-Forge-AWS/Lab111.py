"""
TRABAJO CON LISTAS TUPLAS Y DICCIONARIOS
"""

#Definicion de una lista 
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#ACCESO DE UNA LISTA POR INDEX
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#MODIFICACION DE LOS VALORES DE UNA LISTA 
myFruitList[2] = "orange"
print(myFruitList)

"""
DEFINICION DE UNA TUPLA
Una tupla es similar a una lista, pero no se pueden cambiar los datoa son INMUTABLES UNA VEZ QUE SE CREAN
se crea en parentesis en vez de corchetes([]).
"""
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
"""
DEFINICION DE UNA DICCIONARIO
Un diccionario es una lista cuyas posiciones 
tienen nombres asignados (claves) con valores al lado (valor)
Clave Valor 
"""
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
#Acceso por clave
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
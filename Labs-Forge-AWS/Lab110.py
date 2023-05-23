"""
TIPO DE DATO DE CADENA 
"""
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
#CONCATENACION 
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
#TRABAJAR CON INPUT
name = input("What is your name? ")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))#=>.format() coloca las variables en orden en el print con format
#print("Facundo,you like a rojo halcon")

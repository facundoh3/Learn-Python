# En programación, una función es una sección con nombre dentro de un programa que realiza una tarea específica. Python tiene funciones integradas como print() proporcionadas por el mismo lenguaje. Además, puede utilizar funciones proporcionadas por otros desarrolladores a través de la instrucción import. Por ejemplo, puede utilizar import math si desea utilizar la función math.floor(). En Python, puede crear sus propias funciones, denominadas funciones definidas por el usuario.

# Para continuar el debate sobre las funciones definidas por el usuario, escribirá un programa para implementar un cifrado César, que es un método sencillo de cifrado. El cifrado César toma las letras de un mensaje y desplaza cada letra a lo largo del alfabeto un número determinado de posiciones.

# En este laboratorio, deberá realizar lo siguiente:

# crear funciones definidas por el usuario
# utilizar varias funciones para implementar un programa de cifrado César


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount


def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(
        myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()
def rombo (filas):
    for i in range(1,filas-1):
        print(' ' * (filas-i) + '* '*(i))

    for i in range(filas-1, -0,-1):
        print(" " * (filas-i) + "* " * (i))
        
filas = int(input("Ingrese el tamaño del rombo :"))
rombo(filas)
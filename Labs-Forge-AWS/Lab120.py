# En el módulo de Control de caudal, aprendió sobre las instrucciones if-else, los bucles while, las listas y los bucles for. Ahora pondrá en práctica lo aprendido en la aplicación de la insulina en el mundo real.

# Aquí utilizará bucles lists, for y while, y cálculos básicos para determinar la carga neta de la insulina entre pH 0 y pH 14.

# En este laboratorio, deberá realizar lo siguiente:

# crear un diccionario de valores de pKa (que indican la intensidad de un ácido) que se utilizará en los cálculos de carga neta
# utilizar el método count() para obtener un recuento de aminoácidos
# utilizar un bucle while para calcular la carga neta de la insulina entre pH 0 y pH 14

# Python3.6
# Coding: utf-8
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}


float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x))
            for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']})

pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])))
               for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x])))
                for x in ['y', 'c', 'd', 'e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1
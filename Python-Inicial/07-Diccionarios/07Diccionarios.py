# Diccionarios "Clave - Valor" =>
diccionario = {
    'avion': 'rapido',
    'auto': 'lento'
}
print(diccionario)  # {'avion': 'rapido', 'auto': 'lento'}
print(len(diccionario))  # 2
print(diccionario['avion'])  # rapido
print(diccionario.get(''))  # None
print(diccionario.get('auto'))  # lento
print('avion' in diccionario)  # True

# Mutacion de Diccionarios =>
persona = {
    'nombre': '',
    'edad': 50,
    'lenguajes': ['ingles', 'spanish']
}
# Reemplazar valores
persona['nombre'] = 'facundo'


print(persona)
# {'nombre': 'facundo', 'edad': 50, 'lenguajes': ['ingles', 'spanish']}
persona['edad'] += 25
print(persona)
# {'nombre': 'facundo', 'edad': 75, 'lenguajes': ['ingles', 'spanish']}
persona['lenguajes'].append('aleman')
print(persona)
# {'nombre': 'facundo', 'edad': 75, 'lenguajes': ['ingles', 'spanish', 'aleman']}
del persona['nombre']
print(persona)  # {'edad': 75, 'lenguajes': ['ingles', 'spanish', 'aleman']}
print(persona.items())
# dict_items([('edad', 75), ('lenguajes', ['ingles', 'spanish', 'aleman'])])
print(persona.keys())
# dict_keys(['edad', 'lenguajes'])
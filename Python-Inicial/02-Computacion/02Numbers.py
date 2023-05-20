#Ejercicio 1 (Adicion Sustraccion Asignacion)
sword_damage = 3
arrow_damage = 5
spear_damage = 2
dagger_damage = 1
fire_damage = 4
total_damage = sword_damage+arrow_damage+spear_damage+dagger_damage+fire_damage
average_damage = (sword_damage+arrow_damage+spear_damage+dagger_damage+fire_damage)/5
print(f"total damage is: {total_damage}")
print(f"average damage is: {average_damage}")

#Ejercicio 2 (Cociete Exponentes)
7 // 3
# 2 (an integer) me da  el cociente
# 3 elevado a la 2
3 ** 2
# 9 el resultado da 9 

#Ejercicio 3 (Cambiar el resultado en la misma variable)
player_score = 3242439
player_score = (234340+player_score)
print("player_score is: " + str(player_score))

player_health = 156
player_health +=10
print(player_health)

#Ejercicio 4 (Notacion Cientifica)
print(16e3)
# Prints 16000.0
print(7.1e-2)
# Prints 0.071
max_number_of_players=1024e10
print(16e3)
print(f"Maximum players on a Fantasy Quest server: {max_number_of_players}")
#Ejercicio 5(Binario en python) 
print(0b0001)
# Prints 1
print(0b0101)
# Prints 5
#Ejercicio 6 (Operadores a nivel de bits)
can_create_guild = 0b1000
can_review_guild = 0b0100
#Operador (And &) basicamente seria 0 + 0 te da 0 osea false 1+1 te da true 1+0 te da false y asi se compara
0101 = 5
&
0111 = 7
=
0101 = 5
#Son como tablas de verdad 
#Operador (And |)
0101
|     
0111
=
0111
#Con el and si habia un 0 y 1 resultaba false (0) en este caso con OR daria true(1)
#Adicion Binaria
num_heads = 0b0001
num_arms = 0b0010
num_fingers = 0b1010
num_heads=(num_arms+num_fingers)
#Operador NOT cambia el resultado 
 print(not True)
# Prints: False

print(not False)
# Prints: True
#Ejercicio 7 (Operadores de comparacion)
print(5 < 6)
print(5 != 6)
print(5 != 5)
print(6 > 6)

#Ejercicio 1 (comparaciones)
elon_height = 5
sara_height = 10
jill_height = 7
bob_height = 6

bob_taller_than_elon = bob_height>elon_height
sara_taller_than_elon = sara_height> elon_height
jill_taller_than_sara = jill_height> sara_height

print(type(bob_taller_than_elon))
print(bob_taller_than_elon)
print(type(sara_taller_than_elon))
print(sara_taller_than_elon)
print(type(jill_taller_than_sara))
print(jill_taller_than_sara)

#Ejercicio 2 (Incremento Decremento)
shield_armor = 5
print("shield_armor was: " + str(shield_armor))
shield_armor -= 3
print("shield_armor is: " + str(shield_armor))
shield_armor +=5 
print("shield_armor is: " + str(shield_armor))

#Ejercicio 3.1 (If)
player_health = 0
if player_health == 0:
    print("dead!")
if player_health > 0:
    print("alive!")
#Ejercicio 3.2    
number_of_swords = 500
number_of_soldiers = 1000
if number_of_swords < number_of_soldiers: 
    print("We do not have enough swords for the army!")
#Ejercicio 3.3
player_health = 4
if player_health == 0 :
    print("dead")
elif player_health < 5:
    print("injured")
else:
    print("healthy")
#Ejercicio 3.3    

current_player_name = "ash ketchum"
high_scoring_player_name = "ash ketchum"
#Ejercicio 3.4
if current_player_name == high_scoring_player_name:
    print("You are the highest scoring player!")
else:
    print("You are not the highest scoring player")
#Ejercicio 3.5
time_purchased = 3
time_parked = 3

if time_parked >= time_purchased :
    print("You have been charged for overtime parking")
else:
    print("Your time hasnt expired yet")
#Ejercicio 3.6
player_power = 101
enemy_defense = 100
advantage, disadvantage, evenly_matched = False, False, False

if player_power > enemy_defense:
    advantage = True
    
elif player_power < enemy_defense:
    disadvantage = True

else:
    evenly_matched=True
    
if advantage:
    print("You have the advantage!")
elif disadvantage:
    print("You have the disadvantage!")
else:
    print("You are evenly matched!")
#Ejercicio 3.7
gallons_in_car = 8
miles_to_work = 105
miles_per_gallon = 22

gallons_needed = gallons_in_car * miles_per_gallon
if gallons_in_car > gallons_needed:
    print("You have enough gas to make it!")
else:
    print("You need more gas!")
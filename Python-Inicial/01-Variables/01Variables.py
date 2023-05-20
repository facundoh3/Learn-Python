#Ejercicio 1
player_health=1000
print(player_health)
#Ejercicio2 (Reasignacion de variables)
player_health = 1000
# reduce by 100 here
player_health = 900
print(player_health)
# and here
player_health = 800
print(player_health)
# and here
player_health = 700
print(player_health)
# and here
player_health = 600
print(player_health)
#Ejercicio 3 (Operaciones basicas matematicas)
player_health = 1000
armor_multiplier = 2
armored_health = player_health *armor_multiplier
print(armored_health)

player_health = 6783424367754
poison_damage = 89743873
player_poison_health = player_health - poison_damage
print(player_poison_health)

#Ejercicio 4 (Comentarios como funciionan los comentarios)
#the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

#Ejercicios 5 (Tipos de datos)
player_health = 100
player_has_magic = True
# don't touch below this line
print(f"player_health is a/an {type(player_health)}")
print(f"player_has_magic is a/an {type(player_has_magic)}")

# create the empty "enemy" variable here
enemy = None
# don't touch below this line
print(enemy is None)

#Ejercicio 6 (Concatenacion Strings)
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line
print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

#Ejercicio 7 (Declaracion Multivariable)
sword_name, sword_damage, sword_length = "Excalibur", 10, 200

#Es lo mismo que:
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

#Ejercicio 8 (Desafio1)
email_start = "Thank you for shopping with us!"
email_middle = "Your total today was: "
email_end = "Please consider filling out our customer survey."
dollar_sign = "$"
total_price = "20.25"
# don't touch above this line
print(email_start)
print(email_middle+dollar_sign+total_price)
print(email_end)

#Ejercicio 9 (Desafio 2)
game_one_score = 97
game_two_score = 91
game_three_score = 106
game_four_score = 105
game_five_score = 96
game_six_score = 93
game_seven_score = 104
# Don't touch above this line
average_score = (game_one_score+game_two_score+game_three_score+game_four_score+game_five_score+game_six_score+game_seven_score)/7
# Don't touch below this line
print(round(average_score))

#Ejercicio 10 (Desafio 3)
part_one = "Roses are red, "
part_two = "violets are blue."
part_three = "Python is cool, "
part_four = "and so are you!"
# Don't touch above this line
line_one = part_one + part_two
line_two = part_three + part_four
# Don't touch below this line
print(line_one)
print(line_two)
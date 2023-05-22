#Ejercicio 1.1 
inventory = ["Healing Potion", "Leather Scraps", "Iron Helmet", "Bread","Shortsword"]
print(inventory)
#Ejercicio 1.2
inventory = ["Healing Potion", "Leather Scraps", "Iron Helmet", "Bread", "Shortsword"]
item_index = 1
item = inventory[item_index]
print(f"inventory: {inventory}")
print(f"index: {item_index}")
print(f"item: {inventory[item_index]}")
#Ejercicio 1.3
inventory = [
    "Potion",
    "Iron Breastplate",
    "Leather Scraps",
    "Iron Ore",
    "Light Leather",
    "Bread",
    "Shortsword",
    "Longsword",
    "Iron Mace",
]
last_index= len(inventory)-1
print(last_index)
last_item = inventory[last_index]
print(f"last_index: {last_index}")
print(f"last_item: {last_item}")

#Ejercicio 1.4
inventory = ["Healing Potion", "Iron Ore", "Bread", "Shortsword"]
print(inventory)
inventory[1]="Iron Bar"
print(inventory)

#Ejercicio 1.5
player_ids = []

for i in range(0, 100):
    player_ids.append(f"id:{i}")

print(player_ids)

#Ejercicio 1.6
inventory = [
    "Healing Potion",
    "Iron Bar",
    "Kite Shield",
    "Shortsword",
    "Leather Scraps",
    "Tattered Cloth",
]
print(f"inventory: {inventory}")
for i in range(0, len(inventory)):
    item=inventory.pop()
    print(f"Selling: {item}")
    print(f"inventory: {inventory}")
    
#Ejercicio 1.7
items = [
    "Potion",
    "Leather Scraps",
    "Bread",
    "Iron Ore",
    "Light Leather",
    "Bread",
    "Shortsword",
    "Longsword",
    "Iron Mace",
    "Shortsword",
    "Shortsword",
]
potion_count = 0
bread_count = 0
shortsword_count = 0
for i in range(0, len(items)):
    if items[i]=="Potion":
        potion_count += 1
    elif items[i]=="Bread":
        bread_count  += 1
    elif items[i] == "Shortsword":
        shortsword_count += 1    
    else:
        print("LEL")
print(f"You have {potion_count} potions in your inventory.")
print(f"You have {bread_count} pieces of bread in your inventory.")
print(f"You have {shortsword_count} shortswords in your inventory.")
#Ejercicio 1.8
inventory = ["Potion", "Healing Potion", "Iron Breastplate", "Leather Scraps"]
found = False
for item in inventory:
    if item == "Leather Scraps":
        found = True

if found:
    print("Found the leather scraps!")
else:
    print("Couldn't find the leather scraps!")
    
#Ejercicio 1.9
old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
new_character_levels = [1, 42, 41, 52, 12, 3, 32, 12, 54, 32, 43]

for i in range(0, len(old_character_levels)):
    if old_character_levels[i]==new_character_levels[i]:
        print("")
    else:
        print(f"index: {i}")
#Ejercicio 2.1
odd_numbers = []
for i in range(0, 300):
    if i % 3 != 0:
        odd_numbers.append(i)
print(odd_numbers)

#Ejercicio 2.2
champions = [
    "Thrundar",
    "Morgate",
    "Gandolfo",
    "Thraine",
    "Norwad",
    "Gilforn",
]
print(champions[3:])#Agarra del tercer index del comienzo al final
print (champions[:3])#Agarra del tercer index del final al comienzo
print(champions[::2])#Agarra los que son pares
#Ejercicio 2.3
johns_favorites = ["sword", "shield"]
jacks_favorites = ["potion", "hat"]
breannas_favorites = ["feather", "lance"]

all = johns_favorites + jacks_favorites + breannas_favorites #Junta todos los arrays en 1 en comun
print(all)
print(len(all)) #Muestra la longitud del array

#Ejercicio 2.3
top_weapons = [
    "sword of justice",
    "sword of slashing",
    "stabby daggy",
    "great axe",
    "silver bow",
    "spellbook",
    "spiked knuckles",
]
print(f"sword of justice is a top weapon: {'sword of justice'in top_weapons}")
print(f"great axe is a top weapon: {'great axe' in top_weapons}")
print(f"silver bow is a top weapon: {'silver bow'in top_weapons}")
#Lo que hace es que te devuelve un true si es que encuentra el valor

#Ejercicio 2.4
strongholds = [
    "Rivendale",
    "The Morgoth Mountains",
    "The Lonely Island",
    "Mordia",
    "Mordane",
    "Gondolin",
]

# del elimina cosas 
del strongholds[0] #Elimina el primer elemento del array
print(strongholds) 
del strongholds[:2]#elimina de atras para adelante empezando desde el 2
print(strongholds)

#Ejercicio 2.5 Tuples

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
print(my_tuples[0][0])
# this is the first tuple in the list

heroes = [("Glorfindel",2093,True),("Gandalf",1054,False),("Gimli",389,False),("Aragorn",87,False)]
for hero in heroes:
    print(f"name: {hero[0]}, age: {hero[1]}, is_elf: {hero[2]}")    
#name: Glorfindel, age: 2093, is_elf: True
#name: Gandalf, age: 1054, is_elf: False
#name: Gimli, age: 389, is_elf: False
#name: Aragorn, age: 87, is_elf: False

#Ejercicio 2.6
#Ve numeros pares y numeros impares 
numbers = [
    0,
    99,
    2,
    33,
    61,
    44,
    9,
    10,
    12,
    240,
    35,
    9082,
    1234,
]
num_evens = 0
num_odds = 0
for numero in numbers:
    if numero % 2 == 0:
        num_evens+=1
    else:
        num_odds+=1
print(f"There are {num_evens} even numbers and {num_odds} odd numbers.")

#Ejercicio 2.7
players = [
    "Harry",
    "Hermione",
    "Ron",
    "Ginny",
    "Fred",
    "Neville",
    "Draco",
    "Luna",
    "Cho",
    "Gregory",
    "Lee",
    "Michael",
    "Lavender",
    "Frank",
    "Anthony",
]
red_team=[]
blue_team=[]
for name in range(0,len(players)):
    if name %2==0:
        red_team.append(players[name])
    else:
        blue_team.append(players[name])
print(red_team)
print(blue_team)
print(players)

print(f"Red team has {len(red_team)} players")
print(f"Blue team has {len(blue_team)} players")

#Ejercicio 2.8 (Encontrar coincidencias en los arrays)
answer_sheet = ["A", "A", "C", "D", "D", "B", "C"]
student_answers = ["A", "B", "C", "A", "D", "B", "C"]
z=0;
for i in range(0,len(answer_sheet)):
   
    if answer_sheet[i] == student_answers[i]:
        print("coincide")
        z += 1
    else:
        print("no coincide")
percentage = 0    
percentage = z *100 / len(answer_sheet)
print(f"The student answered correctly on {percentage}% of the questions")


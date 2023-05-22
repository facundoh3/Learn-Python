#Ejercicio 1.1 (Comienzo de funciones)

def area_of_circle(r): #=> Esto sirve para declarar una funcion
    return 3.14 * r * r

player1_area = area_of_circle(1)
player2_area = area_of_circle(.5)

print(f"Player 1 has an attack area of {player1_area} meters")
print(f"Player 2 has an attack area of {player2_area} meters")

#Ejercicio 1.2 (Funciones con multiples parametros)
def calculate_damage(enemy_one_dmg, enemy_two_dmg, enemy_three_dmg):
    return enemy_one_dmg + enemy_two_dmg + enemy_three_dmg

print(f"You dealt {calculate_damage(2, 3, 4)} points of damage!")
print(f"You dealt {calculate_damage(-1, 4, 3)} points of damage!")
print(f"You dealt {calculate_damage(3, 2, 4)} points of damage!")
print(f"You dealt {calculate_damage(1, 4, 2)} points of damage!")

#Ejercicio 1.3 (Siempre despues de haber echo la funcion se declaran)
def main():
    print("Fantasy Quest is booting up...")
main()

#Ejercicio 1.4 (Scope en python)
def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)
print(f"max_health is: {max_health}")

#Ejercicio 1.5 (Scope Global en python)
player_level=4

def calculate_health(modifier):
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has {calculate_health(10)} max health.")
print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")

#Ejercicio 1.6 (Practica de funciones)=> La segunda funcion llama a la primera para que le pida el valor para operar
def to_celsius(f):
    return  5/9 * (f-32)

def test(f):
    c = round(to_celsius(f), 2)
    print(f"{f} degrees fahrenheit is {c} degrees celsius")
test(100)
test(88)
test(104)
test(112)

#Ejercicio 1.7 (Practica de funciones encontrar si palabra esta en array)
def string_exists(string_to_check, string_array):
    if string_to_check in string_array:
        return True
    else:
        return False
        
def test(string_to_check, string_array):
    exists = string_exists(string_to_check, string_array)
    if exists:
        print(f"{string_to_check} exists in {string_array}")
    else:
        print(f"{string_to_check} does NOT exist in {string_array}")


test("Healing Potion", ["Iron Bar", "Leather Scraps", "Shortsword"])
test("Iron Helmet", ["Buckler", "Leather Armor Kit", "Iron Breastplate"])
test("Iron Ore", ["Healing Potion", "Iron Ore", "Cheese"])
test("Shortsword", ["Potion", "Iron Breastplate", "Shortsword"])


#Ejercicio 1.8 (Sintaxis AND Y OR )

def does_attack_hit(attack_roll, armor_class):
    return  attack_roll != 1 and attack_roll >= armor_class 


def test(attack_roll, armor_class):
    hits = does_attack_hit(attack_roll, armor_class)
    if hits:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack hits!"
        )
    else:
        print(
            f"With a roll of {attack_roll} and armor class of {armor_class} the attack does NOT hit!"
        )

test(17, 18)
test(20, 25)
test(1, 0)
test(16, 13)
test(25, 21)

#Ejercicio 1.9 (Horas a segundos)

def convert_hours_to_seconds(hours):
    return hours * 60 

def test(hours):
    secs = convert_hours_to_seconds(hours)
    print(f"{hours} hours is {secs} seconds")

test(10)
test(1)
test(2.5)
test(100)
test(33)

#Ejercicio 2.1(Agarrar el primer elemento de array)
def get_first_item(items):
    if items == []:
        return "ERROR"
    else:
        return items[0]

def test(items):
    first = get_first_item(items)
    print(f"First item in {items} is: {first}")

test([1, 2])
test(["Healing Potion"])
test(["Iron Ore", "Iron Bar", "Scimitar"])
test([])

#Ejercicio 2.2 (Ejercicio con booleanos)
def should_serve_customer(customer_age, on_break, time):
    return 5 < time <= 10 and not on_break and customer_age >= 21

def test(customer_age, on_break, time):
    should_serve = should_serve_customer(customer_age, on_break, time)
    print(
        f"age={customer_age}, on_break={on_break}, time={time}: should_serve={should_serve}"
    )

test(22, False, 8)
test(41, False, 1)
test(22, True, 8)
test(18, True, 3)
test(23, False, 9)
test(22, False, 11)
test(21, False, 9)
test(20, False, 9)

#Ejecicio 2.3 (Encontrar el maximo numero posible )
def find_max(nums):
    max_so_far = float("-inf")
    for i in nums:
        if i > max_so_far:
            max_so_far=i
    return max_so_far
            
def test(nums):
    max = find_max(nums)
    print(f"The max of {nums} is {max}")

test([1, 2, 3, 4, 5])
test([1, 2, 300, 4, 5])
test([1, 20, 3, 4, 5])
test([-1, 2, 3, 4, 5])
test([1, 2, 3, 21, 18])
test([])

#Ejercicio 2.4 (Array Inverso)
#items[:] => Crea una copia del array
#items[::-1]=> Crea una copia inversa del array
def reverse_array(items):
    arrayReverso = items[::-1]
    return arrayReverso


def test(items):
    items_copy = items[:]
    reversed = reverse_array(items)
    print(f"{items_copy} reversed is: {reversed}")

test(["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"])
test(["Haste Potion", "Longsword", "Iron Bar", "Leather Scraps"])
test([1, 2, 300, 4, 5])
test(["now!", "order", "reverse", "in", "is", "Array", "This"])
test(["Kite Shield", "Iron Breastplate", "Healing Potion", "Shortsword"])

#Ejercicio 2.5 (Multiples return)
def filter_messages(messages):
    filtered_messages = []  # Lista para almacenar los mensajes filtrados
    counters = []  # Lista para almacenar los contadores de palabras 'dang' eliminadas
    
    for message in messages:
        words = message.split()  # Divide el mensaje en palabras
        
        clean_words = []  # Lista para almacenar las palabras no prohibidas de este mensaje
        count = 0  # Contador de palabras 'dang' eliminadas en este mensaje
        
        for word in words:
            if word == 'dang':
                count += 1  # Incrementa el contador si la palabra es 'dang'
            else:
                clean_words.append(word)  # Agrega la palabra a la lista de palabras no prohibidas
        
        clean_message = ' '.join(clean_words)  # Une las palabras no prohibidas en un solo mensaje
        
        filtered_messages.append(clean_message)  # Agrega el mensaje filtrado a la lista final
        counters.append(count)  # Agrega el contador a la lista de contadores
    
    return filtered_messages, counters
def main():
    messages = [
        "well dang it",
        "dang the whole dang thing",
        "kill that knight, dang it",
        "get him!",
        "donkey kong",
        "oh come on, get them",
        "run away from the dang baddies",
    ]
    filtered_messages, words_removed = filter_messages(messages)
    if len(filtered_messages) != len(words_removed):
        print("filtered_messages and words_removed lists should be the same size")
        return
    for i in range(0, len(filtered_messages)):
        print(
            f"Removed {words_removed[i]} words. Censored text: '{filtered_messages[i]}'"
        )


main()

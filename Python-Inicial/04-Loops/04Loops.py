#Ejercicio 1 (For)
for i in range(0,100):
    print(i)
    
#Ejercicio 1.1 
for i in range(5,16):
    print(i)
#Ejercicio 1.2 (Pasos 3er parametro)
for i in range(10,0,-1 ):
    print(i) #Empezando por el 10 hasta el 0 restando 1

#Ejercicio 1.3
for age in range(0, 75):
    if age < 8:
        print(f"You qualify for free meals. You are {age} years old.")
    elif age > 65:
        print(f"You qualify for retirement. You are {age} years old.")
#Ejercicio 1.4
total = 0
for i in range(0, 100):
    total += i
    print(i)
print(total)
#Ejercicio 1.5
total = 0
for i in range(0,100):
    if not i % 2 == 0:
        print(i)
        total += i
        
print(total)

#Ejercicio 1.6
for i in range(10,0,-1):
    print (i)
    if i == 1 :
        print("Blastoff!")
        
#Ejercicio 1.5
for i in range(100,110):
    num = i**2 
    print(f"{i} squared = {num}")
    
#Ejercicio 1.6
number_of_employees = 102
c_level_bonus = 2000
manager_bonus = 1000
standard_bonus = 500
# C Level Executives
sarah_id = 1
mary_id = 2
# Managers
john_id = 6
bob_id = 44
joe_id = 18
dollars_needed = 0
for i in range(0,number_of_employees-1):
    if i == 1 or i==2:
         dollars_needed+=c_level_bonus
    elif i==6 or i==44 or i==18:
        dollars_needed += manager_bonus
    else:
        dollars_needed +=standard_bonus
print(f"{dollars_needed} dollars are needed to fufill all bonuses")
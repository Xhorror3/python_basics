################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#local scope
# def drink_potion():
#   potion = 2
#   print(f"potion inside function: {potion}")

# drink_potion()
# print(f"potion outside function: {potion}")    #error because postion is defined in drink_portion fuction

#global scope

player_health = 10

def drink_potion():
    health_potion = 2
    print(f"player health: {player_health}")
  
drink_potion()

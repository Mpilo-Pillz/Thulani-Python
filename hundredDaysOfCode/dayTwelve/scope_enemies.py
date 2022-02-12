################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

player_health = 10

def drink_potion():
  potion_strength = 2
  print(potion_strength + player_health)



drink_potion()

# BLOCK SCOPE
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
def create_ally():
  allies = ["Amazon", "Paladin", "Barbarian"]
  if game_level < 10:
    new_ally = allies[1]
  print(new_ally)
if game_level < 5:
  new_enemy = enemies[0]


print(new_enemy)
# print(new_ally) Errors as it is scopped by function


# Modifying Global Scope
num_of_enemies = 1
num_of_allies = 3

def increase_enemies():
  # num_of_enemies += 1 Error caused by scoping
  num_of_enemies = 2
  print(f"number of enemies inside function: {num_of_enemies}")

def increase_allies():
  global num_of_allies
  num_of_allies += 1
  print(f"number of allies inside function: {num_of_allies}")

increase_enemies()
increase_allies()
print(f"number of enemies outside function: {num_of_enemies}")
print(f"number of allies outside function: {num_of_allies}")


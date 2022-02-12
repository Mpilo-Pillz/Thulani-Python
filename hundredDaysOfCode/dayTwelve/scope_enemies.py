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

